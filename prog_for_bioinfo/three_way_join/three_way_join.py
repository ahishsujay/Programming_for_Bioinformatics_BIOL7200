#!/usr/bin/env python3
import sys

file_name1 = sys.argv[1]
file_name2 = sys.argv[2]
file_name3 = sys.argv[3]

# Write your code here.  Print your output to standard out.

first_dict = {}
second_dict = {}

gene_list_1 = []

with open(file_name1) as fh_1:
    for i in fh_1:
        list_1 = i.split("\t")
        key_1 = list_1[0]
        first_dict[key_1] = list_1[1]+"\t"+list_1[3]+"\t"+list_1[4] #UCSCid:chr+start+stop

with open(file_name2) as fh_2:
    for j in fh_2:
        list_2 = j.split("\t")
        key_2 = list_2[4]
        #print(key_2)
        if key_2 not in second_dict:
            second_dict[key_2] = list_2[0] #GeneName:UCSCid

with open(file_name3) as fh_3:
    for k in fh_3:
        if k.startswith("InfectiousDisease"): #In order to ignore the header in Infectious Disease file
            continue
        k = k.rstrip("\n") #Stripping newline
        gene_list_1.append(k) #Storing the genes in a list

print("Gene"+"\t"+"Chr"+"\t"+"Start"+"\t"+"Stop")
for x in sorted(gene_list_1):
    UCSC_ID = second_dict[x]
    final = first_dict[UCSC_ID]
    print(x+"\t"+final)
