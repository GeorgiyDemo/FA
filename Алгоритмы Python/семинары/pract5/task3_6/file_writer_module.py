
from fpdf import FPDF
import qrcode

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('./img/logo.gif', 10, 8, 33)
        self.image('./img/qr.png', 160, 8, 40)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'MEOW', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

if __name__ == "__main__":
    
    img = qrcode.make('Some data here')
    img.save("./img/qr.png")

    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    for i in range(1, 41):
        pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)

    pdf.output('./pdf/tuto2.pdf', 'F')