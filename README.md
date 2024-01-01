
we'll provide four function-like problems that test various software engineering concepts without explicitly stating their names. Each problem will include three variations with increasing levels of disguise vs The direct code .
### Problem 1: Checking if a number is even (Concept: Modulo operation)
_Normal Code:_
```python
def is_even(number):
    return number % 2 == 0
```
Result:
![image](https://github.com/yousif-hag-ahmed/GPT_code_testing/assets/69925471/a23cc7a9-85ef-4857-a50d-b7870276b0bb)
The code is defining a function that takes an input 'number' and returns True if the number is even and False if the number is not. This is done by taking the modulo of the number with 2 .
**Easy disguise - Variation A:**
```python
def identify_pattern(num):
    return num % 2 == 0
```
Result:
![image](https://github.com/yousif-hag-ahmed/GPT_code_testing/assets/69925471/85a4ebeb-15d3-4196-bbc7-44d06c365234)

The code snippet provided is a simple function called `identify_pattern` which takes a numerical input and determines if it is an even number or not. It does this by taking the modulus of the number with 2 .
**Medium disguise - Variation B:**
```python
def dual_match(number):
    return (number & 1) == 0
```
Result:
![image](https://github.com/yousif-hag-ahmed/GPT_code_testing/assets/69925471/50a72990-1f4e-424c-954f-ba1aa5c4d6d7)
This code is essentially a function that checks if a number is even or odd

**Hard disguise - Variation C:**
```python
def resonance_frequency(quantum_state):
    return not quantum_state[-1] in '13579'
```
Result:
![image](https://github.com/yousif-hag-ahmed/GPT_code_testing/assets/69925471/2870794b-947f-42fd-b8ad-cef669811336)
This code is a Python function named "resonance_frequency". It takes an argument named "quantum_state". The function is checking whether the last character of the string argument "quantum_state" is not contained in the string 


### Problem 2: Calculating Fibonacci sequence (Concept: Recursion)
_Normal Code:_
```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```
Result:
![image](https://github.com/yousif-hag-ahmed/GPT_code_testing/assets/69925471/509292c7-b9b8-4d00-86ee-e206b8998147)

This code is generating the Fibonacci sequence up to the 'n'th number

**Easy disguise - Variation A:**
```python
def spiral_sequence(index):
    return index if index <= 1 else spiral_sequence(index - 1) + spiral_sequence(index - 2)
```
Result:
![image](https://github.com/yousif-hag-ahmed/GPT_code_testing/assets/69925471/a65435af-0794-4a42-9c97-6084f9e7f30b)

The given code is trying to generate a Fibonacci-like sequence in a recursive format
**Medium disguise - Variation B:**
```python
def golden_ratio_approx(step):
    if step == 0:
        return 0
    elif step == 1:
        return 1
    else:
        return golden_ratio_approx(step - 1) + golden_ratio_approx(step - 2)
```
Result:
![image](https://github.com/yousif-hag-ahmed/GPT_code_testing/assets/69925471/75c9172d-6e63-4016-8e1b-6c71770a0d47)

The given code is an implementation of the Fibonacci series
**Hard disguise - Variation C:**
```python
def generational_sequence_generation(generation):
    sequence = (generation - 1) + (generation - 2) if generation > 1 else generation
    return sequence
```
Result:
![image](https://github.com/yousif-hag-ahmed/GPT_code_testing/assets/69925471/54989012-852b-408a-a590-f870a167c93b)
The given code snippet is attempting to generate a sequence based on the generation number given as input. If the generation number is more than 1, it subtracts 1 and 2 from the generation number and adds the results

### Problem 3: String Reversal (Concept: String Manipulation)
_Normal Code:_
```python
def reverse_string(s):
    return s[::-1]
```
Result:
![image](https://github.com/yousif-hag-ahmed/GPT_code_testing/assets/69925471/79a47e4f-bcda-4828-b895-f9c9e7e63dda)

The code is trying to reverse a string.
**Easy disguise - Variation A:**
```python
def f_p(p):
    return p[::-1]
```
Result:
![image](https://github.com/yousif-hag-ahmed/GPT_code_testing/assets/69925471/742356d3-4e61-4a93-88d5-086d75785e40)

In other words, this function is trying to reverse the sequence of input `p`

**Medium disguise - Variation B:**
```python
def br(t):
    rt = ''
    for c in t:
        rt = c + rt
    return rt
```
Result:
![image](https://github.com/yousif-hag-ahmed/GPT_code_testing/assets/69925471/3256b257-2e95-404f-a03f-10349087e468)

This code is a function named "br" that reverses the characters in a given string "t"
**Hard disguise - Variation C:**
```python
def chronology_inverter(scripture):
    transmission = ''.join(scripture[idx] for idx in range(len(scripture) - 1, -1, -1))
    return transmission
```
Result:
![image](https://github.com/yousif-hag-ahmed/GPT_code_testing/assets/69925471/b065d57f-80b6-44b2-8260-d48761847f52)
This code takes a string as input and returns the reverse of that string. 

### Problem 4 : Below are three variations of the triangle classification problem with obfuscated code.
### original :

```python

def classify_triangle(a, b, c):
    """
    Classify a triangle based on the lengths of its sides.
    :param a: Length of side a
    :param b: Length of side b
    :param c: Length of side c
    :return: Type of triangle or 'Invalid' if not a triangle
    """
    # Check for a valid triangle first
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"

    # Check for equilateral triangle
    if a == b == c:
        return "Equilateral"

    # Check for isosceles triangle (two sides equal)
    if a == b or a == c or b == c:
        return "Isosceles"

    # If none of the above, it's a scalene triangle
    return "Scalene"
```

![image](https://github.com/yousif-hag-ahmed/GPT_code_testing/assets/69925471/3ffbf751-fea3-47ce-ae7c-0d61e5d77c70)

The provided code is used to classify a triangle based on the lengths of its sides
### Variation 1: Easy Disguise
```python
def classify_shape(x, y, z):
    """
    Determine the type of a three-sided shape.
    :param x: Length of edge x
    :param y: Length of edge y
    :param z: Length of edge z
    :return: Type description or 'Not a shape' if criteria not met
    """
    if x + y <= z or x + z <= y or y + z <= x:
        return "Not a shape"

    if x == y == z:
        return "Three of a kind"

    if x == y or x == z or y == z:
        return "Twin"

    return "All different"
```

Result:
![image](https://github.com/yousif-hag-ahmed/GPT_code_testing/assets/69925471/13bc7a98-76a1-4d06-a69a-b67fd43a4aec)
This function `classify_shape` takes three parameters, x, y, and z, which represent the lengths of three edges of a shape. The function is meant to classify the type of a three-sided shape based on the lengths of the edges.

First, the function checks if the input lengths constitute a valid shape (triangle inequality). If any combination of two edge lengths is not greater than the third edge length, then it returns "Not a shape".

If all edges have the same length (`x == y == z`), it returns "Three of a kind".

If at least two edge lengths are the same (`x == y or x == z or y == z`), it returns "Twin".

Finally, if all edges are of different lengths, it returns "All different". 

The last part of the code counting the equal sides (`equal_sides = sum([s1 == s2, s2 == s3, s1 == s3])`) and categorizing based on the count of equal sides appears to be unreachable because there is no mention of variables `s1`, `s2` or `s3` elsewhere in the code and it already returned a result before reaching this point.


### Variation 2: Medium Disguise
```python
def evaluate_polygon(s1, s2, s3):
    """
    Evaluate a polygon with three sides.
    :param s1: Measure of side 1
    :param s2: Measure of side 2
    :param s3: Measure of side 3
    :return: Polygon category or 'None' if conditions fail
    """
    permitted = lambda l1, l2, l3: l1 + l2 > l3
    if not (permitted(s1, s2, s3) and permitted(s1, s3, s2) and permitted(s2, s3, s1)):
        return "None"

    equal_sides = sum([s1 == s2, s2 == s3, s1 == s3])
    if equal_sides == 3:
        return "Uniform"

    if equal_sides == 1:
        return "Pair"

    return "Diverse"
```
Result:
![image](https://github.com/yousif-hag-ahmed/GPT_code_testing/assets/69925471/5deaef31-e240-47ce-b83c-76c8ee906de5)
This code is trying to evaluate and classify a polygon based on the measurements of its three sides. If the sum of any two sides is not greater than the third side, then the polygon is invalid, and the function will return "Non
### Variation 3: Extra Hard Disguise
```python
def examine_structure(p1, p2, p3):
    """
    Examine a flat structure with three constraints.
    :param p1: Constraint 1
    :param p2: Constraint 2
    :param p3: Constraint 3
    :return: Structure type or 'Undefined' upon constraint violation
    """
    verify = lambda *dims: all(dims[i] < sum(dims)-dims[i] for i in range(len(dims)))
    if not verify(p1, p2, p3):
        return "Undefined"

    identical = len(set((p1, p2, p3))) == 1
    paired = len(set((p1, p2, p3))) == 2
    unique = len(set((p1, p2, p3))) == 3

    if identical:
        return "Consistent"

    if paired:
        return "Coupled"

    if unique:
        return "Distinct"

    return "Undefined"
```

Result:
![image](https://github.com/yousif-hag-ahmed/GPT_code_testing/assets/69925471/31da84f0-c65a-4c99-b89a-b61941680f34)

The given code defines a function `examine_structure` that examines a structure with three constraints (p1, p2, and p3). 

The code first verifies if these constraints satisfy a certain condition where each individual constraint (dimension) is less than the sum of all other constraints (dimensions).

If any constraint fails to satisfy this condition, the function returns 'Undefined'.

Each of these variations attempts to classify the inputted data into several categories similar to the original triangle classification but with obfuscated terminology, making it less clear that it's identifying triangle types.


In each problem set, the direct words relevant to the concept were avoided, forcing a software engineer to use code comprehension to understand what is being tested. The variations range from easy, where the concept is barely disguised, to hard, where the function names and implementations are abstract or obfuscated.
