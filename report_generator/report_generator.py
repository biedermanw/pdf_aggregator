# report_generator.py
import psycopg2
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


class ReportGenerator:
    def __init__(self, database):
        self.database = database
        self.query = ''

    def set_query(self, query):
        self.query = query

    def generate_pdf_report(self, output_file_path):
        # Connect to the database
        conn = psycopg2.connect(self.database)
        cursor = conn.cursor()

        # Execute the SQL query
        cursor.execute(self.query)
        result = cursor.fetchall()

        # Create a PDF document
        doc = SimpleDocTemplate(output_file_path, pagesize=letter)
        elements = []

        # Define table data and styles
        data = []
        headers = []
        for column in cursor.description:
            headers.append(column.name)
        data.append(headers)

        for row in result:
            data.append(list(row))

        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))

        elements.append(table)

        # Build the PDF document
        doc.build(elements)

        # Close the database connection
        cursor.close()
        conn.close()
