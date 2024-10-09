"""Demonstrates how operators and expressions work in Python.
"""

from settings import *


#%%
def demonstrate_arithmetic_operators():
    """Working with arithmetic operators.
    Arithmetic operators in Python are pretty much the same as in other programming languages.
    The integer division operator: //
    """

    print((3 * 2 - 21 % 4) // 3)


#%%
# Test demonstrate_arithmetic_operators()
demonstrate_arithmetic_operators()

#%%


def demonstrate_relational_operators():
    """Working with relational operators.
    - simple comparisons
    - comparing dates (== vs. is)
    - is compares id()'s, == compares contents
    - id()'s are the same for equal strings and numbers, but not for lists, user class instances,...
    - comparing dates (>, <, etc. with dates)
    - None in comparisons, type(None)
    """

    print(3 > 2)
    print(3 <= 2)
    print()

    from datetime import date
    d1 = date.today()
    d2 = date(2024, 6, 19)
    print(d2 > d1)
    print()

    d3 = date(2024, 6, 19)
    print(d3 == d2)
    print(d3 is d2)
    print()

    a = 2
    b = 2
    print(a is b)
    s1 = 'Green Day'
    s2 = 'Green Day'
    print(s1 is s2)
    print()

    print(type(d1))
    print(type(None))
    print(a is None)
    # print(d1 > None)
    print(d1 == None)


#%%
# Test demonstrate_relational_operators()
demonstrate_relational_operators()

#%%


def demonstrate_logical_operators():
    """Working with logical operators.
    - logical operations with True, False and None
    - logical operations with dates
        - make sure to read this: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not !!!
          (or just this: https://stackoverflow.com/questions/44612144/logical-operators-in-python)
    - logical operations with None (incl. None and int, None and date, etc.)
    - None and date vs. None > date
    """

    print(2 > 3 and True)
    print(2 > 1 and True)
    print(2 > 1 and 1)
    print()

    from datetime import date
    d1 = date.today()
    d2 = date(2024, 6, 19)
    print(d1 and d2)
    print(d1 and None)
    print(None and d1)


#%%
# Test demonstrate_logical_operators()
demonstrate_logical_operators()

