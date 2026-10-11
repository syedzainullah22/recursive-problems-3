"""
1) Add the file and topic details.
   a) Mention the file name as `01-tower-of-hanoi.py`.
   b) Mention the topic as "Tower of Hanoi, Solving Tower of Hanoi with Code".
   c) Introduce the program as a way to count the minimum moves needed to shift disks.

2) Create the recursive function.
   a) Define a function named `hanoi(n)`.
   b) Use `n` as the number of disks.

3) Add the base case.
   a) Check if `n` is equal to 0.
   b) Return 0 because zero disks need zero moves.
   c) Use this base case to stop recursion.

4) Add the recursive case.
   a) Return `2 * hanoi(n - 1) + 1`.
   b) Count moving the smaller stack once.
   c) Count moving the biggest disk once.
   d) Count moving the smaller stack again.

5) Show fixed examples.
   a) Pause before showing the examples.
   b) Print `hanoi(1)`.
   c) Print `hanoi(2)`.

6) Ask for the number of disks.
   a) Ask the user to enter a number of disks.
   b) Suggest example values like 3 or 4.
   c) Convert the input into an integer.

7) Ask for a prediction.
   a) Ask the user to guess the value of `hanoi(n)`.
   b) Store the user's guess.

8) Display the final result.
   a) Pause before showing the answer.
   b) Call `hanoi(n)` using the user's number.
   c) Print the minimum moves and the user's original guess.
"""
#tower of hanoi
def hanoi(n):
   if n == 0:
      return 0
   return 2* hanoi(n - 1) + 1
input("hanoi counts miunimun moves to shift n disk form pigied to peg c")
print("hanoi(1)=",hanoi(1))
print("hanoi(2)=",hanoi(2))
n = int(input("enter a number like 3 or 4"))
guess = input("Enture your guess for hanoi( "+str(n)+")?")
input("hanoi(n)=2* hanoi(n - 1)+1 move this stack twoice press enter")
print("hanoi(  "+str(n)+")",hanoi(n),"your guess is " ,guess)