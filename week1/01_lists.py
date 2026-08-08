"""
=============================================
DAY 1: LISTS — Your Bread and Butter
=============================================

Run this file: python week1/01_lists.py
"""

# ============================================
# VISUAL: What is a List?
# ============================================
#
# A list is an ordered collection of items.
# Think of it as a row of boxes, each holding a value.
#
#   Index:    0     1     2     3     4
#           +-----+-----+-----+-----+-----+
#   List:   | 10  | 20  | 30  | 40  | 50  |
#           +-----+-----+-----+-----+-----+
#
# - Indexing starts at 0 (not 1!)
# - Lists can hold ANY type (int, string, even other lists)
# - Lists are MUTABLE — you can change them after creation
#


# ============================================
# CREATING LISTS
# ============================================

# Empty list
empty = []
print(f"Empty list: {empty}")

# List with values
numbers = [10, 20, 30, 40, 50]
print(f"Numbers: {numbers}")

# Mixed types (valid but rarely done in DSA)
mixed = [1, "hello", 3.14, True]
print(f"Mixed: {mixed}")

# Using list() constructor
from_string = list("hello")
print(f"list('hello'): {from_string}")  # ['h', 'e', 'l', 'l', 'o']


# ============================================
# INDEXING — Accessing Elements
# ============================================
#
#   Index:    0     1     2     3     4
#           +-----+-----+-----+-----+-----+
#   List:   | 10  | 20  | 30  | 40  | 50  |
#           +-----+-----+-----+-----+-----+
#   Neg:   -5    -4    -3    -2    -1
#

numbers = [10, 20, 30, 40, 50]

# Positive indexing
print(f"\nFirst element: {numbers[0]}")    # 10
print(f"Third element: {numbers[2]}")      # 30
print(f"Last element: {numbers[4]}")       # 50

# Negative indexing (from the end)
print(f"Last element (neg): {numbers[-1]}")    # 50
print(f"Second to last: {numbers[-2]}")        # 40

# What happens if you go out of range?
# numbers[10]  # Uncomment this — you'll get IndexError!
# PRO TIP: Reading error messages is a skill. Always read them.


# ============================================
# SLICING — Getting a Sub-list
# ============================================
#
# list[start:stop:step]
# - start: where to begin (inclusive)
# - stop: where to end (EXCLUSIVE — Python is "up to but not including")
# - step: how many to skip
#

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"\nOriginal: {numbers}")
print(f"[2:5] = {numbers[2:5]}")        # [2, 3, 4] — index 2, 3, 4 (NOT 5!)
print(f"[:4] = {numbers[:4]}")           # [0, 1, 2, 3] — from start
print(f"[6:] = {numbers[6:]}")           # [6, 7, 8, 9] — to end
print(f"[::2] = {numbers[::2]}")         # [0, 2, 4, 6, 8] — every 2nd
print(f"[::-1] = {numbers[::-1]}")       # [9, 8, 7, ...] — REVERSE!

# Slicing creates a NEW list (copy)
sliced = numbers[2:5]
print(f"Sliced: {sliced}")
print(f"Original unchanged: {numbers}")  # Original is intact


# ============================================
# COMMON LIST METHODS
# ============================================

print("\n--- LIST METHODS ---")

fruits = ["apple", "banana"]
print(f"Starting list: {fruits}")

# append() — add to END
fruits.append("cherry")
print(f"After append('cherry'): {fruits}")

# insert() — add at INDEX
fruits.insert(1, "avocado")
print(f"After insert(1, 'avocado'): {fruits}")

# pop() — remove from END (returns the removed item)
last = fruits.pop()
print(f"After pop() — removed: {last}, list: {fruits}")

# pop(index) — remove at INDEX
first = fruits.pop(0)
print(f"After pop(0) — removed: {first}, list: {fruits}")

# remove(value) — remove first occurrence of VALUE
fruits.remove("banana")
print(f"After remove('banana'): {fruits}")

