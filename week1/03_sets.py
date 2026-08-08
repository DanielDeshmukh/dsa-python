"""
=============================================
DAY 3: SETS — Dedup and Fast Membership
=============================================

Run this file: python week1/03_sets.py
"""

# ============================================
# VISUAL: What is a Set?
# ============================================
#
# A set is an UNORDERED collection of UNIQUE elements.
# Think of it as a bag — no duplicates, no order.
#
#   +-----+-----+-----+-----+
#   |  3  |  1  |  4  |  2  |   (order not guaranteed)
#   +-----+-----+-----+-----+
#
# - No indexing (sets are unordered)
# - Membership check is O(1) — INSTANT
# - Perfect for deduplication and "is X in here?"
#


# ============================================
# CREATING SETS
# ============================================

# Empty set (CANNOT use {} — that creates an empty dict!)
empty = set()
print(f"Empty set: {empty}")

# Set with values
numbers = {1, 2, 3, 4, 5}
print(f"Numbers: {numbers}")

# From a list (auto-dedup)
from_list = set([1, 1, 2, 2, 3, 3])
print(f"From list: {from_list}")  # {1, 2, 3}

# From a string
from_string = set("hello")
print(f"From string: {from_string}")  # {'h', 'e', 'l', 'o'}


# ============================================
# SET OPERATIONS
# ============================================

print(f"\n--- BASIC OPERATIONS ---")

s = {1, 2, 3}

# Add
s.add(4)
print(f"After add(4): {s}")

# Remove (raises error if not found)
s.remove(4)
print(f"After remove(4): {s}")

# Discard (no error if not found)
s.discard(99)
print(f"After discard(99): {s}")  # No error!

# Membership check — O(1)!
print(f"2 in s: {2 in s}")
print(f"5 in s: {5 in s}")


# ============================================
# SET MATH (this is where sets shine)
# ============================================

print(f"\n--- SET MATH ---")

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union — everything in either set
print(f"Union (a | b): {a | b}")

# Intersection — only what's in BOTH
print(f"Intersection (a & b): {a & b}")

# Difference — what's in A but not B
print(f"Difference (a - b): {a - b}")

# Symmetric difference — what's in A or B, but NOT both
print(f"Sym diff (a ^ b): {a ^ b}")

# Visual:
#
#   Set A:    {1, 2, 3, 4, 5}
#   Set B:    {4, 5, 6, 7, 8}
#
#   Union (|):        {1, 2, 3, 4, 5, 6, 7, 8}
#   Intersection (&): {4, 5}
#   Diff (A - B):     {1, 2, 3}
#   Sym Diff (^):     {1, 2, 3, 6, 7, 8}
#


# ============================================
# COMMON SET PATTERNS IN DSA
# ============================================

print(f"\n--- DSA PATTERNS ---")

# Pattern 1: Remove duplicates
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(nums))
print(f"Dedup: {unique}")

# Pattern 2: Check if elements exist
required = {"python", "java", "sql"}
applicant_skills = {"python", "java", "javascript", "sql"}

if required.issubset(applicant_skills):
    print("Candidate has all required skills!")

# Pattern 3: Find common elements between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(f"Common: {common}")

# Pattern 4: Set intersection for fast lookup
users_day1 = {"alice", "bob", "charlie"}
users_day2 = {"bob", "diana", "charlie"}
returning = users_day1 & users_day2
print(f"Returning users: {returning}")


# ============================================
# PRACTICE PROBLEMS
# ============================================

print("\n" + "=" * 50)
print("PRACTICE TIME!")
print("=" * 50)

# Problem 1: Check if two strings are anagrams
def is_anagram(s1, s2):
    """YOUR CODE HERE"""
    pass

# Problem 2: Find all unique characters in a string
def unique_chars(s):
    """YOUR CODE HERE"""
    pass

# Problem 3: Given a list of sets, find elements common to ALL
def common_in_all(sets_list):
    """YOUR CODE HERE"""
    pass


# ============================================
# SOLUTIONS
# ============================================

print("\n--- SOLUTIONS ---")

def is_anagram_solution(s1, s2):
    return set(s1.lower()) == set(s2.lower())

print(f"is_anagram('listen', 'silent') = {is_anagram_solution('listen', 'silent')}")  # True
print(f"is_anagram('hello', 'world') = {is_anagram_solution('hello', 'world')}")    # False

def unique_chars_solution(s):
    return list(set(s))

print(f"unique_chars('hello') = {unique_chars_solution('hello')}")  # ['h', 'e', 'l', 'o']

def common_in_all_solution(sets_list):
    if not sets_list:
        return set()
    result = sets_list[0]
    for s in sets_list[1:]:
        result = result & s
    return result

print(f"common_in_all([{{1,2,3}},{{2,3,4}},{{3,4,5}}]) = {common_in_all_solution([{1, 2, 3}, {2, 3, 4}, {3, 4, 5}])}")  # {3}


# ============================================
# TEST RUNNER
# ============================================

def run_tests():
    passed = 0
    failed = 0

    tests = [
        (is_anagram_solution("listen", "silent"), True),
        (is_anagram_solution("hello", "world"), False),
        (set(unique_chars_solution("hello")), {"h", "e", "l", "o"}),
        (common_in_all_solution([{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]), {3}),
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
