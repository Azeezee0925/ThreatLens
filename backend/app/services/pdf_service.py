from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(result):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph("<b>ThreatLens AI Investigation Report</b>", styles["Title"])
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(f"<b>IOC:</b> {result['ioc']}", styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>IOC Type:</b> {result['ioc_type']}", styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>Status:</b> {result['status']}", styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>ThreatLens Score:</b> {result['threatlens_score']}/100", styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>Confidence:</b> {result['confidence']}%", styles["BodyText"])
    )

    story.append(Spacer(1, 15))

    story.append(
        Paragraph("<b>Executive Summary</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(result["executive_summary"], styles["BodyText"])
    )

    story.append(Spacer(1, 10))

    story.append(
        Paragraph("<b>Risk Assessment</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(result["risk_assessment"], styles["BodyText"])
    )

    story.append(Spacer(1, 10))

    story.append(
        Paragraph("<b>Recommendation</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(result["ai_recommendation"], styles["BodyText"])
    )

    doc.build(story)

    buffer.seek(0)

    return buffer