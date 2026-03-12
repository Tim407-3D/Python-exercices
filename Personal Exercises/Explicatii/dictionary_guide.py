# DICTIONARIES - EFFICIENT USAGE GUIDE
# =====================================

# What is a Dictionary?
# A dictionary is a collection of key-value pairs that allows fast lookup, insertion, and deletion.

# 1. Basic Dictionary Creation and Access
print("=== BASIC DICTIONARY OPERATIONS ===")

# Creating dictionaries
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

# Accessing values (efficient O(1) operation)
print(f"Alice's grade: {student_grades['Alice']}")

# Safe access with .get() method (avoids KeyError)
print(f"David's grade: {student_grades.get('David', 'Not found')}")

# 2. Efficient Dictionary Patterns
print("\n=== EFFICIENT PATTERNS ===")

# Pattern 1: Counting occurrences
def count_words(text):
    word_count = {}
    for word in text.split():
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

sentence = "the quick brown fox jumps over the lazy dog the fox"
counts = count_words(sentence)
print(f"Word counts: {counts}")

# Pattern 2: Grouping data
students_by_grade = {
    "A": ["Alice", "Emma"],
    "B": ["Bob", "David"],
    "C": ["Charlie"]
}

# Pattern 3: Using defaultdict for automatic initialization
from collections import defaultdict

def group_by_first_letter(words):
    groups = defaultdict(list)
    for word in words:
        groups[word[0]].append(word)
    return dict(groups)

words = ["apple", "banana", "cherry", "apricot", "blueberry"]
grouped = group_by_first_letter(words)
print(f"Words by first letter: {grouped}")

# 3. Dictionary Comprehensions (Very Efficient!)
print("\n=== DICTIONARY COMPREHENSIONS ===")

# Traditional way
squares = {}
for i in range(1, 6):
    squares[i] = i ** 2

# Dictionary comprehension (more efficient and readable)
squares_comp = {i: i ** 2 for i in range(1, 6)}
print(f"Squares: {squares_comp}")

# Conditional comprehension
even_squares = {i: i ** 2 for i in range(1, 11) if i % 2 == 0}
print(f"Even squares: {even_squares}")

# 4. Valid Reasons to Use Dictionaries Efficiently
print("\n=== PRACTICAL USE CASES ===")

# Use Case 1: Configuration Management
config = {
    "database_url": "localhost:5432",
    "max_connections": 100,
    "timeout": 30,
    "debug": True
}

def get_config_value(key, default=None):
    """Efficient config lookup with fallback"""
    return config.get(key, default)

print(f"Database URL: {get_config_value('database_url')}")
print(f"Log level: {get_config_value('log_level', 'INFO')}")

# Use Case 2: Caching/Memoization
def fibonacci_with_cache(n, cache={}):
    """Efficient Fibonacci using dictionary cache"""
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    
    result = fibonacci_with_cache(n-1, cache) + fibonacci_with_cache(n-2, cache)
    cache[n] = result
    return result

print(f"Fibonacci(10): {fibonacci_with_cache(10)}")

# Use Case 3: Data Transformation
def transform_student_data(raw_data):
    """Transform list of tuples to dictionary for efficient lookup"""
    return {student_id: {"name": name, "grade": grade} 
            for student_id, name, grade in raw_data}

raw_students = [
    (1, "Alice", 85),
    (2, "Bob", 92),
    (3, "Charlie", 78)
]

student_dict = transform_student_data(raw_students)
print(f"Student 2 info: {student_dict[2]}")

# Use Case 4: Frequency Analysis
def analyze_text_frequency(text):
    """Efficient text analysis using dictionaries"""
    frequency = defaultdict(int)
    
    for char in text.lower():
        if char.isalpha():
            frequency[char] += 1
    
    return dict(frequency)

text = "Hello World! This is a test."
freq_analysis = analyze_text_frequency(text)
print(f"Letter frequency: {freq_analysis}")

# 5. Performance Tips
print("\n=== PERFORMANCE TIPS ===")

# Tip 1: Use .get() for safe access
# Tip 2: Use defaultdict for grouping
# Tip 3: Use dict comprehensions for transformations
# Tip 4: Choose appropriate keys (immutable types)

# Bad key example (will cause error)
try:
    bad_dict = {[1, 2, 3]: "value"}  # Lists are mutable, can't be keys
except TypeError as e:
    print(f"Error with list key: {e}")

# Good key examples
good_keys = {
    "string": "works",
    42: "works", 
    (1, 2): "works",  # Tuples are immutable
    frozenset({1, 2}): "works"  # Frozen sets are immutable
}

print(f"Good keys example: {good_keys}")

# 6. Dictionary Methods Overview
print("\n=== USEFUL DICTIONARY METHODS ===")

sample_dict = {"a": 1, "b": 2, "c": 3}

# Get all keys, values, items
print(f"Keys: {list(sample_dict.keys())}")
print(f"Values: {list(sample_dict.values())}")
print(f"Items: {list(sample_dict.items())}")

# Update dictionary
sample_dict.update({"d": 4, "e": 5})
print(f"After update: {sample_dict}")

# Remove items
removed_value = sample_dict.pop("a", "default")
print(f"Removed 'a': {removed_value}")
print(f"Remaining: {sample_dict}")

print("\n=== SUMMARY ===")
print("Dictionaries are most efficient when:")
print("1. You need fast O(1) lookups by key")
print("2. You're counting frequencies or grouping data")
print("3. You need to associate related information")
print("4. You're implementing caches or memoization")
print("5. You're transforming data structures")
