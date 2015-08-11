#!/usr/bin/env python
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the 
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body
def big_words():
	fin = open('words.txt')
	line = fin.readline()
	for line in fin:
		word = line.strip()
		if len(word) > 20:
	 		print word 


##############################################################################
def main():
    big_words()

if __name__ == '__main__':
    main()
