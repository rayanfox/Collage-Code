#10-7

#Write a program that inputs a text file. The program should print the unique words in the file in alphabetical order.

with open('file.txt', 'r') as file:
   
    words = file.read().split()

   
    unique_words = set(words)

    sorted_words = sorted(unique_words)

    for word in sorted_words:
        print(word)