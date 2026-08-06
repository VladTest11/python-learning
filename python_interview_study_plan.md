# Python Technical Interview Study Plan - Junior Developer

## Overview
**Target Role:** Junior Python Developer  
**Total Duration:** 8-12 weeks (accelerate based on your 3-10 hrs/day commitment)  
**Focus Sectors:** Web Development, Data Analysis, Automation (highest job availability)

---

## Phase 1: Python Foundations (Weeks 1-4)

### Week 1: Core Python Fundamentals

#### Day 1-2: Data Types & Variables
**Time Allocation:** 3hrs: theory+1 exercise | 5hrs: theory+2 exercises | 10hrs: theory+all exercises+extras

**Concepts to Learn:**
- Variables and naming conventions (PEP 8)
- Basic data types: int, float, str, bool
- Type conversion and type checking
- String operations and formatting (f-strings, .format(), %)

**Technical Architecture Insight:**
Python is dynamically typed (variables don't need type declarations), but it's strongly typed (types matter in operations). Understanding this helps you predict errors.

**Exercise 1.1 - Temperature Converter**
```
Problem: Create a function that converts Celsius to Fahrenheit and vice versa.

Why this matters: Teaches function basics, type handling, and mathematical operations.

Requirements:
- Function should accept temperature and unit ('C' or 'F')
- Return converted temperature with proper rounding
- Handle invalid inputs gracefully
```

**Exercise 1.2 - String Analyzer**
```
Problem: Create a function that analyzes a string and returns:
- Character count
- Word count
- Most frequent character

Why this matters: String manipulation is crucial in real applications (parsing data, validation, text processing).

Technical note: This introduces dictionaries for counting - a common pattern in Python.
```

#### Day 3-4: Collections (Lists, Tuples, Sets, Dictionaries)

**Concepts to Learn:**
- List operations: append, extend, insert, remove, slice
- Tuple immutability and use cases
- Set operations: union, intersection, difference
- Dictionary operations: keys, values, items, get, setdefault
- When to use each collection type

**Architecture Insight:**
Each collection type has different performance characteristics:
- Lists: O(1) append, O(n) search
- Sets: O(1) search, membership testing
- Dictionaries: O(1) key lookup (hash table underneath)

**Exercise 1.3 - Contact Book**
```
Problem: Build a simple contact management system using dictionaries.

Features:
- Add contact (name, phone, email)
- Search contact by name
- Update contact information
- Delete contact
- List all contacts

Why this matters: Real-world CRUD operations (Create, Read, Update, Delete) - foundation of most applications.

Technical architecture: Dictionary stores contacts, each contact is a nested dictionary. This is a simple in-memory database pattern.
```

**Exercise 1.4 - Duplicate Remover**
```
Problem: Given a list of numbers, remove duplicates while preserving order.

Why this matters: Common interview question testing understanding of sets vs lists.

Challenge: Do it in two ways:
1. Using sets (explain why order might change)
2. Preserving original order (explain the algorithm)
```

#### Day 5-6: Control Flow & Functions

**Concepts to Learn:**
- if/elif/else statements
- for loops and while loops
- break, continue, pass
- List comprehensions
- Function definition, parameters, return values
- Default arguments, *args, **kwargs
- Scope (local, global, nonlocal)

**Architecture Insight:**
List comprehensions are Pythonic - they're faster and more readable than traditional loops for simple transformations. Understanding when to use them vs regular loops is key.

**Exercise 1.5 - Grade Calculator**
```
Problem: Create a grading system that:
- Accepts a list of student scores
- Calculates letter grades (A: 90-100, B: 80-89, etc.)
- Returns statistics: average, highest, lowest, pass rate

Why this matters: Combines conditionals, loops, and functions. Common pattern for data processing.

Technical note: This teaches you to break problems into smaller functions (separation of concerns).
```

**Exercise 1.6 - FizzBuzz (Classic Interview Problem)**
```
Problem: Print numbers 1-100, but:
- For multiples of 3, print "Fizz"
- For multiples of 5, print "Buzz"
- For multiples of both, print "FizzBuzz"

Why this matters: Tests basic logic and modulo operations. Extremely common screening question.

Challenge: Write it three ways:
1. Basic if/else
2. List comprehension
3. Using a dictionary (mapping divisors to words)
```

#### Day 7: Practice & Review

**Mini-Project: Expense Tracker**
```
Build a command-line expense tracker:
- Add expense (amount, category, description)
- View all expenses
- Calculate total by category
- Find largest expense

Technical architecture breakdown:
- Data structure: List of dictionaries (each expense is a dict)
- Why? Easy to add/iterate, flexible structure
- Alternative: Could use classes (we'll learn this next week)

This simulates real application structure where you store collections of related data.
```

---

### Week 2: Object-Oriented Programming (OOP)

#### Day 1-2: Classes and Objects

**Concepts to Learn:**
- Class definition and instantiation
- `__init__` constructor method
- Instance variables vs class variables
- Methods (instance methods, class methods, static methods)
- `self` parameter - what it really means

**Architecture Insight:**
OOP organizes code around "objects" that bundle data (attributes) and behavior (methods). This is crucial for maintaining large codebases. Think of classes as blueprints, objects as the actual houses built from those blueprints.

**Exercise 2.1 - Bank Account Class**
```
Problem: Create a BankAccount class with:
- Attributes: account_number, holder_name, balance
- Methods: deposit(), withdraw(), get_balance()
- Validation: Can't withdraw more than balance

Why this matters: Real-world entity modeling. Almost every application models real-world objects as classes.

Technical explanation:
- __init__ sets up initial state
- Methods modify state (self.balance)
- Encapsulation: Balance can't be directly set, only through methods
```

**Exercise 2.2 - Inventory System**
```
Problem: Create Product and Inventory classes.

Product class:
- Attributes: id, name, price, quantity
- Method: update_quantity()

Inventory class:
- Stores multiple products
- Methods: add_product(), remove_product(), search_by_name(), total_value()

Why this matters: Shows class composition (Inventory contains Products). This is how complex systems are built.
```

#### Day 3-4: Inheritance and Polymorphism

**Concepts to Learn:**
- Parent and child classes
- Method overriding
- `super()` function
- Multiple inheritance (briefly)
- Abstract base classes concept

**Architecture Insight:**
Inheritance models "is-a" relationships. A Dog "is-a" Animal. Use it to share common behavior and specialize where needed. However, prefer composition over inheritance when relationship isn't clearly "is-a".

**Exercise 2.3 - Employee Management System**
```
Problem: Create an employee hierarchy.

Base class: Employee
- Attributes: name, id, base_salary
- Method: calculate_salary()

Child classes:
- FullTimeEmployee: salary = base_salary
- ContractEmployee: salary = base_salary * hours_worked
- Manager (inherits FullTimeEmployee): salary = base_salary + bonus

Why this matters: Demonstrates inheritance and method overriding. Real systems often have entity hierarchies.

Technical note: Each class overrides calculate_salary() differently - this is polymorphism in action.
```

#### Day 5-6: Special Methods and Properties

**Concepts to Learn:**
- `__str__` and `__repr__`
- `__len__`, `__getitem__`, `__setitem__`
- `@property` decorator
- Getters and setters
- `__eq__`, `__lt__` for comparisons

**Architecture Insight:**
Special methods (dunder methods) let your objects behave like built-in types. This makes your code more intuitive - you can use `len(my_object)` instead of `my_object.length()`.

**Exercise 2.4 - Custom List Class**
```
Problem: Create a SmartList class that extends list functionality.

Features:
- Track how many times items are added/removed
- Implement __len__, __getitem__, __str__
- Add method: get_stats() returning usage statistics

Why this matters: Understanding special methods is crucial for writing Pythonic code. Interviewers love asking about these.
```

#### Day 7: OOP Practice Project

**Project: Library Management System**
```
Build a complete system with:

Classes needed:
- Book (title, author, isbn, available)
- Member (name, member_id, borrowed_books)
- Library (books collection, members collection)

Features:
- Add/remove books and members
- Borrow/return books
- Search books by author/title
- View member borrowing history

Technical architecture:
- Library uses composition (has-a relationship with Books and Members)
- Use property decorators for encapsulation
- Implement __str__ for readable output
- Use class methods for factory patterns if time permits

This is similar to real interview take-home assignments.
```

---

### Week 3: File Handling, Exceptions & Modules

#### Day 1-2: File I/O Operations

**Concepts to Learn:**
- Reading files: read(), readline(), readlines()
- Writing files: write(), writelines()
- Context managers (with statement)
- File modes: 'r', 'w', 'a', 'r+', 'b'
- Working with CSV files
- JSON serialization

**Architecture Insight:**
The `with` statement ensures files are properly closed even if errors occur. This is Python's context manager protocol - it prevents resource leaks. Always use `with` for file operations in production code.

**Exercise 3.1 - Log File Analyzer**
```
Problem: Parse a log file and extract insights.

Given a log file format:
2024-01-15 10:23:45 ERROR Database connection failed
2024-01-15 10:24:12 INFO User logged in
2024-01-15 10:25:33 WARNING High memory usage

Tasks:
- Count errors, warnings, info messages
- Find most common error message
- List all errors with timestamps

Why this matters: Log analysis is extremely common in real jobs. File processing is essential.

Technical note: Use context managers, string methods (split), and dictionaries for counting.
```

**Exercise 3.2 - CSV Data Processor**
```
Problem: Read a CSV of sales data and generate report.

CSV format: date,product,quantity,price

Tasks:
- Calculate total revenue
- Find best-selling product
- Generate monthly summary
- Write results to new CSV

Why this matters: CSV is ubiquitous in data processing. Many junior roles involve data manipulation.

Technical architecture: Use csv module (not just split) because it handles edge cases (commas in fields, quotes, etc.)
```

#### Day 3-4: Exception Handling

**Concepts to Learn:**
- try/except/else/finally blocks
- Common built-in exceptions
- Raising exceptions
- Creating custom exceptions
- Exception hierarchy
- Best practices: catch specific exceptions, not bare except

**Architecture Insight:**
Exceptions are for exceptional situations, not regular control flow. Use them when something unexpected happens (file not found, network error), not for normal program logic.

**Exercise 3.3 - Robust Calculator**
```
Problem: Build a calculator that handles all error cases.

Operations: add, subtract, multiply, divide

Must handle:
- Division by zero
- Invalid input (non-numbers)
- Invalid operations
- Empty input

Why this matters: Error handling is critical in production. Unhandled exceptions crash programs.

Technical note: Use specific exceptions (ValueError, ZeroDivisionError), provide helpful error messages.
```

**Exercise 3.4 - Configuration File Reader**
```
Problem: Read application configuration from file with error handling.

Expected config format (JSON):
{
  "database": "postgres",
  "port": 5432,
  "timeout": 30
}

Handle:
- File not found
- Invalid JSON
- Missing required fields
- Invalid data types

Provide default values for optional fields.

Why this matters: Config reading is common in real applications. Shows you understand defensive programming.
```

#### Day 5-6: Modules and Packages

**Concepts to Learn:**
- Importing modules (import, from...import)
- Creating your own modules
- `__name__ == "__main__"` pattern
- Package structure
- Common standard library modules: os, sys, datetime, random, collections

**Architecture Insight:**
Modules organize code into logical units. Large applications are split into multiple files/packages. Understanding imports is crucial for working on real codebases.

**Exercise 3.5 - Utility Module Creation**
```
Problem: Create a reusable utilities module.

Create file: myutils.py with:
- String utilities: capitalize_words(), reverse_string()
- Math utilities: is_prime(), factorial()
- Date utilities: days_until(), format_date()

Then import and use in main.py

Why this matters: Real projects have utility modules. Shows you understand code organization.

Technical note: Add docstrings to all functions. Use if __name__ == "__main__" for testing.
```

#### Day 7: Integration Project

**Project: Personal Task Manager with Persistence**
```
Build a task manager that saves to files:

Features:
- Add/remove/complete tasks
- Save tasks to JSON file
- Load tasks on startup
- Handle all file errors gracefully
- Generate statistics report (save to CSV)

Technical architecture:
- Task class for data structure
- TaskManager class for business logic
- Separate file_handler module for I/O operations
- Use exception handling throughout
- Implement proper logging

This demonstrates:
- OOP design
- File persistence
- Error handling
- Module organization
```

---

### Week 4: Advanced Python Concepts

#### Day 1-2: Iterators and Generators

**Concepts to Learn:**
- Iterator protocol (__iter__, __next__)
- Generator functions (yield)
- Generator expressions
- Benefits: memory efficiency, lazy evaluation

**Architecture Insight:**
Generators are memory-efficient - they generate values on-demand rather than storing everything in memory. Critical for processing large datasets. This is a key Pythonic pattern.

**Exercise 4.1 - Fibonacci Generator**
```
Problem: Create a generator that yields Fibonacci numbers.

Requirements:
- Infinite sequence (no predetermined end)
- Memory efficient (don't store all numbers)
- Compare with regular function that returns list

Why this matters: Common interview question. Tests understanding of generators vs lists.

Technical explanation:
- yield vs return: yield maintains state between calls
- Generator uses constant memory regardless of how many numbers generated
- List approach would consume unbounded memory
```

**Exercise 4.2 - File Line Iterator**
```
Problem: Create a generator that reads large files line by line.

Features:
- Yield lines one at a time
- Filter lines by pattern
- Count processed lines

Why this matters: Real files can be gigabytes. Loading entire file crashes program. Generators solve this.

Compare memory usage: generator vs reading entire file.
```

#### Day 3-4: Decorators

**Concepts to Learn:**
- Function decorators
- Wrapper functions
- @wraps from functools
- Common use cases: timing, logging, authentication
- Multiple decorators

**Architecture Insight:**
Decorators add functionality to functions without modifying their code. This is the Open/Closed Principle - open for extension, closed for modification. Used extensively in web frameworks (Flask, Django).

**Exercise 4.3 - Timing Decorator**
```
Problem: Create a decorator that measures function execution time.

Usage:
@timing_decorator
def slow_function():
    # some code

Should print: "slow_function took 2.34 seconds"

Why this matters: Performance monitoring is crucial. Decorators are elegant solution.

Technical note: Use time.time() before/after. Preserve function metadata with @wraps.
```

**Exercise 4.4 - Caching Decorator**
```
Problem: Create a decorator that caches function results.

Example: expensive_calculation(5) called twice should compute once.

Why this matters: Common optimization technique. Tests understanding of closures and dictionaries.

Technical note: This is simplified version of functools.lru_cache.
```

#### Day 5-6: Lambda Functions and Functional Programming

**Concepts to Learn:**
- Lambda syntax
- map(), filter(), reduce()
- List/dict/set comprehensions (advanced)
- any(), all() functions
- sorted() with key parameter

**Architecture Insight:**
Functional programming treats computation as evaluation of functions. Python is multi-paradigm - supports both OOP and functional styles. Modern Python favors comprehensions over map/filter.

**Exercise 4.5 - Data Transformation Pipeline**
```
Problem: Process a list of user dictionaries.

Data: [{'name': 'Alice', 'age': 30, 'salary': 50000}, ...]

Tasks using functional approach:
- Filter users over age 25
- Calculate average salary
- Sort by name
- Transform to list of formatted strings

Do each task with:
1. Lambda + filter/map/sorted
2. List comprehension
Compare readability.

Why this matters: Data transformation is common. Interview tests multiple approaches.
```

#### Day 7: Review & Practice

**Comprehensive Coding Challenges:**

1. **Implement a Custom Range**
   - Create iterator class that mimics range()
   - Support start, stop, step parameters

2. **Context Manager**
   - Create a Timer context manager
   - Usage: with Timer(): <code>
   - Prints elapsed time automatically

3. **Decorator Chain**
   - Create multiple decorators (auth, logging, timing)
   - Apply to same function
   - Understand execution order

---

## Phase 2: Problem Solving & Algorithms (Weeks 5-8)

### Week 5: Data Structures Fundamentals

#### Day 1-2: Arrays and Strings

**Concepts to Learn:**
- Two-pointer technique
- Sliding window pattern
- String manipulation algorithms
- In-place operations
- Time complexity analysis

**Architecture Insight:**
Arrays (lists in Python) have O(1) index access but O(n) insertion/deletion in middle. Understanding these tradeoffs helps you choose right data structure and optimize algorithms.

**Exercise 5.1 - Two Sum Problem**
```
Problem: Find two numbers in array that sum to target.

Input: [2, 7, 11, 15], target = 9
Output: [0, 1] (indices of 2 and 7)

Solution approaches:
1. Brute force: O(n²) - check every pair
2. Hash map: O(n) - single pass with dictionary

Why this matters: Extremely common interview question. Teaches hash map optimization pattern.

Technical explanation:
- Brute force uses nested loops
- Hash map stores complements: for each num, check if (target - num) exists
- Space-time tradeoff: use more space (dictionary) for better time
```

**Exercise 5.2 - Palindrome Check**
```
Problem: Check if string is palindrome (reads same forwards/backwards).

Approaches:
1. Reverse and compare: O(n) time, O(n) space
2. Two pointers: O(n) time, O(1) space

Variations:
- Ignore spaces and punctuation
- Case-insensitive
- Alphanumeric characters only

Why this matters: Tests string manipulation and optimization thinking.
```

**Exercise 5.3 - Sliding Window Maximum**
```
Problem: Find maximum in each sliding window of size k.

Input: [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]

Why this matters: Sliding window is crucial pattern for many problems.

Technical explanation:
- Naive: O(n*k) - check max in each window
- Optimized: O(n) - use deque to track potential maximums
```

#### Day 3-4: Linked Lists

**Concepts to Learn:**
- Node structure
- Singly vs doubly linked lists
- Common operations: insert, delete, reverse
- Runner technique (fast/slow pointers)

**Architecture Insight:**
Unlike arrays, linked lists have O(1) insertion/deletion but O(n) access. They're used when you need efficient insertion/deletion in middle. Understanding when to use lists vs arrays is important.

**Exercise 5.4 - Implement Linked List**
```
Problem: Create LinkedList class from scratch.

Node class:
- value
- next pointer

LinkedList class:
- append(value)
- prepend(value)
- delete(value)
- find(value)
- reverse()
- print_list()

Why this matters: Shows you understand pointers and memory. Common interview ask.

Technical note: In Python, "pointers" are object references. Draw diagrams to visualize.
```

**Exercise 5.5 - Detect Cycle**
```
Problem: Detect if linked list has a cycle.

Approach: Floyd's cycle detection (tortoise and hare)
- Two pointers: slow (moves 1 step), fast (moves 2 steps)
- If they meet, cycle exists

Why this matters: Classic algorithm. Tests understanding of two-pointer technique.

Technical explanation:
- If no cycle: fast reaches end
- If cycle: fast catches up to slow (like running on circular track)
```

#### Day 5-6: Stacks and Queues

**Concepts to Learn:**
- Stack (LIFO): push, pop, peek
- Queue (FIFO): enqueue, dequeue
- Implementation using lists/deque
- Common applications

**Architecture Insight:**
Stacks: function call stack, undo/redo, parsing expressions
Queues: task scheduling, breadth-first search, message queuing
These aren't just academic - they power real systems.

**Exercise 5.6 - Valid Parentheses**
```
Problem: Check if parentheses string is valid.

Input: "({[]})" → True
Input: "([)]" → False

Approach: Use stack
- Push opening brackets
- Pop and match closing brackets

Why this matters: Classic stack problem. Tests pattern recognition.

Technical explanation:
- Stack perfect for nested structures
- Last opened must be first closed (LIFO matches requirement)
```

**Exercise 5.7 - Implement Queue Using Stacks**
```
Problem: Implement queue using only two stacks.

Why this matters: Tests deep understanding of data structure properties.

Technical explanation:
- Stack1 for enqueue
- Stack2 for dequeue
- Amortized O(1) for all operations
- This illustrates how you can build one structure from another
```

#### Day 7: Practice Problems

**Challenge Set:**
1. Reverse linked list
2. Merge two sorted lists
3. Implement min stack (getMin in O(1))
4. Evaluate reverse Polish notation

---

### Week 6: Recursion and Sorting

#### Day 1-3: Recursion

**Concepts to Learn:**
- Base case and recursive case
- Call stack visualization
- Recursion vs iteration
- Tail recursion
- Common pitfalls: infinite recursion, stack overflow

**Architecture Insight:**
Recursion breaks problems into smaller identical problems. It's elegant but uses stack memory. Some problems are naturally recursive (trees, graphs). Understanding recursion is essential for advanced algorithms.

**Exercise 6.1 - Factorial and Fibonacci**
```
Problem: Implement both recursively and iteratively.

Compare:
- Code simplicity
- Performance
- Memory usage

Why this matters: Understand tradeoffs between recursion and iteration.

Technical explanation:
- Recursive Fibonacci: O(2^n) - exponential due to repeated calculations
- Iterative: O(n) - linear
- Memoization can optimize recursive to O(n)
```

**Exercise 6.2 - Power Function**
```
Problem: Calculate x^n efficiently.

Naive: O(n) - multiply x, n times
Optimized: O(log n) - divide and conquer

Algorithm:
- x^n = (x^(n/2))^2 if n even
- x^n = x * (x^(n/2))^2 if n odd

Why this matters: Classic divide-and-conquer. Common in interviews.
```

**Exercise 6.3 - Generate Permutations**
```
Problem: Generate all permutations of list.

Input: [1, 2, 3]
Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

Approach: Recursive backtracking

Why this matters: Backtracking is powerful technique for combinatorial problems.

Technical explanation:
- Fix first element, permute rest
- Recursively permute smaller lists
- Base case: empty list has one permutation (itself)
```

#### Day 4-6: Sorting Algorithms

**Concepts to Learn:**
- Bubble sort, selection sort, insertion sort: O(n²)
- Merge sort, quick sort: O(n log n)
- When to use each
- Stability in sorting
- In-place vs out-of-place

**Architecture Insight:**
Python's built-in sort uses Timsort (hybrid of merge sort and insertion sort). Understanding sorting algorithms teaches divide-and-conquer and helps you analyze any algorithm's complexity.

**Exercise 6.4 - Implement Merge Sort**
```
Problem: Implement merge sort from scratch.

Steps:
1. Divide list in half (recursively)
2. Sort each half
3. Merge sorted halves

Why this matters: Merge sort is reliable O(n log n). Understanding it teaches recursion and divide-and-conquer.

Technical explanation:
- Divide: O(log n) levels of recursion
- Merge: O(n) at each level
- Total: O(n log n)
- Space: O(n) for temporary arrays
```

**Exercise 6.5 - Quick Sort**
```
Problem: Implement quicksort.

Steps:
1. Choose pivot
2. Partition: smaller left, larger right
3. Recursively sort partitions

Why this matters: Very common interview question. Faster in practice than merge sort.

Technical explanation:
- Average: O(n log n)
- Worst case: O(n²) if bad pivot choices
- In-place: O(log n) space for recursion stack
```

#### Day 7: Sorting Practice

**Problems:**
1. Sort array of 0s, 1s, 2s (Dutch national flag)
2. Find kth largest element
3. Merge k sorted arrays
4. Sort array by frequency of elements

---

### Week 7: Hash Tables and Trees (Basics)

#### Day 1-3: Hash Tables (Dictionaries)

**Concepts to Learn:**
- Hash function concept
- Collision handling
- Time complexity: O(1) average
- Applications: caching, counting, grouping

**Architecture Insight:**
Hash tables trade space for speed. They're fundamental to database indexing, caching systems, and more. Python dicts are highly optimized hash tables.

**Exercise 7.1 - Two Sum (revisited)**
```
Now explain the hash map solution in detail:

for num in array:
    complement = target - num
    if complement in seen:
        return [seen[complement], current_index]
    seen[num] = current_index

Technical breakdown:
- seen dictionary maps values to indices
- "in" operator on dict is O(1) hash lookup
- Single pass through array: O(n) total
- This is space-time tradeoff: O(n) space for O(n) time
```

**Exercise 7.2 - Group Anagrams**
```
Problem: Group strings that are anagrams.

Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

Approach: Use sorted string as hash key

Why this matters: Classic hash table grouping problem.

Technical explanation:
- Anagrams have same characters, different order
- sorted("eat") = "aet" = sorted("tea")
- Use sorted string as dictionary key
- Group words with same key
```

**Exercise 7.3 - First Non-Repeating Character**
```
Problem: Find first character that appears only once.

Input: "leetcode" → "l"
Input: "loveleetcode" → "v"

Approach: Two passes with hash map
1. Count frequency of each character
2. Find first with count == 1

Why this matters: Tests understanding of hash map counting pattern.
```

#### Day 4-6: Binary Trees (Introduction)

**Concepts to Learn:**
- Tree terminology: root, leaf, parent, child
- Binary tree structure
- Tree traversals: inorder, preorder, postorder, level-order
- Depth-first search (DFS) vs breadth-first search (BFS)

**Architecture Insight:**
Trees represent hierarchical data: file systems, organizational charts, HTML DOM. Understanding tree traversal is foundation for more complex algorithms.

**Exercise 7.4 - Implement Binary Tree**
```
Create TreeNode and BinaryTree classes:

TreeNode:
- value
- left child
- right child

BinaryTree:
- insert(value)
- search(value)
- height()
- count_nodes()

Why this matters: Foundation for more complex tree problems.
```

**Exercise 7.5 - Tree Traversals**
```
Implement all traversals:

Inorder (Left, Root, Right):
- Visits nodes in sorted order for BST

Preorder (Root, Left, Right):
- Useful for copying tree

Postorder (Left, Right, Root):
- Useful for deleting tree

Level-order (BFS):
- Visit level by level
- Use queue

Why this matters: Each traversal has specific use cases. Must know all.

Technical explanation:
- DFS traversals use recursion (or stack)
- BFS uses queue
- Space: O(h) for DFS, O(w) for BFS (h=height, w=max width)
```

**Exercise 7.6 - Binary Tree Problems**
```
Solve:
1. Maximum depth of tree
2. Check if tree is balanced
3. Find path sum
4. Lowest common ancestor

These test recursion and tree traversal understanding.
```

#### Day 7: Combined Practice

**Project: Build a Simple In-Memory Database**
```
Features:
- Store key-value pairs (hash table)
- Support transactions (stack for undo)
- Query by prefix (tree/trie structure)

This combines multiple data structures for real-world-like system.
```

---

### Week 8: Problem-Solving Patterns

#### Day 1-2: Two Pointers Pattern

**Concepts:**
- When to use: sorted arrays, linked lists
- Variations: same direction, opposite directions
- Common problems: pair finding, removing duplicates

**Problems:**
1. Container with most water
2. Three sum
3. Remove duplicates from sorted array
4. Trapping rain water (harder)

#### Day 3-4: Sliding Window Pattern

**Concepts:**
- Fixed size window
- Dynamic window
- When to expand/shrink window

**Problems:**
1. Maximum sum subarray of size k
2. Longest substring without repeating characters
3. Minimum window substring
4. Longest substring with k distinct characters

#### Day 5-6: Fast and Slow Pointers

**Concepts:**
- Cycle detection
- Finding middle
- Linked list problems

**Problems:**
1. Linked list cycle
2. Happy number
3. Middle of linked list
4. Palindrome linked list

#### Day 7: Mixed Practice

**Complete 5-10 problems mixing all patterns learned**

---

## Phase 3: Interview Preparation (Weeks 9-12)

### Week 9: Coding Interview Simulation

#### Daily Structure:
- Morning: Timed problem solving (2 problems, 45 min each)
- Afternoon: Review solutions, learn optimal approaches
- Evening: Watch interview videos, learn communication techniques

**Topics to Cover:**
- Arrays and strings (Day 1-2)
- Linked lists and stacks (Day 3)
- Trees and graphs basics (Day 4-5)
- Dynamic programming intro (Day 6-7)

### Week 10: System Design Basics (Junior Level)

**Concepts:**
- Client-server architecture
- REST APIs basics
- Databases: SQL vs NoSQL basics
- Caching concepts
- How web applications work

**Simple Design Questions:**
- Design URL shortener
- Design simple chat application
- Design file storage system

### Week 11: Python-Specific Topics

#### Day 1-2: Testing
- unittest framework
- pytest basics
- Writing test cases
- Test-driven development concept

#### Day 3-4: Virtual Environments & Packages
- pip and package management
- requirements.txt
- Virtual environments (venv)
- Basic project structure

#### Day 5-6: Common Libraries
- requests (HTTP)
- datetime
- collections (Counter, defaultdict)
- itertools
- json

#### Day 7: Code Quality
- PEP 8