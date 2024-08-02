import pandas
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("texts/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    print(filepath)
    filename = Path(filepath).stem
    pdf.cell(w=50, h=8, txt=filename.title())
    print(filename)
    print(type(filename))
pdf.output(f"PDFs/output.pdf")