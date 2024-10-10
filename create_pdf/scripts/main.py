import argparse
import random
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
import os

def create_pdf(num_pages, target_size_mb):
    # pdfディレクトリが存在しない場合は作成
    pdf_dir = 'pdf'
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)

    filename = f"pdf_{num_pages}pages_{target_size_mb}MB.pdf"
    filepath = os.path.join(pdf_dir, filename)

    doc = SimpleDocTemplate(filepath, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch, leftMargin=0.5*inch, rightMargin=0.5*inch)
    styles = getSampleStyleSheet()
    custom_style = ParagraphStyle('CustomStyle', fontSize=12, leading=14, textColor=colors.black)

    story = []

    for i in range(1, num_pages + 1):
        # ページタイトル
        story.append(Paragraph(f"Page {i}", styles['Heading1']))

        # サンプルテキスト（より多くのテキストを追加）
        sample_text = f"This is page number {i} of our {num_pages}-page PDF document. " * 50
        story.append(Paragraph(sample_text, custom_style))

        # 最後のページ以外に改ページを追加
        if i < num_pages:
            story.append(PageBreak())

    doc.build(story)

    # ファイルサイズが目標に達するまでダミーデータを追加
    current_size = os.path.getsize(filepath)
    target_size = target_size_mb * 1024 * 1024  # Convert MB to bytes

    if current_size < target_size:
        with open(filepath, 'ab') as f:
            f.write(b'\0' * (target_size - current_size))

    print(f"{num_pages}-page PDF has been created successfully as '{filepath}'!")
    print(f"File size: {os.path.getsize(filepath) / (1024 * 1024):.2f} MB")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a multi-page PDF with specified file size')
    parser.add_argument('--pages', type=int, default=100, help='Number of pages to generate (default: 100)')
    parser.add_argument('--size', type=int, default=10, help='Target file size in MB (default: 10)')
    args = parser.parse_args()

    create_pdf(args.pages, args.size)
