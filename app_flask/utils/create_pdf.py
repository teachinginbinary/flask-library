from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from io import BytesIO

def create_pdf(book):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    styles = getSampleStyleSheet()

    style_titulo = styles["Heading1"]
    style_titulo.fontSize = 16 # Aumentar el tamaño de fuente del título
    style_titulo.textColor = 'black' # Color del texto
    style_titulo.leading = 18 # Espaciado entre líneas
    
    # Definir el estilo para el texto con tamaño de fuente aumentado
    style_texto = styles["BodyText"]
    style_texto.fontSize = 12 # Aumentar el tamaño de fuente del texto
    style_texto.leading = 15 # Espaciado entre líneas
    
    # Ajustar las coordenadas para mover el contenido más abajo
    y_titulo = 700
    y_texto = 320
    
    # Dibujar el título del libro
    titulo = Paragraph(book.name, style_titulo)
    titulo.wrapOn(c, 500, y_titulo)
    titulo.drawOn(c, 50, y_titulo)
    
    # Dibujar el texto del libro
    texto = Paragraph(book.text, style_texto)
    texto.wrapOn(c, 500, y_texto)
    texto.drawOn(c, 50, y_texto)
    # Asegurarse de que se cierre el último texto antes de guardar
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer