import pandas 

def xlsx_to_csv(input_file, output_file):
    # Read the Excel file into a pandas DataFrame
    df = pandas.read_excel(input_file)

    # Write the DataFrame to a CSV file
    df.to_csv(output_file, index=False)

def main():
    # Input XLSX file path
    input_file = "C:\images\sample.xlsx"
    # Output CSV file path
    output_file = "C:\images\sample1.csv"  # Specify the full path where you want to save the CSV file

    # Convert XLSX to CSV
    xlsx_to_csv(input_file, output_file)

    print(f"Conversion from XLSX to CSV complete. Output file: {output_file}")

if __name__ == "__main__":
    main()
