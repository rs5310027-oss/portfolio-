import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Load Excel data
df = pd.read_excel("sales_data.xlsx")

# Calculate total sales
total_sales = df["Sales"].sum()

# Create PDF
pdf = SimpleDocTemplate("business_report.pdf", pagesize=letter)

styles = getSampleStyleSheet()
elements = []

# Title
elements.append(Paragraph("Business Sales Report", styles['Title']))

# Summary
elements.append(
    Paragraph(f"Total Sales: ₹{total_sales}", styles['Normal'])
)

# Table data
data = [df.columns.tolist()] + df.values.tolist()

table = Table(data)
elements.append(table)

# Build PDF
pdf.build(elements)

print("PDF report generated successfully!")