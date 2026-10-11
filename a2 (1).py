"""
1) Add the file and topic details.
   a) Mention the file name as `02-phone-keypad.py`.
   b) Mention the topic as "Phone Keypad, Recursion Trees and How Problems Grow".
   c) Introduce the program as a way to count keypad letter combinations.

2) Create the keypad dictionary.
   a) Store digits from 2 to 9 as keys.
   b) Store the matching letters for each digit.
   c) Use the dictionary to find how many choices each digit has.

3) Create the recursive function.
   a) Define a function named `count_combos(digits)`.
   b) Use `digits` as the remaining keypad input.

4) Add the base case.
   a) Check if the digit string is empty.
   b) Return 1 because one complete combination path has been counted.
   c) Use this base case to stop recursion.

5) Add the recursive case.
   a) Look at the first digit using `digits[0]`.
   b) Count how many letters that digit has.
   c) Multiply it by `count_combos(digits[1:])`.
   d) Recursively count the combinations for the remaining digits.

6) Show fixed examples.
   a) Pause before showing the examples.
   b) Print `count_combos('2')`.
   c) Print `count_combos('23')`.

7) Ask for keypad digits.
   a) Ask the user to enter digits from 2 to 9.
   b) Suggest examples like 234 or 2345.
   c) Store the input in `d`.

8) Ask for a prediction and display the result.
   a) Ask the user to guess the number of combinations.
   b) Pause before showing the answer.
   c) Call `count_combos(d)` using the user's digits.
   d) Print the result and the user's original guess.
"""
#phone keypad
keys = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqr","8":"stu","9":"vwx"}
def count_combos(digits):
   if len(digits)==0:
      return 1
   return len(digits[0])*count_combos(digits[1:1])
input("count_combos Multiplying letter choices at each digits letter per step press enter")
print("count_combos('2')=",count_combos('2'))
print("count_combos('23')=",count_combos('23'))
n =(input("enter number like 2 to 9 like ex 234 to 2345"))
guess = input("enter your guess ")
print("count_combos("+(n)+")=",count_combos(n),"your guess is",guess)
