# Import the necessary modules
import pyttsx3
import PyPDF2

# Open our file in reading format and store into book
book = open('demo.pdf', 'rb')  # `rb` stands for reading mode

# Use PyPDF2's PdfReader method on book and store it into pdf_reader
pdf_reader = PyPDF2.PdfReader(book)

# Get the number of pages in our pdf
num_pages = len(pdf_reader.pages)

# Initialize pyttsx3 using init method and let's print playing Audiobook
play = pyttsx3.init()
print('Playing Audio Book')

# Run a loop for the number of pages in our pdf file. 
# A page will get retrieved at each iteration.
for num in range(0, num_pages):
    page = pdf_reader.pages[num]
    # Extract the text from our page using extract_text method on our page and store it into data.
    data = page.extract_text()

    # Call say method on data and finally we can call runAndWait method at the end.    
    play.say(data)
    play.runAndWait()

# Close the PDF file
book.close()