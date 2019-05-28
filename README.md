# BLAST-Tools
Python scripts to assist in the filtering and analysis of BLAST results, including sequence retrieval 

NOTE: These scripts make use of BioPython as a dependency. Installation instructions can be found here:

http://biopython.org/DIST/docs/install/Installation.html

Additionally, these scripts use outformat 6 BLAST output files. For more information on this format, see here:

http://www.metagenomics.wiki/tools/blast/blastn-output-format-6

=====COMPONENTS=====

seqfetch.py:
Retreive sequences from your FASTA file given your BLAST output

ortholog-table.py:
Create ortholog table from pBLAST results from multiple species, including percent IDs. Example use included. 

blast_diff.pyt:
Find sequence hits in one BLAST output that are unique, and do not appear in another BLAST output
