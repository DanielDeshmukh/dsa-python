"""
=============================================
DAY 6: STRINGS — Operations & Tricks
=============================================

Run this file: python week1/06_strings.py
"""

# ============================================
# VISUAL: Strings are Immutable
# ============================================
#
# Strings are like tuples of characters — IMMUTABLE.
#
#   Index:    0     1     2     3     4
#           +-----+-----+-----+-----+-----+
#   String: |  h  |  e  |  l  |  l  |  o  |
#           +-----+-----+-----+-----+-----+
#
# - You can READ characters, but can't CHANGE them
# - s[0] = 'H'  # ERROR! Can't do this
# - Must create a NEW string instead
#


# ============================================
# CREATING STRINGS
# ============================================

s1 = "hello"
s2 = 'world'
s3 = """multi
line"""

print(f"Single: {s1}")
print(f"Double: {s2}")
print(f"Multi-line:\n{s3}")


# ============================================
# INDEXING & SLICING (same as lists!)
# ============================================

print(f"\n--- INDEXING & SLICING ---")

s = "hello world"

print(f"First: {s[0]}")
print(f"Last: {s[-1]}")
print(f"Slice [0:5]: {s[0:5]}")
print(f"Reverse: {s[::-1]}")
print(f"Every 2nd: {s[::2]}")


# ============================================
# COMMON STRING METHODS
# ============================================

print(f"\n--- METHODS ---")

s = "  Hello, World!  "

# Case methods
print(f"upper(): {s.upper()}")
print(f"lower(): {s.lower()}")
print(f"title(): {s.title()}")
print(f"strip(): '{s.strip()}'")  # Remove whitespace
print(f"lstrip(): '{s.strip()}'")
print(f"rstrip(): '{s.rstrip()}'")

# Search methods
text = "hello world hello python"
print(f"\nfind('world'): {text.find('world')}")   # Index of first match
print(f"find('java'): {text.find('java')}")       # -1 if not found
print(f"count('hello'): {text.count('hello')}")

# Split and join (SUPER COMMON)
csv = "apple,banana,cherry"
fruits = csv.split(",")
print(f"split(','): {fruits}")

back_to_string = " | ".join(fruits)
print(f"join(): {back_to_string}")

# Replace
original = "hello world"
modified = original.replace("world", "python")
print(f"replace(): {modified}")

# Start/End with
print(f"\nstartswith('hello'): {original.startswith('hello')}")
print(f"endswith('world'): {original.endswith('world')}")

# Check methods
print(f"\nisdigit(): {'123'.isdigit()}")
print(f"isalpha(): {'abc'.isalpha()}")
print(f"isalnum(): {'abc123'.isalnum()}")


# ============================================
# STRING FORMATTING
# ============================================

print(f"\n--- FORMATTING ---")

name = "Daniel"
age = 25

# f-strings (BEST way)
print(f"My name is {name} and I'm {age}")

# Expressions in f-strings
print(f"10 years later: {age + 10}")
print(f"Name uppercase: {name.upper()}")

# Formatting numbers
pi = 3.14159
print(f"Pi to 2 decimals: {pi:.2f}")

# Padding
for i in range(1, 6):
    print(f"{'#' * i:<10} Row {i}")


# ============================================
# STRING PATTERNS IN DSA
# ============================================

print(f"\n--- DSA PATTERNS ---")

# Pattern 1: Character frequency
def char_freq(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq

print(f"char_freq('aabbbcc'): {char_freq('aabbbcc')}")

# Pattern 2: Check palindrome
def is_palindrome(s):
    return s == s[::-1]

print(f"is_palindrome('racecar'): {is_palindrome('racecar')}")
print(f"is_palindrome('hello'): {is_palindrome('hello')}")

# Pattern 3: Reverse words in string
def reverse_words(s):
    return " ".join(s.split()[::-1])

print(f"reverse_words('hello world python'): {reverse_words('hello world python')}")

# Pattern 4: Check if two strings are anagrams
def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print(f"is_anagram('listen', 'silent'): {is_anagram('listen', 'silent')}")


# ============================================
# PRACTICE PROBLEMS
# ============================================

print("\n" + "=" * 50)
print("PRACTICE TIME!")
print("=" * 50)

# Problem 1: Find the first non-repeating character
def first_unique_char(s):
    """YOUR CODE HERE"""
    pass

# Problem 2: Check if a string is a valid palindrome (ignore non-alphanumeric)
def valid_palindrome(s):
    """YOUR CODE HERE"""
    pass

# Problem 3: Compress a string (aaabbbcc -> a3b3c2)
def compress_string(s):
    """YOUR CODE HERE"""
    pass


# ============================================
# SOLUTIONS
# ============================================

print("\n--- SOLUTIONS ---")

def first_unique_char_solution(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    for i, c in enumerate(s):
        if freq[c] == 1:
            return i
    return -1

print(f"first_unique_char('aabbc'): {first_unique_char_solution('aabbc')}")  # 4
print(f"first_unique_char('aabb'): {first_unique_char_solution('aabb')}")    # -1

def valid_palindrome_solution(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

print(f"valid_palindrome('A man a plan a canal Panama'): {valid_palindrome_solution('A man a plan a canal Panama')}")

def compress_string_solution(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return "".join(result)

print(f"compress_string('aaabbbcc'): {compress_string_solution('aaabbbcc')}")


# ============================================
# TEST RUNNER
# ============================================

def run_tests():
    passed = 0
    failed = 0

    tests = [
        (first_unique_char_solution("aabbc"), 4),
        (first_unique_char_solution("aabb"), -1),
        (valid_palindrome_solution("A man a plan a canal Panama"), True),
        (compress_string_solution("aaabbbcc"), "a3b3c2"),
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
