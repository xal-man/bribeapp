import csv

WP_EARNING = []
TAX_25 = []
EVASION = []
TAX_PAYED = []
BRIBE = []

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            WP_EARNING.append(row[1])
            TAX_25.append(row[2])
            EVASION.append(row[3])
            TAX_PAYED.append(row[4])
            BRIBE.append(row[5])
            line_count += 1
    print(f'Processed {line_count} lines.')