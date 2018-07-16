# Program to return the most frequent pattern
# of a pattern on length 'k'  in a DNA string (text)


#!/usr/bin/python
import os
import operator
import sys
import shutil

os.chdir("C:\\Users\mkumar\Downloads")
text = open("dataset_2_7.txt","r")
text = text.read()

k = 12

def count(text,pattern):
	count = 0
	for i in range(len(text) - len(pattern) + 1):
		if text[i:i+len(pattern)] == pattern:
			count += 1
	return count

def frequentwords(text , k):
	freq_patterns = []
	counts = []
	for i in range(len(text) - k + 1):
		pattern = text[i:i+k]
		num = count(text,pattern)
		counts.append(num)
	maxcount = max(counts)
	for i in range(len(text) - k + 1):
		if counts[i] == maxcount:
			freq_patterns.append(text[i:i+k])
	freq_patterns = set(freq_patterns)
	return list(freq_patterns)

outputPatterns = frequentwords(text,k)

print(" ".join(str(x) for x in list(outputPatterns)))
