# Pruefungsprotokoll Watermarker

from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import tkinter as tk
import tkinter.filedialog

def add_watermark(input_pdf, output, watermark):

    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()

    # Watermark all the pages
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark)
        pdf_writer.addPage(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)

def create_watermark(name):
    can = canvas.Canvas("watermark.pdf", pagesize=A4)
    #print(can.getAvailableFonts())
    can.setFillColorRGB(0,0,0,alpha=0.5)
    can.setFont("Times-Bold", 36)
    can.rotate(-90)
    can.drawString(-820, 30, "Prüfungsprotokoll ausgeliehen von " + name + ".")
    can.drawCentredString(-450, 550, "Nicht zur Weitergabe!")
    can.save()
    wm = PdfFileReader("watermark.pdf")
    return wm.getPage(0)

root = tk.Tk()

def make():
    add_watermark(file,"protokoll.pdf",create_watermark(person.get()))

def choose():
    global file
    file = tk.filedialog.askopenfilename(filetypes=(('pdf files', '*.pdf'),))
    file_label["text"] = file.split("/")[-1]

tk.Label(root, text="Person:").grid(row=0, column=0)
person = tk.Entry(root)
person.grid(row=0, column=1)
tk.Button(root, text="Wähle Datei", command=choose).grid(row=1, column=0)
file_label = tk.Label(root, text="Dateiname")
file_label.grid(row=1, column=1)
tk.Button(root, text="Watermark erstellen",command=make).grid(row=2,column=0,columnspan=2)
tk.mainloop()