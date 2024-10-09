"""Demonstrates peculiarities of if, for, while and other statements.
"""


#%%
def demonstrate_branching():
    """Details and peculiarities of if statements.
    - is compares id()'s, == compares contents
    - id()'s are the same for equal strings and numbers, but not for lists, user class instances,...
    - the condition of an if-statement need not necessarily be a boolean
    - there can be more than one elif after if (no switch statement, use multiple elif instead)
    """

    from datetime import date
    d1 = date.today()
    d2 = date(2024, 6, 19)

    if d1 != d2:
        print('d1 != d2')
    else:
        print('d1 == d2')
    print()

    if []:
        print(True)
    else:
        print(False)
    print()

    if []:
        print(True)
    elif 3:
        print(3)
    elif 0.0:
        print(True)
    else:
        print('...')


#%%
# Test demonstrate_branching()
demonstrate_branching()

#%%


def demonstrate_loops():
    """Different kinds of loops. Also break and continue.
    - it is not necessary to iterate through all elements of an iterable
    - step in range()
    - unimportant counter (_)
    - break and continue
    - while loop
    """

    for i in range(2, 20, 3):
        print(i)
    print()

    for _ in range(3):
        print('Green Day')
    print()

    for i in range(2, 20, 3):
        if i == 5:
            break
        print(i)
    print()

    i = 4
    while i:
        print(i)
        i -= 1


#%%
# Test demonstrate_loops()
demonstrate_loops()
