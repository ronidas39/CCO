from getImages import extract_images_from_pdf
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
import chromadb
import os,glob,shutil,io
from datasets import load_dataset
from chromadb.utils.data_loaders import ImageLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import UnstructuredEmailLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
load_dotenv()
text_splitter=RecursiveCharacterTextSplitter(chunk_size=4000,chunk_overlap=100)


extensions = ["*.jpg", "*.jpeg", "*.png", "*.gif"]

from datetime import datetime

def generate_unique_id():
    # Get the current timestamp
    now = datetime.now()
    
    # Format the datetime to a string
    unique_id = now.strftime("%Y%m%d%H%M%S%f")  # Year, Month, Day, Hour, Minute, Second, Microsecond
    
    return unique_id



def createCollection(path,collection_name):
    # Instantiate the Image Loader
    image_loader = ImageLoader()
    # Instantiate CLIP embeddings
    embedding_function = OpenCLIPEmbeddingFunction()
    #embedding_function=OpenAIEmbeddings()
    client = chromadb.PersistentClient(
        path=f"./{path}"
    )

    collection = client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_function,
        data_loader=image_loader,
        
        )
    return collection

def addImageToCollection(path,collection_name,image_folder):
    client = chromadb.PersistentClient(
        path=f"./{path}"
    )
    embedding_function = OpenCLIPEmbeddingFunction()
    image_loader = ImageLoader()
    # Initialize lists for ids and uris
    ids = []
    uris = []
    collection=client.get_collection(
        name=collection_name,
        embedding_function=embedding_function,
        data_loader=image_loader,
    )
    # Iterate over each file in the dataset folder
    for ext in extensions:
        # Use glob to find files with the current extension
        files = glob.glob(os.path.join(image_folder, ext))
        
        # Enumerate through files and append to lists
        for i, file_path in enumerate(sorted(files)):
            ids.append(generate_unique_id())  # Use len(ids) to maintain sequential numbering across extensions
            uris.append(file_path)
            print(file_path)

    # Add to image collection
    print(ids)
    if ids:
        collection.add(
            ids=ids,
            uris=uris
        )

        print("Images added to the database.")
        # with io.open("id.txt","w",encoding="utf-8")as f1:
        #     id_string = ", ".join(ids)
        #     f1.write(id_string)
    else:
        print("not image found to add")

addImageToCollection("index_db","multimodal_collection","images")
def loadEmail(path,collection_name,persist_directory):
    cwd=os.getcwd()
    files = glob.glob(cwd+"/"+path+"/*.eml")
    for file in files:
        loader = UnstructuredEmailLoader(file)
        docs = loader.load()
        splited_docs=text_splitter.split_documents(docs)
        print(len(splited_docs))
        vs=Chroma(collection_name=collection_name,
                  embedding_function=OpenAIEmbeddings(),
                  persist_directory=f"./{persist_directory}")
        vs.add_documents(docs)

        
#loadEmail("masterdata","text_collection","index_db")
        
def loadPdf(path,collection_name,persist_directory):
    cwd=os.getcwd()
    files = glob.glob(cwd+"/"+path+"/*.pdf")
    for file in files:
        loader = PyPDFLoader(file)
        docs = loader.load()
        splited_docs=text_splitter.split_documents(docs)
        print(len(splited_docs))
        vs=Chroma(collection_name=collection_name,
                  embedding_function=OpenAIEmbeddings(),
                  persist_directory=f"./{persist_directory}")
        vs.add_documents(docs)
    #     context=vs.similarity_search("Business Plan: The Gentry Collection",k=3)
    # print(context)

#loadPdf("masterdata","text_collection","index_db")
        