"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    new_list=[]
    for item in list1:
        if item not in new_list:
            new_list.append(item)
    return new_list

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    new_list=[]
    for item in list1:
        if item in list2:
            new_list.append(item)
    
    return new_list                        

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """   
    new_list=[]
    for item in list1:
        new_list.append(item)
    for item in list2:
        new_list.append(item)
    
    
    for item in range(len(new_list)-1):
        for item in range(len(new_list)-1):
            if new_list[item]>new_list[item+1]:
                
                
                                       dummy_k=new_list[item+1]
                                       new_list[item+1]=new_list[item]
                                       new_list[item]=dummy_k
                                       
    return new_list    
       
          
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive. 
    """
    if len(list1)==0:
        return []
    if len(list1)==1:
        return list1
    else:
        if list1[0]>list1[1]: 
            dummy_k=list1[1]
            dummy_l=list1[0]
            
            new_list=[dummy_k,dummy_l]
            return remove_duplicates(merge(new_list,merge_sort(list1[1:])))
        else:
            dummy_k=list1[1]
            dummy_l=list1[0]
            new_list=[dummy_l,dummy_k]
            return remove_duplicates(merge(new_list,merge_sort(list1[1:])))
        
    

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word)==0:
        return [""]
   
    if len(word)==1:
        return [word,""]
    
    else:
        
        first=word[0]
    
        rest=word[1:]
        rest_strings=gen_all_strings(rest)
        dummy_l=[] 
        for item in rest_strings:
            for dummy_i in range(len(item)): 
                dummy_w=item[0:dummy_i]+first+item[dummy_i:]
                dummy_l.append(dummy_w) 
            dummy_l.append(item+first)    
        return dummy_l+rest_strings     

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url_file = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url_file)
    lines = netfile.readlines()



    clean_words = [line for line in lines] 

    return clean_words

      
    

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
#run()

    