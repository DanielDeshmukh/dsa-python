"""
=============================================
DAY 5: COMPREHENSIONS — Python's Superpower
=============================================

Run this file: python week1/05_comprehensions.py
"""

# ============================================
# VISUAL: What is a Comprehension?
# ============================================
#
# A comprehension is a one-liner to create lists/dicts/sets.
# Instead of this:
#
#   result = []
#   for x in range(5):
#       result.append(x * 2)
#
# You write this:
#
#   result = [x * 2 for x in range(5)]
#
# Same thing, one line. Faster to write, faster to read.
#
#   FOR LOOP:                    COMPREHENSION:
#   +-----------+                +---------------------------+
#   | result=[] |                | [x*2 for x in range(5)]  |
#   | for x...  |                +---------------------------+
#   |   append  |                Done. One line.
#   +-----------+
#


# ============================================
# LIST COMPREHENSIONS
# ============================================

print("--- LIST COMPREHENSIONS ---")

# Basic: [expression for item in iterable]
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# With condition: [expression for item in iterable if condition]
evens = [x for x in range(20) if x % 2 == 0]
print(f"Evens: {evens}")

# With if-else: [expr_if_true if condition else expr_if_false for item in iterable]
labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
print(f"Labels: {labels}")

# Nested loops: [expr for outer in iterable for inner in outer]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(f"Flattened: {flat}")

# String manipulation
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"Upper: {upper_words}")


# ============================================
# DICT COMPREHENSIONS
# ============================================

print(f"\n--- DICT COMPREHENSIONS ---")

# Basic: {key: value for item in iterable}
names = ["alice", "bob", "charlie"]
name_lengths = {name: len(name) for name in names}
print(f"Name lengths: {name_lengths}")

# With condition
scores = {"Alice": 95, "Bob": 67, "Charlie": 88, "Diana": 92}
passing = {name: score for name, score in scores.items() if score >= 80}
print(f"Passing: {passing}")

# Invert dict
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(f"Inverted: {inverted}")

# From two lists
keys = ["name", "age", "city"]
values = ["Daniel", 25, "Mumbai"]
combined = {k: v for k, v in zip(keys, values)}
print(f"Combined: {combined}")


# ============================================
# SET COMPREHENSIONS
# ============================================

print(f"\n--- SET COMPREHENSIONS ---")

# Basic: {expression for item in iterable}
unique_lengths = {len(word) for word in ["hello", "world", "hi", "python"]}
print(f"Unique lengths: {unique_lengths}")

# From string
chars = {c for c in "mississippi"}
print(f"Unique chars in 'mississippi': {chars}")


# ============================================
# GENERATOR EXPRESSIONS (lazy evaluation)
# ============================================

print(f"\n--- GENERATOR EXPRESSIONS ---")

# Parentheses instead of brackets = generator (lazy)
# Doesn't create the whole list in memory — generates on demand
gen = (x**2 for x in range(10))
print(f"Generator: {gen}")
print(f"First: {next(gen)}")
print(f"Second: {next(gen)}")

# Useful for sum/min/max on large data
total = sum(x**2 for x in range(1000000))
print(f"Sum of squares (1M): {total}")


# ============================================
# COMPREHENSIONS vs LOOPS
# ============================================
#
#   WHEN TO USE COMPREHENSION:        WHEN TO USE LOOP:
#   - Simple transformation            - Complex logic
#   - Filter with one condition        - Multiple conditions
#   - One-liner is readable            - Need to handle errors
#   - Creating new list/dict/set       - Side effects (print, write)
#
# RULE: If comprehension is > 1 line, use a loop instead.
#


# ============================================
# PRACTICE PROBLEMS
# ============================================

print("\n" + "=" * 50)
print("PRACTICE TIME!")
print("=" * 50)

# Problem 1: Get all prime numbers from 1 to 100 using comprehension
def primes_up_to_100():
    """YOUR CODE HERE"""
    pass

# Problem 2: Create a dict mapping numbers to "even"/"odd"
def even_odd_dict(n):
    """YOUR CODE HERE"""
    pass

# Problem 3: Flatten a 2D matrix and keep only positive numbers
def flatten_positives(matrix):
    """YOUR CODE HERE"""
    pass


# ============================================
# SOLUTIONS
# ============================================

print("\n--- SOLUTIONS ---")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_up_to_100_solution():
    return [x for x in range(2, 101) if is_prime(x)]

print(f"Primes (1-100): {primes_up_to_100_solution()}")

def even_odd_dict_solution(n):
    return {i: "even" if i % 2 == 0 else "odd" for i in range(1, n + 1)}

print(f"Even/Odd (1-5): {even_odd_dict_solution(5)}")

def flatten_positives_solution(matrix):
    return [num for row in matrix for num in row if num > 0]

print(f"Flatten positives: {flatten_positives_solution([[-1, 2, -3], [4, -5, 6]])}")


# ============================================
# TEST RUNNER
# ============================================

def run_tests():
    passed = 0
    failed = 0

    tests = [
        (len(primes_up_to_100_solution()), 25),
        (even_odd_dict_solution(3), {1: "odd", 2: "even", 3: "odd"}),
        (flatten_positives_solution([[-1, 2, -3], [4, -5, 6]]), [2, 4, 6]),
    ]

    for result, expected in tests:
        if result == expected:
            print(f"PASS: {result}")
            passed += 1
        else:
            print(f"FAIL: got {result}, expected {expected}")
            failed += 1

    print(f"\nResults: {passed} passed, {failed} failed")

if __name__ == "__main__":
    run_tests()
