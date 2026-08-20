#Covering python basic syntaxes
"""
============================

PYTHON DSA QUICK RECAP

============================

Variables

- Python is dynamically typed (same variable can hold different data types).
- Common types: int, float, str, bool.

Input

- int(input())            -> Single integer
- float(input())          -> Single float
- input()                 -> String
- map(int, input().split()) -> Multiple integers
- list(map(int, input().split())) -> List of integers

Output

- print(x)                -> Print value
- print(a, b)             -> Multiple values
- print(x, end=" ")       -> Stay on same line
- f"..."                  -> Formatted string (f-string)

Data Types

- int, float, str, bool, list, tuple, set, dict, None
- type(x) -> Returns the data type

Arithmetic Operators

+  Addition
-  Subtraction
*  Multiplication
/  Float Division
// Integer (Floor) Division
%  Modulus (Remainder)
** Exponent (Power)

Comparison Operators

==, !=, >, <, >=, <=

Logical Operators

and, or, not

If-Else

- if / elif / else
- Indentation is mandatory.

Loops

- for -> Iterate over a sequence/range
- while -> Repeat until condition becomes False
- range(stop)
- range(start, stop)
- range(start, stop, step)
- break -> Exit loop immediately
- continue -> Skip current iteration and move to next

Functions

- def function_name(...):
- return -> Sends value back
- Default parameters are used only if no argument is passed.

Strings

- Indexing: s[0], s[-1]
- Length: len(s)
- Slicing: s[start:stop:step]
- s[::-1] -> Reverse string
- Strings are immutable.

Important String Methods

- lower()        -> Lowercase
- upper()        -> Uppercase
- strip()        -> Remove leading/trailing spaces
- replace()      -> Replace substring
- split()        -> String → List
- join()         -> List → String
- find()         -> First index (-1 if not found)
- count()        -> Count occurrences
- startswith()   -> Prefix check
- endswith()     -> Suffix check

Lists (Most Important for DSA)

- Ordered & Mutable
- Access: arr[i]
- Modify: arr[i] = value
- len(arr)
- append()  -> Add at end
- insert()  -> Add at index
- pop()     -> Remove element
- del       -> Delete element
- extend()  -> Add multiple elements
- reverse() -> Reverse list
- sort()    -> Ascending
- sort(reverse=True) -> Descending
- Traverse using 'for x in arr' or indices

============================

DSA MUST-KNOW METHODS

============================

Strings : len(), lower(), upper(), strip(), replace(), split(), join(),
find(), count(), startswith(), endswith()

Lists   : append(), pop(), insert(), extend(), reverse(), sort()

Sets    : add(), remove(), in

Dicts   : get(), items(), keys(), values()
============================
"""