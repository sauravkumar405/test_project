from csv import DictReader

file_handle = open("DataSet/data.csv", "r")
DataSet = DictReader(file_handle)

subset = []
unique = []
for entry in DataSet:
    if entry['Region'] not in unique:
        subset.append(entry)
        unique.append(entry['Region'])
subset = subset[::15]

file_handle.close()
