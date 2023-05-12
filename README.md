# PDF Aggregator

PDF Aggregator is a Python library and wrapper script that generates a PDF report based on data provided. It uses the ReportLab library to create the PDF document.

## Features

- Generate PDF reports with customizable data.
- Support for fetching data from a PostgreSQL database.
- Simple and easy-to-use interface.

## Installation

1. Clone the repository:

```shell
git clone https://github.com/williambiederman/pdf-aggregator.git
```

2. Change into the project directory:

```shell
cd pdf-aggregator
```

3. Install the required dependencies:
    - Using a virtual environment

    ```shell
    python -m venv venv
    . venv/bin/activate
    (venv) pip install -r requirements.txt
    ```

    - Directly.

    ```shell
    pip install -r requirements.txt
    ```

4. *Optional:* Copy the `.env_example` file to `.env` and update the `DATABASE_CONNECTION_STRING`. You can pass this in with the `--database` option later.

## Usage

This tool allows a user to dynamically create a PDF from data in a PostgreSQL table with the following command.

```
python main.py -d DATABASE_CONNECTION_STRING -q SQL_QUERY -o OUTPUT_FILENAME
```

### Arguments
-d, --database: Database connection string. This can also be set in a `.env` file.
-q, --query: SQL query to be rendered in the PDF.
-o, --output: Output file path.

If the --database argument is not provided, the tool will attempt to use the DATABASE_CONNECTION_STRING from the .env file.

If any of the required arguments are missing, an error message will be displayed.

## Example Setup

If you do not already have a PostgreSQL installation and would like to use the example server, follow these steps.

### Dockerized PostgreSQL Setup

Navigate to the root directory of this project and modify the `Dockerfile` with any credentials you'd like.

Build the image using the `Dockerfile`.

```
docker build -t example-postgres-image .
```

Next, run the container with this command.

```
docker run -d --name example-postgres-container -p 5432:5432 example-postgres-image
```

You can use this command with the settings from the `Dockerfile` to test the connection.

```
docker exec -it example-postgres-container psql -h localhost -p 5432 -U POSTGRES_USER -d POSTGRES_DB
```

## Unit Test

If you've set the DATABASE_CONNECTION_STRING in the `.env` file, you can run the current unit tests by navigating to the root directory of the project and using this commands.

```shell
python -m unittest discover -s tests -p 'test_*.py'
```

*Note: If you're using a virtual environment, you'll have to activate it to run tests.*

## License

This project is licensed under the MIT License. See the LICENSE file for more information.
