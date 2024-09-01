import json
import csv

def read_spec_file(spec_file):
    """Read the JSON spec file and return field specifications and metadata."""
    try:
        with open(spec_file, 'r', encoding='utf-8') as f:
            spec_data = json.load(f)
        
        field_names = spec_data["ColumnNames"]
        widths = list(map(int, spec_data["Offsets"]))  # Convert widths to integers
        
        field_specs = list(zip(field_names, widths))
        return field_specs, spec_data
    except FileNotFoundError:
        print(f"Error: The file '{spec_file}' was not found.")
        raise
    except json.JSONDecodeError:
        print(f"Error: The file '{spec_file}' is not a valid JSON file.")
        raise

def generate_fixed_width_line(data, field_specs):
    """Generate a single line of fixed-width format according to the spec."""
    fixed_width_line = ""
    for field_value, (field_name, width) in zip(data, field_specs):
        # Ensure field value fits the width; pad with spaces if needed
        fixed_width_line += field_value.ljust(width)[:width]
    return fixed_width_line

def generate_fixed_width_file(spec_file, output_file, data_rows):
    """Generate a fixed-width file using the provided spec and data."""
    field_specs, spec_data = read_spec_file(spec_file)
    
    with open(output_file, 'w', encoding=spec_data["FixedWidthEncoding"]) as f:
        if spec_data.get("IncludeHeader") == "True":
            # Write header if required
            header_data = [name for name, _ in field_specs]
            header_line = generate_fixed_width_line(header_data, field_specs)
            f.write(header_line + '\n')
        
        # Write data rows in fixed-width format
        for data in data_rows:
            fixed_width_line = generate_fixed_width_line(data, field_specs)
            f.write(fixed_width_line + '\n')

def parse_fixed_width_line(line, field_specs):
    """Parse a single line of fixed-width format according to the spec."""
    parsed_data = []
    current_position = 0
    for field_name, width in field_specs:
        field_value = line[current_position:current_position + width].strip()
        parsed_data.append(field_value)
        current_position += width
    return parsed_data

def parse_fixed_width_file(input_file, output_file, spec_file):
    """Parse a fixed-width file and write the data to a delimited file (CSV)."""
    field_specs, spec_data = read_spec_file(spec_file)
    
    with open(input_file, 'r', encoding=spec_data["FixedWidthEncoding"]) as infile, \
         open(output_file, 'w', encoding=spec_data["DelimitedEncoding"], newline='') as outfile:
        writer = csv.writer(outfile)
        
        # Write header if required
        if spec_data.get("IncludeHeader") == "True":
            header = infile.readline().strip()
            field_specs = [(name, width) for name, width in zip(json.load(open(spec_file))["ColumnNames"], list(map(int, json.load(open(spec_file))["Offsets"])))]
        
        # Parse and write data rows
        for line in infile:
            parsed_data = parse_fixed_width_line(line.strip(), field_specs)
            writer.writerow(parsed_data)

# Example usage for generating and parsing files
spec_file = 'spec.json'
fixed_width_file = 'fixed_width_output.txt'
delimited_file = 'delimited_output.csv'

# Sample data matching the field names in spec file
data_rows = [
    ('John', 'Doe', '1234', 'AB', 'New York', 'NY', 'USA', '1234567890', 'john@example.com', '1990-01-01'),
    ('Jane', 'Smith', '5678', 'CD', 'Los Angeles', 'CA', 'USA', '9876543210', 'jane@example.com', '1985-05-15')
]

# Generate fixed-width file
generate_fixed_width_file(spec_file, fixed_width_file, data_rows)
print(f"Fixed-width file '{fixed_width_file}' generated successfully.")

# Parse fixed-width file to delimited file
parse_fixed_width_file(fixed_width_file, delimited_file, spec_file)
print(f"Delimited file '{delimited_file}' generated successfully.")


