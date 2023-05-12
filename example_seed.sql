-- Create a new table for companies
CREATE TABLE companies (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  location VARCHAR(100) NOT NULL
);

-- Create a new table for hourly rates
CREATE TABLE hourly_rates (
  id SERIAL PRIMARY KEY,
  rate DECIMAL(10, 2) NOT NULL,
  company_id INT NOT NULL,
  FOREIGN KEY (company_id) REFERENCES companies (id)
);

-- Create a new table for users
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  company_id INT NOT NULL,
  FOREIGN KEY (company_id) REFERENCES companies (id)
);

-- Insert some initial data into companies
INSERT INTO companies (name, location) VALUES
  ('Company A', 'Location A'),
  ('Company B', 'Location B'),
  ('Company C', 'Location C');

-- Insert some initial data into hourly_rates
INSERT INTO hourly_rates (rate, company_id) VALUES
  (10.50, 1),
  (12.75, 2),
  (15.00, 3);

-- Insert some initial data into users
INSERT INTO users (name, email, company_id) VALUES
  ('John Doe', 'johndoe@example.com', 1),
  ('Jane Smith', 'janesmith@example.com', 2),
  ('Michael Johnson', 'michaeljohnson@example.com', 3);
