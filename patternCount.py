# Program to return the number of occurrences
# of a pattern on length 'n' (pattern) in a DNA string (text).

#!/usr/bin/python
import os
import operator
import sys
import shutil


# To take input from file
os.chdir("C:\\Users\mkumar\Downloads")
text = open("dataset_2_7.txt","r")
text = text.read()
#dna_substring = (input("Enter character pair to be counted: "))
pattern = 'GGTTATAGG'
length = 7

# Function to find the pattern in the DNA sequence

def patternCount(text,pattern):
    count = 0
    print(text)
    while (len(text)>0):
       # Get the position of the pair in the sequence
       start = text.find(pattern)
       if(start >= 0):
           #print (sequence)
           count = count +1
       text = text[start+length:]
    return(count)

# Call the function that returns the count value
pattern_count = patternCount(text,pattern)
if pattern_count > 0:
   print ("The pattern occurs", pattern_count, "times")
elif pattern_count == 0:
   print ("The pattern could not be found") 
