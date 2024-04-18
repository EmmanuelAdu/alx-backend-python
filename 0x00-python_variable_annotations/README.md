Tasks
0. Basic annotations - add
mandatory
Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.

bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__)

bob@dylan:~$ ./0-main.py
True
{'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}

1. Basic annotations - concat
mandatory
Write a type-annotated function concat that takes a string str1 and a string str2 as arguments and returns a concatenated string

bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3
concat = __import__('1-concat').concat

str1 = "egg"
str2 = "shell"

print(concat(str1, str2) == "{}{}".format(str1, str2))
print(concat.__annotations__)

bob@dylan:~$ ./1-main.py
True
{'str1': <class 'str'>, 'str2': <class 'str'>, 'return': <class 'str'>}

2. Basic annotations - floor
mandatory
Write a type-annotated function floor which takes a float n as argument and returns the floor of the float.

3. Basic annotations - to string
mandatory
Write a type-annotated function to_str that takes a float n as argument and returns the string representation of the float.

4. Define variables
mandatory
Define and annotate the following variables with the specified values:

a, an integer with a value of 1
pi, a float with a value of 3.14
i_understand_annotations, a boolean with a value of True
school, a string with a value of “Holberton”

5. Complex types - list of floats
mandatory
Write a type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float.

6. Complex types - mixed list
mandatory
Write a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float.

7. Complex types - string and int/float to tuple
mandatory
Write a type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple. The first element of the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float.

8. Complex types - functions
mandatory
Write a type-annotated function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier.

9. Let's duck type an iterable object
mandatory
Annotate the below function’s parameters and return values with the appropriate types

def element_length(lst):
    return [(i, len(i)) for i in lst]

10. Duck typing - first element of a sequence
#advanced
Augment the following code with the correct duck-typed annotations:

# The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None

11. More involved type annotations
#advanced
Given the parameters and the return values, add type annotations to the function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default

12. Type Checking
#advanced
Use mypy to validate the following piece of code and apply any necessary changes.

def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
