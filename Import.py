import os
import csv
from Core.Stock import Stock
from Data.DataManager import DataManager

dm = DataManager()
data_manager = dm.get_instance()
source_dir = './Temp/Input/'
dest_dir = './Temp/Output/'
file_count = 0
file_list = os.listdir(source_dir)
for source_file in file_list:
    source_file_path = os.path.join(source_dir, source_file)
    dest_file_path = os.path.join(dest_dir, source_file)
    issuer_id = 17
    row_count = 0

    with open(source_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            if row_count == 0:
                #print("Column names are {}".format({", ".join(row)}))
                row_count += 1
            else:
                stock = Stock(0, issuer_id, row[0], row[1], row[2], row[4], row[5], row[6], row[7], row[8])
                id = data_manager.insert_stock(stock)
                row_count += 1
                if (row_count % 100) == 0:
                    print("\nProcessed: {} rows".format(row_count))

        print("\nProcessed: {} rows".format(row_count))

    if row_count > 0:
        os.rename(source_file_path, dest_file_path)
    file_count += 1

print("\nProcessed {} file(s)".format(file_count))
