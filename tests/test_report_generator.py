import os
import unittest
import PyPDF2
import psycopg2

from decimal import Decimal
from dotenv import load_dotenv
from report_generator.report_generator import ReportGenerator

# Load environment variables from .env file.
load_dotenv()


class TestReportGenerator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.database = os.environ.get('DATABASE_CONNECTION_STRING')
        cls.query = '''
            SELECT
                u.name AS user,
                u.email,
                c.name AS company,
                c.location,
                r.rate
            FROM
                users AS u
                LEFT JOIN companies AS c
                    ON u.company_id = c.id
                LEFT JOIN hourly_rates AS r
                    ON r.company_id = c.id
            ;
        '''
        cls.report_generator = ReportGenerator(cls.database)

    def test_set_query(self):
        self.report_generator.set_query(self.query)
        self.assertEqual(self.query, self.report_generator.query)

    def test_generate_pdf_report(self):
        output_path = 'test_output.pdf'
        self.report_generator.set_query(self.query)
        self.report_generator.generate_pdf_report(output_path)

        # Verify that the output file is created.
        self.assertTrue(os.path.exists(output_path))

        # Check if the PDF file has pages.
        self.assertGreater(os.path.getsize(output_path), 0)

        # Extract rows from the DB.
        db_rows = self.query_database(self.query)

        # Extract the PDF's contents as rows, skipping the header.
        pdf_rows = self.extract_text_from_pdf(output_path, len(db_rows[0]))

        # Compare PDF rows with the database query result.
        self.assertEqual(pdf_rows, db_rows)

        # Clean up the test output.
        os.remove(output_path)

    def extract_text_from_pdf(self, file_path, row_len):
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            rows = []
            for page in pdf_reader.pages:
                text = page.extract_text().split('\n')
                table_data = [cell.strip() for cell in text if cell.strip()]

                # Extract the table data.
                headers = table_data[:row_len]
                data = table_data[row_len:]

                row_range = range(0, len(data), row_len)
                row_data = [data[i:i+row_len] for i in row_range]
                rows.extend(
                    [headers] + row_data
                )
            return rows[1:]

    def query_database(self, query):
        conn = psycopg2.connect(self.database)
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        # Convert decimal values to strings for easier comparison.
        rows = [
            [
                str(value) if isinstance(value, Decimal) else value
                for value in row
            ]
            for row in rows
        ]

        cursor.close()
        conn.close()
        return rows

    def format_database_rows(self, rows):
        formatted_rows = []
        for row in rows:
            # Convert values to strings for easier comparison.
            formatted_row = [str(cell) for cell in row]
            formatted_rows.append(formatted_row)
        return formatted_rows


if __name__ == '__main__':
    unittest.main()
