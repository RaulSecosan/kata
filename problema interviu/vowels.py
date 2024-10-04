'''
Your task here is even more special than before: you must redesign the (ugly) vowel eater from the previous lab (3.1.2.10) and create a better, upgraded (pretty) vowel eater! Write a program that uses:

a for loop;
the concept of conditional execution (if-elif-else)
the continue statement.
Your program must:

ask the user to enter a word;
use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about the so-called string methods and the upper() method very soon - don't worry;
use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.
Look at the code in the editor. We've created word_without_vowels and assigned an empty string to it. Use concatenation operation to ask Python to combine selected letters into a longer string during subsequent loop turns, and assign it to the word_without_vowels variable.

Test your program with the data we've provided for you.
Sample input: Gregory

Expected output:

GRGRY
Sample input: abstemious

Expected output:

BSTMS

'''

# Solicită utilizatorului să introducă un cuvânt
user_word = input("Enter a word: ")

# Convertim cuvântul la majuscule
user_word = user_word.upper()

# Inițializăm variabila pentru cuvântul fără vocale
word_without_vowels = ""

# Iterăm prin fiecare literă din cuvânt
for letter in user_word:
    if letter in 'AEIOU':  # Verificăm dacă litera este o vocală
        continue  # Dacă este vocală, trecem peste această iterație
    word_without_vowels += letter  # Adăugăm litera dacă nu este vocală

# Afișăm cuvântul rezultat fără vocale
print(word_without_vowels)