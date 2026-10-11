"""
1) Add the file and topic details.
   a) Mention the file name as `03-recursion-tree.py`.
   b) Mention the topic as "Recursion Trees and How Problems Grow".
   c) Introduce the program as a way to count paths through a grid.

2) Create the recursive function.
   a) Define a function named `paths(m, n)`.
   b) Use `m` for rows.
   c) Use `n` for columns.

3) Add the base case.
   a) Check if `m` is equal to 1 or `n` is equal to 1.
   b) Return 1 because there is only one path along a single row or column.
   c) Use this base case to stop recursion.

4) Add the recursive case.
   a) Call `paths(m - 1, n)` to count paths after moving down.
   b) Call `paths(m, n - 1)` to count paths after moving right.
   c) Add both results because both moves are possible.

5) Show fixed examples.
   a) Pause before showing the examples.
   b) Print `paths(3, 3)`.
   c) Print `paths(4, 4)`.

6) Ask for the grid size.
   a) Ask the user to enter one number for both rows and columns.
   b) Suggest example values like 5 or 6.
   c) Convert the input into an integer.

7) Ask for a prediction.
   a) Ask the user to guess the value of `paths(n, n)`.
   b) Store the user's guess.

8) Display the final result.
   a) Pause before showing the answer.
   b) Call `paths(n, n)` using the user's grid size.
   c) Print the total paths and the user's original guess.
   d) Highlight that each call can branch into two smaller calls.
"""