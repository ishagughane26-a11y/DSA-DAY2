# DSA-DAY2

# DSA With Python 🚀

Welcome to my Python and Data Structures & Algorithms learning repository.  
This repository contains daily coding practice, Python fundamentals, problem-solving questions, string manipulation programs, dictionaries, tuples, arrays, and pattern-based logic building exercises.

---

# 📅 Day 2- Strings, Dictionaries, Tuples & Problem Solving

---

## 📌 String Methods Practiced

- `isalnum()`
- `isalpha()`
- `isdigit()`
- `islower()`
- `isupper()`
- `istitle()`
- `isspace()`
- `startswith()`
- `endswith()`
- `find()`
- `index()`
- `count()`

---

## 📌 String Operations
- `lower()`
- `upper()`
- `swapcase()`
- `title()`
- `capitalize()`
- String formatting using:
  - `format()`
  - f-strings

Example:
```python
name = "prashant"
sal = 5000
age = 28

print("{} sal is {} age is {}".format(name,sal,age))
print(f"{name} is a good boy")
````

---

# 📌 Nested Loop Pattern Programs

### Patterns Practiced

* Number patterns
* Alphabet patterns
* Star patterns
* Pyramid patterns
* Reverse patterns

Example:

```python
for i in range(1,5):
    for j in range(1,5):
        print(i,end=" ")
    print()
```

---

# 📌 Array Problems

## ✅ Product of Array Except Self

### Problem

```python
Input : [1,2,3,4]
Output: [24,12,8,6]
```

### Solution

```python
arr = [1,2,3,4]
product = 1

for i in arr:
    product = product * i

for i in range(len(arr)):
    arr[i] = product // arr[i]

print(arr)
```

---

# 📌 Dictionary Concepts

Topics Covered:

* Dictionary creation
* Accessing values using keys
* Updating values
* Iterating keys and values
* `items()`
* `values()`
* `pop()`
* `copy()`

### Practice Problems

* Tuple as dictionary key
* Frequency count of elements
* Maximum & minimum dictionary values
* Dictionary key behavior with different datatypes

---

# 📌 String Problem Solving

## ✅ Remove Duplicate Characters

```python
Input : "prashant"
Output: "prashnt"
```

---

## ✅ Reverse a String

```python
Input : "prashant"
Output: "tnahsarp"
```

---

## ✅ Palindrome Check

```python
Input : "NAMAN"
Output: Palindrome
```

---

## ✅ Anagram Check

```python
Input : listen, silent
Output: ANAGRAM
```

---

## ✅ Count Vowels & Consonants

---

## ✅ Count Words in Sentence

```python
Input : "This is a sentence"
Output: 4
```

---

# 📌 Number Logic Programs

## ✅ Reverse a Number

```python
Input : 123
Output: 321
```

---

# 📌 Tuple Concepts

Topics Practiced:

* Tuple creation
* Tuple immutability
* Tuple multiplication
* Tuple slicing
* Tuple length
* Difference between tuple and string

---

# 📌 Type Conversion Functions

### Functions Practiced

* `int()`
* `float()`
* `complex()`
* `bool()`

---

# 📌 Concepts Learned

* String manipulation techniques
* Dictionary operations and hashing behavior
* Pattern printing logic using nested loops
* Array transformation problems
* Problem-solving using loops and conditions
* Tuple immutability concepts


# 🛠️ Technologies Used
* Python 3
* VS Code
# 🎯 Learning Outcome
Today I practiced string manipulation, dictionary operations, tuple concepts, nested loops, and array-based DSA problems to improve logical thinking and coding efficiency.

# 🚀 Repository Goal
To document my daily DSA and Python learning journey consistently while improving problem-solving skills for placements and interviews.



```
```
