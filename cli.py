import argparse
import os
from dotenv import load_dotenv
from report_generator.report_generator import ReportGenerator

# Load environment variables from .env file
load_dotenv()


def main():
    parser = argparse.ArgumentParser(description='PyReportGenerator CLI')
    parser.add_argument('-d', '--database', help='Database connection string')
    parser.add_argument('-q', '--query', help='SQL query')
    parser.add_argument('-o', '--output', help='Output file path')

    args = parser.parse_args()

    # Use DATABASE_CONNECTION_STRING from .env or --database arg.
    if not args.database:
        args.database = os.environ.get('DATABASE_CONNECTION_STRING')

    # Define the required arguments and error messages.
    req_args = {
        'database': 'Missing database connection string.',
        'query': 'Missing SQL query',
        'output': 'Missing output file path.'
    }

    # Check if any of the required args are missing
    bad_args = [arg for arg, err in req_args.items() if not getattr(args, arg)]
    if bad_args:
        parser.error('\n'.join(req_args[arg] for arg in bad_args))

    output_file_path = os.path.join("output_files", args.output)
    report_generator = ReportGenerator(args.database)

    report_generator.set_query(args.query)
    report_generator.generate_pdf_report(output_file_path)


if __name__ == '__main__':
    main()