# sort() — in-place sort
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(f"\nAfter sort(): {numbers}")

# sorted() — returns NEW sorted list, original unchanged
original = [3, 1, 4, 1, 5, 9, 2, 6]
new_sorted = sorted(original)
print(f"Original: {original}")
print(f"sorted(original): {new_sorted}")

# reverse() — in-place reverse
numbers.reverse()
print(f"After reverse(): {numbers}")

# len() — get length
print(f"\nLength of {fruits}: {len(fruits)}")


# ============================================
# PRACTICE PROBLEMS
# ============================================
#
# Try to solve these BEFORE looking at the solutions below.
# Write your code in the space provided.
#

print("\n" + "=" * 50)
print("PRACTICE TIME!")
print("=" * 50)

# Problem 1: Given a list, return the middle element
# If list has even length, return the larger of the two middle elements
def get_middle(lst):
    """YOUR CODE HERE"""
    pass

# Problem 2: Given a list, return a new list with elements in reverse
# WITHOUT using [::-1] or .reverse()
def manual_reverse(lst):
    """YOUR CODE HERE"""
    pass

# Problem 3: Given a list, remove all duplicates and return sorted result
def remove_duplicates(lst):
    """YOUR CODE HERE"""
    pass


# ============================================
# SOLUTIONS (try first, then check!)
# ============================================

print("\n--- SOLUTIONS ---")

def get_middle_solution(lst):
    mid = len(lst) // 2
    if len(lst) % 2 == 0:
        return max(lst[mid - 1], lst[mid])
    return lst[mid]

print(f"get_middle([1,2,3,4,5]) = {get_middle_solution([1, 2, 3, 4, 5])}")  # 3
print(f"get_middle([1,2,3,4]) = {get_middle_solution([1, 2, 3, 4])}")      # 3
print(f"get_middle([1,2,3,4,5,6]) = {get_middle_solution([1, 2, 3, 4, 5, 6])}")  # 4

def manual_reverse_solution(lst):
    result = []
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])
    return result

print(f"manual_reverse([1,2,3]) = {manual_reverse_solution([1, 2, 3])}")  # [3, 2, 1]

def remove_duplicates_solution(lst):
    return sorted(set(lst))

print(f"remove_duplicates([3,1,2,1,3]) = {remove_duplicates_solution([3, 1, 2, 1, 3])}")  # [1, 2, 3]


# ============================================
# TEST RUNNER
# ============================================

def run_tests():
    """Run all tests — call this at the end"""
    passed = 0
    failed = 0

    # Test get_middle
    tests = [
        (get_middle_solution([1, 2, 3, 4, 5]), 3),
        (get_middle_solution([1, 2, 3, 4]), 3),
        (get_middle_solution([1, 2, 3, 4, 5, 6]), 4),
    ]

    for result, expected in tests:
        if result == expected:
            print(f"PASS: get_middle = {result}")
            passed += 1
        else:
            print(f"FAIL: got {result}, expected {expected}")
            failed += 1

    # Test manual_reverse
    tests = [
        (manual_reverse_solution([1, 2, 3]), [3, 2, 1]),
        (manual_reverse_solution([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1]),
    ]

    for result, expected in tests:
        if result == expected:
            print(f"PASS: manual_reverse = {result}")
            passed += 1
        else:
            print(f"FAIL: got {result}, expected {expected}")
            failed += 1

    # Test remove_duplicates
    tests = [
        (remove_duplicates_solution([3, 1, 2, 1, 3]), [1, 2, 3]),
        (remove_duplicates_solution([1, 1, 1]), [1]),
    ]

    for result, expected in tests:
        if result == expected:
            print(f"PASS: remove_duplicates = {result}")
            passed += 1
        else:
            print(f"FAIL: got {result}, expected {expected}")
            failed += 1

    print(f"\nResults: {passed} passed, {failed} failed")

if __name__ == "__main__":
    run_tests()
