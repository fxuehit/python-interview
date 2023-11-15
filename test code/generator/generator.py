def csv_reader(file_name):
    file = open(file_name)
    print(type(file))
    result = file.read().split("\n")
    return result

def csv_reader2(file_name):
    for row in open(file_name, "r"):
        yield row

filename = r'./test code/generator/some_csv.txt'
csv_gen1 = (row for row in open(filename))
print(type(csv_gen1))
print(next(csv_gen1))
print(next(csv_gen1))
print(next(csv_gen1))

row_count = 0
csv_gen2 = csv_reader(filename)
for row in csv_gen2:
    row_count += 1
print(type(csv_gen2))
print(f"Row count is {row_count}")

csv_gen3 = csv_reader2(filename)
row_count = 0

for row in csv_gen3:
    row_count += 1
print(type(csv_gen3))
print(f"Row count is {row_count}")