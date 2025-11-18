from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader, PdfWriter
import io
import os
import copy

# Регистрируем шрифт
pdfmetrics.registerFont(TTFont('DejaVuSans', 'test_pdf_editor/DejaVuSans.ttf'))

# Пути для сохранения
mask_output_path = "test_pdf_editor/output_mask.pdf"
merged_output_path = "test_pdf_editor/output_merged.pdf"
template_path = "test_pdf_editor/diploma.pdf"

# Создаем кастомный размер страницы 309 × 222 мм в горизонтальной ориентации
CUSTOM_SIZE = (309 * mm, 222 * mm)  # 309 мм ширина, 222 мм высота

# Пример списка словарей с данными для каждого листа
data_list = [
    {
        'name': 'Иванов Иван Иванович',
        'place': '1',
        'weight_category': '20 A',
        'age_group': '2019-2020'
    },
    {
        'name': 'Петров Петр Петрович',
        'place': '2',
        'weight_category': '25 B',
        'age_group': '2019-2020'
    },
    {
        'name': 'Сидоров Алексей Николаевич',
        'place': '3',
        'weight_category': '30 C',
        'age_group': '2018-2019'
    },
    {
        'name': 'Очень Длинное Имя Одну Строку',
        'place': '1',
        'weight_category': '35 D',
        'age_group': '2020-2021'
    }
    # Добавьте столько словарей, сколько нужно страниц
]

# Функция для центрирования текста по горизонтали
def draw_centered_text(canvas, text, y, font_name, font_size):
    """
    Рисует текст по центру страницы по горизонтали.
    Вычисляет ширину текста и корректирует координату X.
    """
    canvas.setFont(font_name, font_size)
    text_width = canvas.stringWidth(text, font_name, font_size)
    x = (CUSTOM_SIZE[0] - text_width) / 2  # Используем кастомную ширину
    canvas.drawString(x, y, text)

# Создаем временный PDF в памяти для маски
packet = io.BytesIO()

# Создаем canvas с кастомным размером страницы
can = canvas.Canvas(packet, pagesize=CUSTOM_SIZE)

# Проходим по всем элементам списка и создаем страницу для каждого
for data in data_list:
    # ВАЖНО: Устанавливаем прозрачность через сохранение состояния
    can.saveState()
    
    # Рисуем прозрачный прямоугольник на всю страницу
    can.setFillColorRGB(1, 1, 1, alpha=0)  # Полностью прозрачный
    can.rect(0, 0, CUSTOM_SIZE[0], CUSTOM_SIZE[1], fill=1, stroke=0)
    can.restoreState()
    
    # Теперь устанавливаем черный цвет для текста
    can.setFillColorRGB(0, 0, 0)  # Черный текст
    
    # Рисуем центрированное ФИО
    draw_centered_text(can, data['name'], 350, 'DejaVuSans', 24)
    
    # Остальной текст рисуем как раньше (координаты остаются прежними)
    can.setFont("DejaVuSans", 24)
    can.drawString(430, 315, data['place'])
    
    can.setFont("DejaVuSans", 16)
    can.drawString(280, 225, data['weight_category'])
    can.drawString(530, 225, data['age_group'])
    
    # Завершаем текущую страницу и начинаем новую (если это не последний элемент)
    if data != data_list[-1]:
        can.showPage()

# Завершаем рисование
can.save()

# Перемещаем указатель на начало буфера
packet.seek(0)

# Сохраняем маску отдельно
with open(mask_output_path, "wb") as output_stream:
    output_stream.write(packet.getvalue())

# Теперь создаем версию с наложением на шаблон
# Проверяем, существует ли файл шаблона
if not os.path.exists(template_path):
    print(f"Файл шаблона не найден: {template_path}")
else:
    # Читаем созданную маску
    new_pdf = PdfReader(packet)
    
    # Читаем исходный шаблон
    with open(template_path, "rb") as f:
        existing_pdf = PdfReader(f)
        output = PdfWriter()

        # Для каждой страницы маски создаем отдельную страницу с наложением
        for i in range(len(new_pdf.pages)):
            # Берем страницу шаблона (если страниц меньше, чем в маске, используем первую)
            if i < len(existing_pdf.pages):
                # Создаем глубокую копию страницы шаблона
                template_page = existing_pdf.pages[i]
            else:
                template_page = existing_pdf.pages[0]
            
            # Создаем временный PDF для отдельной страницы
            single_page_packet = io.BytesIO()
            single_page_writer = PdfWriter()
            single_page_writer.add_page(template_page)
            single_page_writer.write(single_page_packet)
            single_page_packet.seek(0)
            
            # Читаем отдельную страницу
            single_page_reader = PdfReader(single_page_packet)
            single_page = single_page_reader.pages[0]
            
            # Накладываем маску на отдельную страницу шаблона
            single_page.merge_page(new_pdf.pages[i])
            output.add_page(single_page)

        # Сохраняем объединенный документ
        with open(merged_output_path, "wb") as output_stream:
            output.write(output_stream)

print(f"Маска успешно сохранена как {mask_output_path}")
print(f"Файл с наложением на шаблон сохранен как {merged_output_path}")
print(f"Файл для проверки был сохранен тут: {merged_output_path}")