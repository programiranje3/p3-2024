"""Demonstrates working with lists.
"""


#%%
def demonstrate_lists():
    """Using just the simplest operations with lists.
    - create a non-empty list with different kinds of elements
    - accessing/slicing a list
    - comparing 2 lists (== vs. is)
    - concatenating 2 lists (the + operator)
    - looping through a list
    """

    green_day = ['Green Day', 1987, 'Rodeo, CA', True]
    print(green_day[0])
    print(green_day[1:3])
    print(green_day[1:])
    print(green_day[:-2])
    print(green_day[-2])


#%%
# Test demonstrate_lists()
demonstrate_lists()


#%%
def demonstrate_list_methods():
    """Using
    append()
    insert()
    remove()
    pop()
    extend()
    count()
    index()
    reverse()
    len()
    ...
    Also, "in" and "not in" operators can be used to search lists
    for the occurrence of a given element.
    """

    green_day = ['Green Day', 1987, 'Rodeo, CA', True]
    green_day.append('Billy Joe Armstrong')
    print(green_day)
    green_day.remove('Rodeo, CA')
    print(green_day)
    green_day.insert(2, 'Mike Dirnt')
    print(green_day)
    # green_day = green_day + ['Tre Cool']
    green_day.extend(['Tre Cool'])
    print(green_day)


#%%
# Test demonstrate_list_methods()
demonstrate_list_methods()

#%%


def populate_empty_list():
    """Creating an empty list and populating it with random values
    using random.seed() and random.randint()
    """

    from random import randint, seed
    seed(12)
    l = []
    for i in range(4):
        l.append(randint(1, 10))
    print(l)


#%%
# Test populate_empty_list()
populate_empty_list()

#%%


def duplicate_list():
    """Duplicating lists (carefully :)).
    Don't use l2 = l1, but either of the following:
    - l2 = l1.copy()
    - l2 = l1 + []
    - l2 = l1[:]
    """
    green_day = ['Green Day', 1987, 'Rodeo, CA', True]
    # gd = green_day.copy()
    gd = green_day[:]
    print(green_day == gd)


#%%
# Test duplicate_list()
duplicate_list()

#%%


def demonstrate_list_comprehension():
    """Showing examples of list comprehension.
    - list comprehension over a list of strings
    - list comprehension with enumerate(), to find indices of all occurrences of an element in a list
    Using str() and join() in printing results.
    """

    # songs = ['Hold On', 'Outlaws', 'Longview', 'I Was There', 'Dilemma', 'Ashley', 'You Lied']
    # # first_words = [words.split()[0] for words in songs]
    # # print(''.join([word[0] for word in first_words]))
    # # print(''.join([word[0] for word in first_words]).capitalize())
    # print(''.join([t[0] for t in songs]).capitalize())

    songs = ['Hold On', 'Outlaws', 'Longview', 'I Was There', 'Dilemma', 'Outlaws', 'Ashley', 'Outlaws', 'You Lied']
    print([i for i, j in enumerate(songs) if j == 'Outlaws'])


#%%
# Test demonstrate_list_comprehension()
demonstrate_list_comprehension()

