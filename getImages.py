

import fitz  # PyMuPDF
import os,glob

def extract_images_from_pdf(pdf_path, output_folder):
    cwd=os.getcwd()
    #get all pdf files
    files=glob.glob(cwd+"/"+pdf_path+"/*.pdf")
    
    # Open the PDF file
    for pdf_path in files:
        pdf_document = fitz.open(pdf_path)
        name=pdf_path.split("/")[-1]
        # Loop through each page
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            
            # Get all images on the page
            image_list = page.get_images(full=True)
            
            for img_index, image in enumerate(image_list):
                xref = image[0]  # Image reference number
                image_bytes = pdf_document.extract_image(xref)
                image_filename = os.path.join(output_folder, f"image_{name}_{page_num + 1}_{img_index + 1}.png")
                
                # Save the image
                with open(image_filename, "wb") as img_file:
                    img_file.write(image_bytes["image"])
                    print(f"Images extracted to {output_folder} for {pdf_path}")

        # print(f"Images extracted to {output_folder} for {pdf_path}")

# Example usage for change
# pdf_path = "path_to_your_pdf.pdf"
# output_folder = "path_to_output_folder"
#extract_images_from_pdf("masterdata" ,"images")
