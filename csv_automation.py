import csv

input_file = 'input.csv'
output_file = 'output.csv'

with open(input_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    data = []
    for row in reader:
        row['Score'] = str(int(row['Score']) + 10)
        data.append(row)

with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("Updated CSV saved as", output_file)