from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import io
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('DejaVuSans', 'test_pdf_editor\DejaVuSans.ttf'))

# Шаблон: путь к исходному PDF
input_pdf_path = "test_pdf_editor/diploma.pdf"
output_pdf_path = "test_pdf_editor/output.pdf"

# Создаем временный PDF в памяти с нужным текстом
packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=A4)

# Настройки шрифта
can.setFont("DejaVuSans", 24)

# Добавляем текст в нужные координаты (проверьте, подходят ли координаты для вашего PDF)
can.drawString(300, 350, "Иванов Иван Иванович")
can.drawString(430, 315, "1")
can.drawString(425, 245, "28")


# Завершаем рисование
can.save()

# Перемещаем указатель на начало буфера
packet.seek(0)

# Читаем временный PDF
new_pdf = PdfReader(packet)

# Читаем исходный PDF
with open(input_pdf_path, "rb") as f:
    existing_pdf = PdfReader(f)
    output = PdfWriter()

    # Берём первую страницу
    page = existing_pdf.pages[0]

    # Накладываем новый текст на существующую страницу
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)

    # Сохраняем результат
    with open(output_pdf_path, "wb") as output_stream:
        output.write(output_stream)

print(f"PDF успешно сохранён как {output_pdf_path}")
