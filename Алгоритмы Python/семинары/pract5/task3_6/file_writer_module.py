
from fpdf import FPDF
import qrcode

class PDFWriter():

    def __init__(self, header, main_text, qr_text, pdf_filename_to_save):
        
        self.pdf_filename_to_save = pdf_filename_to_save
        self.processed_flag = False
        self.header = header.split("\n")
        self.main_text = main_text.split("\n")
        self.qr_text = qr_text
        self.processing()

        

    def processing(self):
        

        img = qrcode.make(self.qr_text)
        img.save("./img/qr.png")
        

        pdf = FPDF()
        pdf.add_page()
        pdf.add_font('Times', 'B', './img/times.ttf', uni=True)
        pdf.set_font('Times', 'B', 16)

        pdf.image('./img/logo.gif', 10, 10, 33)
        pdf.image('./img/qr.png', 160, 8, 45)

        for header in self.header:

            pdf.cell(75)
            pdf.cell(30, 10, header, 0, 1, "C")
        
       
        pdf.ln(20)
        pdf.add_font('Times', '', './img/times.ttf', uni=True)
        pdf.set_font('Times', '', 14)
        
        for t in self.main_text:
            pdf.cell(0, 10, t, 0, 1)
        
        pdf.output('./pdf/'+self.pdf_filename_to_save, 'F')
        self.processed_flag = True