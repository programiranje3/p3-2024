"""Demonstrates working with strings in Python.
"""


#%%
def demonstrate_formatting():
    """Demonstrating details of string formatting.
    - using classical formatting
    - \n is the new line char
    - r'...' - raw formatting
    - using \"\"\"...\"\"\" for multi-line formatting
    - string "multiplication"
    - substrings / slicing
    - str() vs. repr() (usually the same, but with whitespace there is a difference)
    """


#%%
# Test demonstrate_formatting()
demonstrate_formatting()

#%%


def demonstrate_fancy_formatting():
    """Using "fancy" formatting.
    - format strings like '{0}{1} {2}', '{0}{1} {2}, {3}', etc.
    """

    print('This is {} and {} have toured {}.'.format(2024, 'Green Day', 'Europe'))


#%%
# Test demonstrate_fancy_formatting()
demonstrate_fancy_formatting()

#%%


def demonstrate_fancy_formatting_with_f_strings():
    """Using f-strings in formatting.
    - format strings like f'Some text {some var}, more text {another var}...', etc.
    """

    print(f'The value of 2+3 is {2 + 3}.')


#%%
# Test demonstrate_fancy_formatting_with_f_strings()
demonstrate_fancy_formatting_with_f_strings()

#%%


def demonstrate_string_operations():
    """Using different string operations.
    - endswith(), split(), center(), in (aka contains()), == (aka equals()), len(), ..., strip() (lstrip(), rstrip())
    """

    print('Green Day'.endswith('Day'))
    print('Green Day'.split())
    print('Day' in 'Green Day')
    print('Green Day'.center(20, '*'))
    print('    Green Day'.lstrip())
    print('    Green Day'.strip())
    print('    Green Day**'.rstrip('*'))


#%%
# Test demonstrate_string_operations()
demonstrate_string_operations()
