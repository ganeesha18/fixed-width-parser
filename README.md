# fixed-width-parser
This repository contains a Python script to parse fixed-width files and convert them to a delimited format (like CSV). The solution includes a Dockerfile for containerization, allowing easy setup and execution without worrying about dependencies.

## Overview

This project contains a Python application that parses fixed-width text files and converts them into a delimited file format such as CSV. It uses standard Python libraries to achieve this without relying on third-party packages like pandas. The code is Dockerized for easy deployment and usage.

## Features
- Fixed-width file parsing: Reads and processes fixed-width files based on a provided spec file.
- Custom delimiters: Converts data to delimited formats like CSV.
- Docker Support: Run the parser in a containerized environment without installing Python or other dependencies.
- Simple and Easy to Use: Minimal dependencies, straightforward setup.
  
## Getting Started
### Prerequisites
1.Git: Version control to clone the repository.
2.Python 3-slim: For local development and testing.
3.Docker: To build and run the Docker container.

### Installation
1. Clone the Repository:
    ```bash
    git clone https://github.com/ganeesha18/fixed-width-parser.git
    cd fixed-width-parser
2. Install Python Dependencies (if running locally)
    ```bash
    pip install -r requirements.txt

## Usage
1. Running Locally
You can run the script directly using Python.
    ```bash
    python fixed_width_parser.py
2. Running with Docker
    ```bash
    docker build -t fixed-width-parser

## Example
Generate a fixed-width file with a specific format based on the spec.json, then the parser will generate a CSV file:
### Sample Data Rows
Below are example data rows formatted as tuples. Each tuple represents a row of data to be written to a fixed-width file:

```python
  data_rows = [
    ('John', 'Doe', '1234', 'AB', 'New York', 'NY', 'USA', '1234567890', 'john@example.com', '1990-01-01'),
    ('Jane', 'Smith', '5678', 'CD', 'Los Angeles', 'CA', 'USA', '9876543210', 'jane@example.com', '1985-05-15')
]
```

### Fixed-Width File Specification
The file specification is defined in `spec.json`, which outlines the column names and their respective offsets. The offsets represent the length of each field in the fixed-width file.
#### `spec.json` Example
```json
{
    "ColumnNames": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "f9",
        "f10"
    ],
    "Offsets": [
        "5",
        "12",
        "3",
        "2",
        "13",
        "7",
        "10",
        "13",
        "20",
        "13"
    ]
}
```
### Sample Output CSV
The fixed-width file is parsed into a CSV format as shown below:

```csv
FirstName,LastName,ID,Code,City,State,Country,PhoneNumber,Email,DateOfBirth
John,Doe,1234,AB,New York,NY,USA,1234567890,john@example.com,1990-01-01
Jane,Smith,5678,CD,Los Angeles,CA,USA,9876543210,jane@example.com,1985-05-15
```

## Development
### Edit Code Locally
Modify the source code in your preferred IDE or text editor.

### Rebuild Docker Image (if needed)
After making changes, rebuild the Docker image to include the updated code.

