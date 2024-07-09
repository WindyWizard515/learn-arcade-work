import os

# Clear the terminal before you print anything
os.system("clear")

# Create the variable that counts how many times it took and what line the villain is on
villian_number = 1

# Open the super_villains.txt file so we can look through it using a for loop
file = open("/home/paul/learn-arcade-work/Testing/super_villains.txt")

# Use a for loop to loop through the super_villains.txt file
for line in file:
    if line.strip() == "Hagar Bloodcrow":
        print("\n                            I found Him!")
        print(f"                          He is on line {villian_number}\n")
        pass
    else:
        villian_number += 1
        
file.close()