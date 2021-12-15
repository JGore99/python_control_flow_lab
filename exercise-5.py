# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

term = 0
number = 0
print(f"term: {term} / number: {number}")
term = 1
number = 1
print(f"term: {term} / number: {number}")
term = 2
number = 1
val1 = 1
val2 = 1
print(f"term: {term} / number: {number}")
for fib in range(48):
  term += 1
  number = val1 + val2
  val1 = val2
  val2 = number
  print(f"term: {term} / number: {number}")

