import csv

def column_to_array(csv_file, column_index):
   
    with open(csv_file, 'r') as file:
        
        reader = csv.reader(file)

       
        next(reader)

        
        column_data = []

       
        for row in reader:
            try:
                
                column_data.append(row[column_index])
            except IndexError:
              
                pass

    return column_data

def main():
    # Input CSV file path
    csv_file = "C:/images/sample1.csv"
   
    column_index = 2  

   
    array_data = column_to_array(csv_file, column_index)

    
    print("Array data:")
    print(array_data)

if __name__ == "__main__":
    main()
