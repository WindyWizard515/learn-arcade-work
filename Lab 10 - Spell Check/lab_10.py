## Import the library "os" so that you can clear the bash console
import os
import re

## Clear the bash console by using the command os.system("clear")
os.system("clear")

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def main():
    
    alice_in_wonderland_text =  open("/home/paul/learn-arcade-work/Lab 10 - Spell Check/AliceInWonderLand200.txt")
    
    dictionary = open("/home/paul/learn-arcade-work/Lab 10 - Spell Check/dictionary.txt")
    
    dictionary_list = []
    
    for line in dictionary:
        line = line.strip()
        
        dictionary_list.append(line)
    
    print("--- Linear Search ---")
    
    current_list_position = 0
    line_number = 0
    
    for line in alice_in_wonderland_text:
        word_list = split_line(line)
        line_number += 1
        for word in word_list:
            
            while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != word.upper():
                current_list_position += 1
                
            if current_list_position >= len(dictionary_list):
                print(f"Line {line_number}: possible misspelled word: {word}")
                
            current_list_position = 0
            
    alice_in_wonderland_text.close()
            
        
    dictionary.close()
            
    print("--- Binary Search ---")
    
    alice_in_wonderland_text =  open("/home/paul/learn-arcade-work/Lab 10 - Spell Check/AliceInWonderLand200.txt")
    
    line_number = 0
    
    for line in alice_in_wonderland_text:
        line_number += 1
        if line != "/n":
            word_list = split_line(line)
        for word in word_list:
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False
            
            while not found:

                # Find the middle position
                middle_pos = (lower_bound + upper_bound) // 2
                
                if upper_bound == lower_bound and lower_bound == middle_pos and dictionary_list[middle_pos] != word.upper():
                    break
                elif upper_bound < lower_bound:
                    break
                elif dictionary_list[middle_pos] == word.upper():
                    found = True
                elif dictionary_list[middle_pos] < word.upper(): 
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > word.upper():
                    upper_bound = middle_pos - 1
                                   
            if not found:
                print(f"Line {line_number}: possible misspelled word: {word}")
                
            
    alice_in_wonderland_text.close()
                
main()