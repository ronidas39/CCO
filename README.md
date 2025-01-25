read me about the repo
===========================

knowledgebase is available as persistent storage inside index_db directory
created two collection one for text and one image , this already support multimodal .
If required in future we cab audio and video inside the same index_db by adding new collections.
Right now all pdf,eml and image data is avaialble inside the collection , if required we can build again.


##getImages.py module is used to extract all images from each pdf file , this images will be used later to build the knowledgebase
## **Python Module: Extract Images from PDF**

### **Description**
This script extracts all embedded images from PDF files located in a specified folder. It uses the `PyMuPDF` library (imported as `fitz`) to process the PDFs and save the extracted images into a designated output folder.

The script loops through each page of every PDF in the input directory, identifies all the images on the page, and saves them as `.png` files in the output folder. 

### **Dependencies**
Ensure you have the following Python libraries installed:
- `PyMuPDF` (also known as `fitz`): Used to handle PDF files and extract images.
- `os` and `glob`: Used to work with directories and fetch file paths.

You can install `PyMuPDF` using pip:
```bash
pip install pymupdf
```

### **Functions**

#### `extract_images_from_pdf(pdf_path, output_folder)`
This function extracts images from PDF files in the specified folder.

#### **Parameters**
- `pdf_path` (str): The relative or absolute path to the folder containing the PDF files.
- `output_folder` (str): The folder where the extracted images will be saved.

#### **Steps**
1. Get the current working directory using `os.getcwd()`.
2. Fetch all `.pdf` files in the specified `pdf_path` folder using the `glob` module.
3. For each PDF file:
   - Open the file using `fitz.open(pdf_path)`.
   - Loop through each page of the PDF using `pdf_document.page_count`.
   - Use `page.get_images(full=True)` to get all image references on the page.
   - Extract each image using `pdf_document.extract_image(xref)`.
   - Save the image as a `.png` file in the output folder with a filename format:
     ```
     image_<pdf_filename>_<page_number>_<image_index>.png
     ```
4. Print a message confirming the extraction for each PDF.

### **Example Usage**

Here’s an example of how to use the script:

```python
# Specify the folder containing PDFs and the folder for extracted images
pdf_folder = "masterdata"        # Folder containing PDF files
output_folder = "images"         # Folder to save extracted images

# Call the function
extract_images_from_pdf(pdf_folder, output_folder)
```

### **Expected Behavior**
- The script will extract all images from the PDFs located in the `masterdata` folder.
- It will save the extracted images in the `images` folder.
- The images will be named using the format:
  ```
  image_<pdf_filename>_<page_number>_<image_index>.png
  ```
  For example:
  ```
  image_sample.pdf_1_1.png
  image_sample.pdf_1_2.png
  image_sample.pdf_2_1.png
  ```
  
###The buildKb.py script provided integrates functionalities for creating, managing, and querying multimodal collections using **ChromaDB** with the help of embedding functions for image and text-based data (emails and PDFs). Below is a breakdown of its functionalities:

---

### **Purpose**
1. Extract images from PDFs and add them to a multimodal collection.
2. Load email and PDF files into a ChromaDB collection.
3. Use embedding models for efficient similarity search across image and text data.

---

### **Script Overview**

#### **Imports**
- **Core Libraries**: `os`, `glob`, `shutil`, `io`, and `datetime`.
- **ChromaDB**: Provides database-like functionality for vector storage.
- **LangChain**: Used for text-based document splitting and embedding.
- **Dataset and Loader Utilities**: Used to parse and load different file types (`emails`, `PDFs`, `images`).
- **Embedding Models**: 
  - `OpenCLIPEmbeddingFunction` for images.
  - `OpenAIEmbeddings` for text.

---

### **Functions**

#### **1. `generate_unique_id()`**
Generates a unique ID using the current timestamp down to the microsecond.

- **Usage**:
```python
unique_id = generate_unique_id()
```

- **Example Output**:
`20250125153545896321`

---

#### **2. `createCollection(path, collection_name)`**
Creates a new multimodal collection in ChromaDB.

- **Parameters**:
  - `path`: Directory where the ChromaDB index will be stored.
  - `collection_name`: Name of the collection to create.

- **Returns**:
  A ChromaDB collection with the specified name.

- **Usage**:
```python
collection = createCollection("index_db", "multimodal_collection")
```

---

#### **3. `addImageToCollection(path, collection_name, image_folder)`**
Adds images to an existing ChromaDB collection.

- **Parameters**:
  - `path`: Path to the ChromaDB index.
  - `collection_name`: Name of the collection to update.
  - `image_folder`: Folder containing the image files.

- **Workflow**:
  - Iterates through a predefined list of image extensions (`extensions`).
  - Extracts image paths and assigns a unique ID to each image.
  - Adds the images to the ChromaDB collection.

- **Usage**:
```python
addImageToCollection("index_db", "multimodal_collection", "images")
```

---

#### **4. `loadEmail(path, collection_name, persist_directory)`**
Loads `.eml` email files into a ChromaDB collection.

- **Parameters**:
  - `path`: Path to the folder containing `.eml` files.
  - `collection_name`: Name of the ChromaDB collection for text data.
  - `persist_directory`: Directory where the ChromaDB index is stored.

- **Workflow**:
  - Iterates through `.eml` files and processes them with `UnstructuredEmailLoader`.
  - Splits the text into manageable chunks using `RecursiveCharacterTextSplitter`.
  - Adds the documents to the ChromaDB collection.

- **Usage**:
```python
loadEmail("masterdata", "text_collection", "index_db")
```

---

#### **5. `loadPdf(path, collection_name, persist_directory)`**
Loads `.pdf` files into a ChromaDB collection.

- **Parameters**:
  - `path`: Path to the folder containing `.pdf` files.
  - `collection_name`: Name of the ChromaDB collection for text data.
  - `persist_directory`: Directory where the ChromaDB index is stored.

- **Workflow**:
  - Processes `.pdf` files using `PyPDFLoader`.
  - Splits the text into chunks using `RecursiveCharacterTextSplitter`.
  - Adds the documents to the ChromaDB collection.

- **Usage**:
```python
loadPdf("masterdata", "text_collection", "index_db")
```

---

### **How to Use the Script**

1. **Setup Environment**:
   - Ensure you have ChromaDB, LangChain, and other required libraries installed:
     ```bash
     pip install chromadb langchain pymupdf datasets
     ```

2. **Extract Images and Create Image Collection**:
   - Place your images or PDFs containing images in a folder.
   - Extract images (if necessary) and add them to the image collection:
     ```python
     from getImages import extract_images_from_pdf
     extract_images_from_pdf("masterdata", "images")
     addImageToCollection("index_db", "multimodal_collection", "images")
     ```

3. **Load Text-Based Documents**:
   - For emails:
     ```python
     loadEmail("masterdata", "text_collection", "index_db")
     ```
   - For PDFs:
     ```python
     loadPdf("masterdata", "text_collection", "index_db")
     ```

4. **Access and Query Collections**:
   - Use ChromaDB to search for documents or images based on embeddings.

---

### **Notes**
- **ChromaDB Persistence**: The `PersistentClient` ensures your collections are saved and retrievable across sessions.
- **Embedding Models**: 
  - Use `OpenCLIPEmbeddingFunction` for images.
  - Use `OpenAIEmbeddings` for text.
- **File Organization**: Ensure your input folders (`masterdata`, `images`) are properly set up.


  


