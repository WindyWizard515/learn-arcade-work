## Import the library "os" so that you can clear the bash console
import os
import re

## Clear the bash console by using the command os.system("clear")
os.system("clear")

# def split_line(line):
#     return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

# def main():
    
#     alice_in_wonderland_text =  open("/home/paul/learn-arcade-work/Lab 10 - Spell Check/AliceInWonderLand200.txt")
    
#     dictionary = open("/home/paul/learn-arcade-work/Lab 10 - Spell Check/dictionary.txt")
    
#     dictionary_list = []
    
#     for line in dictionary:
#         line = line.strip()
        
#         dictionary_list.append(line)
        
#     dictionary.close()
    
#     print("--- Linear Search ---")
    
#     current_list_position = 1
#     line_number = 0
    
#     for line in alice_in_wonderland_text:
#         word_list = split_line(line)
#         line_number += 1
#         for word in word_list:
#             while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != word.upper():
#                 current_list_position += 1
                
#             if current_list_position < len(dictionary_list):
#                 print(f"Line {line_number}: possible misspelled word: {word}")
                
#             current_list_position = 0
            
#     alice_in_wonderland_text.close()
#                 ## Import the library "os" so that you can clear the bash console
# import os
# import re

# ## Clear the bash console by using the command os.system("clear")
# os.system("clear")

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def main():
    
    alice_in_wonderland_text =  open("/home/paul/learn-arcade-work/Lab 10 - Spell Check/AliceInWonderLand200.txt")
    
    dictionary = open("/home/paul/learn-arcade-work/Lab 10 - Spell Check/dictionary.txt")
    
    dictionary_list = []
    
    for line in dictionary:
        line = line.strip()
        
        dictionary_list.append(line)
        
    dictionary.close()
    
    print("--- Linear Search ---")
    
    current_list_position = 1
    line_number = 0
    
    for line in alice_in_wonderland_text:
        word_list = split_line(line)
        line_number += 1
        for word in word_list:
            while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != word.upper():
                current_list_position += 1
                
            if current_list_position < len(dictionary_list):
                print(f"Line {line_number}: possible misspelled word: {word}")
                
            current_list_position = 0
            
    alice_in_wonderland_text.close()
                
main()