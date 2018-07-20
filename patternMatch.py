# Program to return collection of space-separated integers
# specifying all starting positions where Pattern appears
# as a substring of Genome.

#!/usr/bin/python
import os
import operator
import sys
import shutil


# To take input from file
os.chdir("C:\\Users\mkumar\Downloads")
genome = open("dataset_3_5.txt","r")
genome = genome.read()
#genome = 'GATATATGCATATACTT'
pattern = (input("Enter pattern to be matched: "))
#pattern = 'ATAT'


# Function to find the pattern in the DNA sequence

def patternMatch(genome,pattern):
    startingPoints = []
    for i in range(len(genome) - len(pattern) + 1):
                    if genome[i:i+len(pattern)] == pattern:
                                startingPoints.append(i)
    return startingPoints

# Call the function that returns the count value
patternMatches = patternMatch(genome,pattern)

print(" ".join(str(x) for x in patternMatches))
