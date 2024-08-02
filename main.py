import pandas
import glob
from fpdf import FPDF
from pathlib import Path

# Get a list of filepaths to the files
filepaths = glob.glob("texts/*.txt")

# Create pdf file
pdf = FPDF(orientation="P", unit="mm", format="A4")



# Generate pages with titles
for filepath in filepaths:

    pdf.add_page()
    print(filepath)

    # Get filename in order to use it for pdf file name and title
    filename = Path(filepath).stem.title() # "Path" - get path to file, "stem" - separates the name and return str,

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=filename, ln=1)


    # Add description(text) from external files
    with open(filepath, "r") as file:
        content = file.readline()
        pdf.set_font(family="Times", size=12, style="I")
        pdf.multi_cell(w=190, h=7, txt=content)
    print(content)
    print(type(content))
    print(filename)
    print(type(filename))

pdf.output(f"PDFs/output.pdf")