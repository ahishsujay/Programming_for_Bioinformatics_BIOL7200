#!/usr/bin/env python3

import sys
k = sys.argv[1]
k = int(k)
fasta_file = sys.argv[2]

new = ""                                    #Storing the complete DNA in string named "new"
dna = []
kmer_counts = {}

with open(fasta_file) as fh:
    header = fh.readline()                  #Storing the header file in variable "header"
    line = fh.readlines()                   #Reading the rest of the file and storing in "line"
    fh.close()

for x in line:                              #As .readlines() stores everything as a list in the variable "line", I am coverting the elements of the list into a complete string by using a for loop and concatenating to "new"
    new += x
new = new.replace("\n","")                  #Removing the \n in "new" by using replace. rstrip didn't work for some reason

for i in range(len(new) - k + 1):           #For loop to take all the possible kmers, and storing them in a list "dna"
    dna.append(new[i:i+k])

for j in dna:                               #For loop to count occurence of each of the kmers and storing them in a dict "kmer_counts"
    kmer_counts[j] = kmer_counts.get(j,0) + 1

for key in sorted(kmer_counts.keys()):      #Printing the kmer and kmer counts in std output
    print(key+"\t"+str(kmer_counts[key]))
