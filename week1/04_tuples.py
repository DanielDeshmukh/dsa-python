"""
=============================================
DAY 4: TUPLES — Immutable, Hashable
=============================================

Run this file: python week1/04_tuples.py
"""

# ============================================
# VISUAL: What is a Tuple?
# ============================================
#
# A tuple is like a list, but IMMUTABLE (can't change it).
#
#   Index:    0     1     2
#           +-----+-----+-----+
#   Tuple:  | 10  | 20  | 30  |
#           +-----+-----+-----+
#
# - Same indexing/slicing as lists
# - Can't add, remove, or modify elements
# - HASHABLE — can be used as dict keys or set elements!
# - Lists are NOT hashable (can't be dict keys)
#


# ============================================
# CREATING TUPLES
# ============================================

# Empty tuple
empty = ()
print(f"Empty tuple: {empty}")

# Tuple with values
point = (3, 4)
print(f"Point: {point}")

# Single element tuple (NEED the comma!)
not_a_tuple = (42)      # This is just an int
is_a_tuple = (42,)      # This is a tuple
print(f"Not a tuple: {type(not_a_tuple)}")
print(f"Is a tuple: {type(is_a_tuple)}")

# Tuple unpacking (SUPER USEFUL)
x, y = (10, 20)
print(f"x={x}, y={y}")

# Swap variables (Pythonic!)
a, b = 1, 2
a, b = b, a
print(f"Swapped: a={a}, b={b}")


# ============================================
# WHY TUPLES MATTER
# ============================================

print(f"\n--- WHY TUPLES ---")

# 1. Tuples can be dict keys (lists can't!)
location = {(40.7128, -74.0060): "New York", (51.5074, -0.1278): "London"}
print(f"Location: {location}")

# 2. Tuples can be set elements
unique_points = {(1, 2), (3, 4), (1, 2)}  # Duplicates removed
print(f"Unique points: {unique_points}")

# 3. Returning multiple values from a function
def get_min_max(lst):
    return min(lst), max(lst)

mn, mx = get_min_max([3, 1, 4, 1, 5, 9])
print(f"Min: {mn}, Max: {mx}")

# 4. Named tuples (like a lightweight class)
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"Named tuple: x={p.x}, y={p.y}")


# ============================================
# TUPLE OPERATIONS
# ============================================

print(f"\n--- OPERATIONS ---")

t = (1, 2, 3, 4, 5)

# Indexing (same as lists)
print(f"First: {t[0]}")
print(f"Last: {t[-1]}")

# Slicing (same as lists)
print(f"Slice [1:4]: {t[1:4]}")

# Concatenation
t2 = (6, 7)
print(f"Concat: {t + t2}")

# Repetition
print(f"Repeat: {t * 2}")

# Length
print(f"Length: {len(t)}")

# Count
print(f"Count of 1: {t.count(1)}")

# Index
print(f"Index of 3: {t.index(3)}")

# Membership
print(f"3 in t: {3 in t}")


# ============================================
# TUPLES vs LISTS — When to use which?
# ============================================
#
#   Use TUPLE when:                  Use LIST when:
#   - Data shouldn't change          - Data will change
#   - Need dict key / set element    - Need to add/remove
#   - Returning multiple values      - Ordered collection
#   - Fixed structure (x,y coords)   - Dynamic size
#


# ============================================
# PRACTICE PROBLEMS
# ============================================

print("\n" + "=" * 50)
print("PRACTICE TIME!")
print("=" * 50)

# Problem 1: Return (min, max) of a list without using min/max
def min_max(lst):
    """YOUR CODE HERE"""
    pass

# Problem 2: Check if a point is inside a rectangle
# Rectangle is (x1, y1, x2, y2) — top-left and bottom-right
def is_inside(point, rectangle):
    """YOUR CODE HERE"""
    pass

# Problem 3: Group words by their sorted letters (anagram grouping)
def group_anagrams(words):
    """YOUR CODE HERE"""
    pass


# ============================================
# SOLUTIONS
# ============================================

print("\n--- SOLUTIONS ---")

def min_max_solution(lst):
    mn = lst[0]
    mx = lst[0]
    for num in lst[1:]:
        if num < mn:
            mn = num
        if num > mx:
            mx = num
    return mn, mx

print(f"min_max([3,1,4,1,5,9]) = {min_max_solution([3, 1, 4, 1, 5, 9])}")

def is_inside_solution(point, rectangle):
    x, y = point
    x1, y1, x2, y2 = rectangle
    return x1 <= x <= x2 and y1 <= y <= y2

print(f"is_inside((3,4), (0,0,5,5)) = {is_inside_solution((3, 4), (0, 0, 5, 5))}")  # True
print(f"is_inside((6,7), (0,0,5,5)) = {is_inside_solution((6, 7), (0, 0, 5, 5))}")  # False

def group_anagrams_solution(words):
    from collections import defaultdict
    groups = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        groups[key].append(word)
    return dict(groups)

print(f"group_anagrams(['eat','tea','tan','ate','nat','bat']) = {group_anagrams_solution(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])}")


# ============================================
# TEST RUNNER
# ============================================

def run_tests():
    passed = 0
    failed = 0

    tests = [
        (min_max_solution([3, 1, 4, 1, 5, 9]), (1, 9)),
        (is_inside_solution((3, 4), (0, 0, 5, 5)), True),
        (is_inside_solution((6, 7), (0, 0, 5, 5)), False),
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
