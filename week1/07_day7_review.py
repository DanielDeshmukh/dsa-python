"""
=============================================
DAY 7: REVIEW — Mix All Concepts
=============================================

Run this file: python week1/07_day7_review.py

This pulls together everything from Week 1.
If you can solve these, you're ready for Phase 1.
"""

# ============================================
# REVIEW: Quick Reference
# ============================================
#
# LIST:    [1, 2, 3]     — mutable, ordered, indexed
# DICT:    {"a": 1}       — key:value, O(1) lookup
# SET:     {1, 2, 3}      — unique, unordered, O(1) membership
# TUPLE:   (1, 2, 3)      — immutable, hashable
# STRING:  "hello"         — immutable sequence of chars
#
# COMPREHENSION SHORTHAND:
#   [x for x in range(10)]          — list
#   {x: x**2 for x in range(10)}    — dict
#   {x for x in range(10)}          — set
#


# ============================================
# MIXED PROBLEM 1: Word Frequency Counter
# ============================================
#
# Given a sentence, return the top N most common words.
# Ignore case, ignore punctuation.
#

from collections import Counter

def top_n_words(sentence, n):
    """YOUR CODE HERE"""
    pass

print("--- PROBLEM 1: Word Frequency ---")
result = top_n_words("the cat sat on the mat the cat ate the rat", 3)
print(f"Top 3: {result}")  # Expected: [('the', 4), ('cat', 2), ('sat', 1)]


# ============================================
# MIXED PROBLEM 2: Two Sum (Classic!)
# ============================================
#
# Given a list of numbers and a target, find two numbers
# that add up to the target. Return their indices.
#

def two_sum(nums, target):
    """YOUR CODE HERE"""
    pass

print("\n--- PROBLEM 2: Two Sum ---")
print(f"two_sum([2,7,11,15], 9) = {two_sum([2, 7, 11, 15], 9)}")  # [0, 1]
print(f"two_sum([3,2,4], 6) = {two_sum([3, 2, 4], 6)}")          # [1, 2]


# ============================================
# MIXED PROBLEM 3: Group Anagrams
# ============================================
#
# Given a list of words, group anagrams together.
#

from collections import defaultdict

def group_anagrams(words):
    """YOUR CODE HERE"""
    pass

print("\n--- PROBLEM 3: Group Anagrams ---")
result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(f"Anagram groups: {result}")
# Expected: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


# ============================================
# MIXED PROBLEM 4: Find Duplicates
# ============================================
#
# Given a list, find all elements that appear more than once.
#

def find_duplicates(nums):
    """YOUR CODE HERE"""
    pass

print("\n--- PROBLEM 4: Find Duplicates ---")
print(f"find_duplicates([1,2,3,2,4,3,5]) = {find_duplicates([1, 2, 3, 2, 4, 3, 5])}")
# Expected: [2, 3]


# ============================================
# MIXED PROBLEM 5: Matrix Transpose
# ============================================
#
# Given a matrix (list of lists), return its transpose.
#

def transpose(matrix):
    """YOUR CODE HERE"""
    pass

print("\n--- PROBLEM 5: Matrix Transpose ---")
matrix = [[1, 2, 3], [4, 5, 6]]
print(f"Original: {matrix}")
print(f"Transposed: {transpose(matrix)}")
# Expected: [[1, 4], [2, 5], [3, 6]]


# ============================================
# SOLUTIONS
# ============================================

print("\n" + "=" * 50)
print("SOLUTIONS (try first!)")
print("=" * 50)

def top_n_words_solution(sentence, n):
    # Clean: lowercase, remove punctuation
    import string
    cleaned = sentence.lower()
    for char in string.punctuation:
        cleaned = cleaned.replace(char, "")
    words = cleaned.split()
    return Counter(words).most_common(n)

def two_sum_solution(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def group_anagrams_solution(words):
    groups = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        groups[key].append(word)
    return list(groups.values())

def find_duplicates_solution(nums):
    freq = Counter(nums)
    return [num for num, count in freq.items() if count > 1]

def transpose_solution(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


# ============================================
# TEST RUNNER
# ============================================

def run_tests():
    passed = 0
    failed = 0

    # Test top_n_words
    result = top_n_words_solution("the cat sat on the mat the cat ate the rat", 3)
    expected = [('the', 4), ('cat', 2), ('ate', 1)]  # or similar
    if result[0] == ('the', 4):  # At least check top 1
        print("PASS: top_n_words")
        passed += 1
    else:
        print(f"FAIL: top_n_words got {result}")
        failed += 1

    # Test two_sum
    tests = [
        (two_sum_solution([2, 7, 11, 15], 9), [0, 1]),
        (two_sum_solution([3, 2, 4], 6), [1, 2]),
    ]
    for result, expected in tests:
        if result == expected:
            print(f"PASS: two_sum = {result}")
            passed += 1
        else:
            print(f"FAIL: two_sum got {result}, expected {expected}")
            failed += 1

    # Test find_duplicates
    result = find_duplicates_solution([1, 2, 3, 2, 4, 3, 5])
    if sorted(result) == [2, 3]:
        print(f"PASS: find_duplicates = {result}")
        passed += 1
    else:
        print(f"FAIL: find_duplicates got {result}")
        failed += 1

    # Test transpose
    result = transpose_solution([[1, 2, 3], [4, 5, 6]])
    expected = [[1, 4], [2, 5], [3, 6]]
    if result == expected:
        print(f"PASS: transpose = {result}")
        passed += 1
    else:
        print(f"FAIL: transpose got {result}, expected {expected}")
        failed += 1

    print(f"\nResults: {passed} passed, {failed} failed")

if __name__ == "__main__":
    run_tests()
