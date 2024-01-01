# GPT_code_testing
website that tests code using generative AI tools 
Below are three variations of the triangle classification problem with obfuscated code. I will rank them from easy to extra hard.
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
