# Use the official PostgreSQL base image.
FROM postgres:latest

# Set environment variables.
ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=database

# Copy initialization and seed scripts to the container.
COPY example_seed.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL port.
EXPOSE 5432
