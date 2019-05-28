#M.L. Mair
#Finds hit IDs in file1 that are not found in file2
#try also:
#grep -v -f file2 file1 > out
file2 = open("file2.txt",'r')
ids = []
for line in file2:
    line = line.strip()
    line = line.split()
    id = line[0]
    if id not in ids:
        ids.append(id)
print(ids)
file1 = open("file1.txt",'r')
out = open("out.txt", 'w')

for line in file1:
    list = line.split()
    id = list[0]
    if id not in ids:
        print(line)
        out.write(line)
