  Python 3.10+ function to read data from .csv file "csv_read". Compiles data based on datatype and writes it to file .csv file "csv_write". 
  In the compiled file, the first row contains all labels and first column contains all data types. Useful for data cleaning, 
  data profiling, or data visualization tasks.

Params:
        csv_read: str = None -> The .csv file to read data from.
        csv_write: str = None -> The .csv file to write data to.
        (Ensure both "csv_read" and "csv_write" are raw file strings.)

Returns:
    None (String printed to declare process completion.)
