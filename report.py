from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(result):
    doc = SimpleDocTemplate("report.pdf")
    styles = getSampleStyleSheet()

    content = []
    content.append(Paragraph("AI Detection Report", styles['Title']))
    content.append(Paragraph(result["decision"], styles['Normal']))
    content.append(Paragraph(str(result["final_score"]), styles['Normal']))

    doc.build(content)