#Mair M L
#Create an ortholog table based on BLAST results from multiple species
#USES PROTEIN BLAST OUTPUTS!
#Only takes the top hit.
#In this example, and ortholog table is made for 
#Aedes aegypti genes appearing in Anopheles darlingi and Drosophila melanogaster
#For custom use, change file names. 

dictionary = {}#dictionary of ortholog values/Percent IDs per gene
aedesdar = open("darlingi_aegypti.txt","r") #BLAST file for one species A-species B
aedesfly= open("aegypti_fly.txt",'r') #BLAST file for speciesA-species C
for line in aedesdar: #first BLAST file
    line = line.split("\t")
    #Get genes
    aeGene = line[1]
    daGene = line[0]
    #Get percent ID
    adPID = line[2]
    if aeGene not in dictionary.keys(): #avoid duplicates
        dictionary[aeGene]=[[daGene, adPID],["-","-"]]

for line in aedesfly: #second BLAST file
    line = line.split("\t")
    aeGene = line[0]
    flyGene = line[1]
    afPID = line[2]
    if aeGene not in dictionary.keys(): #if no ortholog for sppA-sppB, record sppA-sppC
        dictionary[aeGene]=[["-","-"],[flyGene, afPID]]
    else: #if sppA-sppB exists, add sppA-sppC
        val = dictionary[aeGene]
        if "['-', '-']" in str(val):
            val.pop(1)
            val.append([flyGene, afPID])
            dictionary[aeGene]=val

out = open("aedes_ortho.txt",'w') #ortholog file

out.write("Aegypti"+"\t"+"Darlingi"+"\t"+"PID"+"\t"+"Melanogaster"+"\t"+"PID"+"\n")
out.close() #create file/get the header in place before adding everything

out = open("aedes_ortho.txt",'a') #ortholog file 

for gene,items in dictionary.items():
    string = gene
    for i in items: 
        for x in i:
            string =string + "\t" +x + "\t" #format the ortholog printout
    string = string +"\n" #new line character for file format
    out.write(string)
