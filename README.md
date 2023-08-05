this is the script to convert a pdf file to txt file
here is the line by line explanation
import PyPDF2
# python library to work with pdf 

def pdf_to_txt(pdf_file, txt_file):
#   function takes two arguments
#   path of the pdf file to be converted
#   path  of the txt file to be saved
  

  pdf_reader = PyPDF2.PdfReader(pdf_file)
  #reads the file
  num_pages = len(pdf_reader.pages)
  #counts the number of pages

  with open(txt_file, "w") as txt_writer:#open the file in write mode
    for page in range(num_pages):#iterates over lines in the pdf
      text = pdf_reader.pages[page].extract_text()#text variable stores the data
      txt_writer.write(text)#writes down the data

if __name__ == "__main__":
  pdf_file = "input.pdf"                note :WRITE THE NAME OF YOUR OWN PDF FILE TO BE CHANGED
  txt_file = "output.txt"

  pdf_to_txt(pdf_file, txt_file)

  print("PDF file converted to TXT file successfully!")
