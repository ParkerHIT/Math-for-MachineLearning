#!/usr/bin/python
import os
import operator
import sys
import shutil

os.chdir("C:\\Users\mkumar\Downloads")
text = open("dataset_2_7.txt","r")
text = text.read()

def reverse_comp(text):
	rev_comp = ''
	for nucleotide in text:
		if nucleotide == 'A':
			rev_comp = rev_comp + 'T'
		elif nucleotide == 'T':
			rev_comp = rev_comp + 'A'
		elif nucleotide == 'G':
			rev_comp = rev_comp + 'C'
		elif nucleotide == 'C':
			rev_comp = rev_comp + 'G'
	rev_comp = rev_comp[::-1]
	return rev_comp
	

reverseCompliment = reverse_comp(text)

print(reverseCompliment)
