from Bio import SeqIO

blast = open("input_blast.txt",'r')
queries = []
for line in blast:
    line = line.strip("\n")
    row = line.split("\t")  # creates a list of column names, each value separated via tab
    query = row.pop(0)
    queries.append(query)
#Optional: Filter which queries to retreive based on match
    #match = row.pop(0)
    #if match == "MATCH ID":
    #    print query
    #    queries.append(query)

shared = open("output.fasta",'a')
for record in SeqIO.parse("input_fasta.fa", "fasta"):
    for query in queries:
        if query in record.id:
            SeqIO.write(record, shared, "fasta")
