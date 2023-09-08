#!/usr/bin/env python

# system include files
#
import sys
import os
import numpy as np
import random
import math
import string

# read file that contain *.txt
#
def file_list(argv):
    # get the list of file in the directory
    #
    dir_list = os.listdir(argv[1])

    # create a list to hold txt file
    #
    txt_list = []
    # check to see if the file is empty and have the file "*.txt"
    #
    for i in dir_list:
        # check to see if ".txt" is in the name
        #
        if ".txt" in i:
            txt_list.append(i)
    file_freq(argv,txt_list)

# end of function

# remove punctuation from the list 
#
def punctuation(my_list):

    # create a new list
    #
    new_list =[]

    # for loop that go word by word in the list
    #
    for word in my_list:

        # loop trhought character in the word 
        #
        for character in word:

            # check the character in the word
            #
            if character in string.punctuation:
                word = word.replace(character,"")

        # add to new list
        #   
        new_list.append(word)
    return(new_list)
# get the freq of word from the text file
#
def file_freq(argv, txt_file):

    # list to hold words and words freq
    #
    words = []
    words_freq = []
    # create a path to the file to read it
    #
    cur_path = os.path.dirname(__file__)

    # got through the list of file names and open them
    #
    for i in txt_file:

        # change the path
        #
        new_path = os.path.relpath(argv[1] + i, cur_path)

        # on the file and read the text
        #
        with open(new_path, 'r') as f:

            # loop through the text
            #
            for line in f:

                # loop through  the line
                #
                for string in line.split():
                    words.append(string.lower())

    # past list too remove punctuation
    #
    new_words = punctuation(words)

    # for loop for word count
    #
    for i in new_words:
        words_freq.append(new_words.count(i))

    # add freq with the words
    #
    words_count_list = list(zip(words_freq, new_words))
    sort_list(words_count_list)
    
# end of function

# sort list
#
def sort_list(final_list):
    list_sort = []

    # for loop that find unique value
    #
    for x in final_list:
        if x not in list_sort:
            list_sort.append(x)
        
    # sort the list by the first value of the tuple and reverse the order
    #
    list_sort.sort(key = lambda a: a[0], reverse = True)
    print(list_sort)

# end of function

# main: this is the main function of this Python
#
# int main(int argc, char** argv)
#
def main(argv):

    # pass argv to directory
    #
    file_list(argv)

#
#
# end of main

# begin gracefully
#
if __name__ == "__main__":
    main(sys.argv)

#
# end of file
