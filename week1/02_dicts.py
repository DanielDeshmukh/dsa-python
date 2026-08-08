"""
=============================================
DAY 2: DICTS — O(1) Lookup Magic
=============================================

Run this file: python week1/02_dicts.py
"""

# ============================================
# VISUAL: What is a Dict?
# ============================================
#
# A dict maps KEYS to VALUES. Like a real dictionary:
#   word (key) -> definition (value)
#
#   +-----------+-----------+
#   |    Key    |   Value   |
#   +-----------+-----------+
#   |  "name"   | "Daniel"  |
#   |  "age"    |    25     |
#   |  "lang"   | "Python"  |
#   +-----------+-----------+
#
# - Keys must be UNIQUE (no duplicates)
# - Keys must be IMMUTABLE (string, int, tuple — NOT list)
# - Values can be anything
# - Lookup by key is O(1) — INSTANT, no matter the size!
#


# ============================================
# CREATING DICTS
# ============================================

# Empty dict
empty = {}
print(f"Empty dict: {empty}")

# Dict with values
person = {
    "name": "Daniel",
    "age": 25,
    "language": "Python"
}
print(f"Person: {person}")

# Using dict() constructor
from_pairs = dict([("a", 1), ("b", 2)])
print(f"From pairs: {from_pairs}")


# ============================================
# ACCESSING VALUES
# ============================================

person = {"name": "Daniel", "age": 25, "lang": "Python"}

print(f"\n--- ACCESSING ---")

# Square bracket access
print(f"Name: {person['name']}")

# What if key doesn't exist?
# person['email']  # Uncomment — you'll get KeyError!

# .get() — SAFE access with default
print(f"Email (safe): {person.get('email', 'not found')}")

# Check if key exists
print(f"'name' in person: {'name' in person}")
print(f"'email' in person: {'email' in person}")


# ============================================
# MODIFYING DICTS
# ============================================

print(f"\n--- MODIFYING ---")

person = {"name": "Daniel", "age": 25}

# Add new key-value pair
person["email"] = "daniel@example.com"
print(f"After adding email: {person}")

# Update existing value
person["age"] = 26
print(f"After updating age: {person}")

# Remove a key
del person["email"]
print(f"After deleting email: {person}")

# pop() — remove and return
lang = person.pop("lang", "not found")
print(f"Popped lang: {lang}")

# Update multiple at once
person.update({"age": 27, "city": "Mumbai"})
print(f"After update(): {person}")


# ============================================
# ITERATING OVER DICTS
# ============================================

print(f"\n--- ITERATING ---")

scores = {"Alice": 95, "Bob": 87, "Charlie": 92}

# Iterate over keys (default)
print("Keys:")
for name in scores:
    print(f"  {name}")

# Iterate over values
print("\nValues:")
for score in scores.values():
    print(f"  {score}")

# Iterate over key-value pairs (MOST USEFUL)
print("\nKey-Value pairs:")
for name, score in scores.items():
    print(f"  {name}: {score}")


# ============================================
# USEFUL DICT PATTERNS
# ============================================

print(f"\n--- COMMON PATTERNS ---")

# Frequency counting (SUPER COMMON in DSA)
text = "hello world"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(f"Frequency of '{text}': {freq}")

# Counting with defaultdict
from collections import defaultdict

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = defaultdict(int)  # default value = 0
for word in words:
    count[word] += 1
print(f"Word count: {dict(count)}")

# Grouping with defaultdict
students = [("A", "Math"), ("B", "Science"), ("A", "Science"), ("B", "Math")]
groups = defaultdict(list)
for student, subject in students:
    groups[subject].append(student)
print(f"Groups: {dict(groups)}")


# ============================================
# PRACTICE PROBLEMS
# ============================================

print("\n" + "=" * 50)
print("PRACTICE TIME!")
print("=" * 50)

# Problem 1: Given a string, return the most frequent character
def most_frequent(s):
    """YOUR CODE HERE"""
    pass

# Problem 2: Given two dicts, merge them (second overrides first)
def merge_dicts(d1, d2):
    """YOUR CODE HERE"""
    pass

# Problem 3: Invert a dict (swap keys and values)
def invert_dict(d):
    """YOUR CODE HERE"""
    pass


# ============================================
# SOLUTIONS
# ============================================

print("\n--- SOLUTIONS ---")

def most_frequent_solution(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return max(freq, key=freq.get)

print(f"most_frequent('aabbbcc') = {most_frequent_solution('aabbbcc')}")  # 'b'

def merge_dicts_solution(d1, d2):
    result = d1.copy()
    result.update(d2)
    return result

print(f"merge_dicts({{'a':1}}, {{'b':2}}) = {merge_dicts_solution({'a': 1}, {'b': 2})}")

def invert_dict_solution(d):
    return {v: k for k, v in d.items()}

print(f"invert_dict({{'a':1,'b':2}}) = {invert_dict_solution({'a': 1, 'b': 2})}")


# ============================================
# TEST RUNNER
# ============================================

def run_tests():
    passed = 0
    failed = 0

    tests = [
        (most_frequent_solution("aabbbcc"), "b"),
        (most_frequent_solution("hello"), "l"),
        (merge_dicts_solution({"a": 1}, {"b": 2}), {"a": 1, "b": 2}),
        (invert_dict_solution({"a": 1, "b": 2}), {1: "a", 2: "b"}),
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
