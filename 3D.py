import PyPDF2
import re

import tabula

# Set the path to your PDF file
pdf_file = "chap1.pdf"

# Open the PDF file in binary mode
with open(pdf_file, 'rb') as f:

    # Create a PyPDF2 PdfFileReader object to read the PDF file
    pdf_reader = PyPDF2.PdfFileReader(f)

    # Loop through each page in the PDF file
    for page_num in range(pdf_reader.numPages):

        # Get the text content of the page
        page = pdf_reader.getPage(page_num)
        page_text = page.extractText()

        # Extract tables using Tabula
        # Set the area of the page containing the table you want to extract
        # You can use the "guess" parameter to automatically detect the table
        # coordinates, or you can set them manually using the format (top, left, bottom, right)
        table_area = (0, 0, 100, 100)

        # Extract the table from the page using Tabula
        table_df = tabula.read_pdf(pdf_file, pages=page_num+1, area=table_area)

        # Print the contents of the table
        if not table_df.empty:
            print("Table found on page", page_num+1)
            print(table_df)

        # Extract text using regular expressions
        # Define your regular expression pattern
        pattern = r"Your pattern here"

        # Search for the pattern in the page text
        matches = re.findall(pattern, page_text)

        # Print the matches
        if matches:
            print("Matches found on page", page_num+1)
            print(matches)
