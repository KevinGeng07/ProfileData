import csv
from collections import defaultdict

def ProfileData(csv_read: str, csv_write: str) -> None:
    """
    Params:
        csv_read: str = None -> The .csv file to read data from.
        csv_write: str = None -> The .csv file to write data to.
        (Ensure both "csv_read" and "csv_write" are raw file strings.)

    Returns:
        None (String printed to declare process completion.)

    Read data from "csv_read", assuming the first row contains only
    labels and subsequent rows contain only data points. Compiles
    data based on datatype and writes it to file "csv_write". In
    "csv_write", the first row contains all labels and first column
    contains all data types."""

    with open(rf"{csv_read}", "r", newline="", encoding="utf-8") as read_csv:
        with open(rf"{csv_write}", "w", newline="", encoding="utf-8") as cur_csv:
            csv_writer = csv.writer(cur_csv, quoting=csv.QUOTE_ALL)
            csv_reader = list(csv.reader(read_csv, quoting=csv.QUOTE_ALL))


            fields = csv_reader[0]
            csv_writer.writerow(["Type"] + fields)

            fields_dict = {key: defaultdict(int) for key in fields}

            cols: set = set()

            for row in csv_reader[1:]:
                for index, item in enumerate(row):
                    try:
                        fields_dict[fields[index]][str(type(eval(item)))] += 1
                        cols.add(str(type(eval(item))))
                    except:  # For strings.
                        fields_dict[fields[index]]["<class 'str'>"] += 1
                        cols.add("<class 'str'>")

            for datatype in cols:

                csv_writer.writerow([datatype.split("'")[1]] + [fields_dict[field][datatype] for field in fields])
                cur_csv.flush()

            cur_csv.close()
            print(f"Data successfully processed from \'{csv_read}\' to \'{csv_write}\'.")
