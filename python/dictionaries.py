"""Demonstrates dictionaries.
From: https://qr.ae/TWCAvj:
Python uses dictionaries all over the place:
- the variables and functions in a module - stored in a dictionary  # can be shown using globals()
- the local variables in a function - stored in a dictionary        # can be shown using locals(); see functions.py
- the implementation of a function - a dictionary
- a class is a dictionary
- an instance of a class is another dictionary
- the modules your program has imported - you guessed it - another dictionary
- even Python set objects are implemented as modified dictionaries
To paraphrase Tim Peter's 'Zen of Python': "dictionaries are great - let's do more of them".
Read more at https://qr.ae/TWCAvj.
"""


#%%
def demonstrate_dictionaries():
    """Creating and using dictionaries.
    - create a blank (empty) dictionary
    - create a non-empty dictionary
    - access dictionary values by the corresponding keys (syntax: value = d[key])
    - print a non-empty dictionary
        - print all items using the items() function
        - print one item per line
    - pprint dictionary in one column
    - add/remove items to/from a dictionary
    - update a dictionary with the items from another dictionary or from an iterable of (k, v) pairs using dict.update()
    - using the keys() and values() functions
    """

    # green_day = {}
    # print(green_day)
    # print(type(green_day))
    # print()

    green_day = {'name': 'Green Day', 'city': 'Rodeo, CA', 'year': 1987}
    print(green_day)
    print(green_day['name'])
    print()

    print(green_day.items())
    for i, j in green_day.items():
        print(i + ':', j)
    print()

    from pprint import pprint
    pprint(green_day, width=1)
    print()

    green_day['latest tour'] = 2024
    print(green_day['latest tour'])
    del green_day['latest tour']
    print(green_day)
    print()

    green_day.update({'latest tour': 2024})
    print(green_day)
    green_day.update((('guitar and vocals', 'Billy Joe Armstrong'), ('bass', 'Mike Dirnt'), ('drums', 'Tre Cool')))
    print(green_day)
    print()

    print(green_day.keys())
    print(green_day.values())


#%%
# Test demonstrate_dictionaries()
demonstrate_dictionaries()


#%%
def sort_dictionary(d, by):
    """Sorting a dictionary by keys or by values.
    - using zip()
    - using operator.itemgetter()
    - using lambda
    """

    # if by.lower() == 'k':
    #     return dict(sorted(zip(d.keys(), d.values())))
    # elif by.lower() == 'v':
    #     return dict(sorted(zip(d.values(), d.keys())))
    # else:
    #     return None

    from operator import itemgetter
    if by.lower() == 'k':
        return dict(sorted(d.items(), key=itemgetter(0)))
    elif by.lower() == 'v':
        return dict(sorted(d.items(), key=itemgetter(1)))
    else:
        return None

    # if by.lower() == 'k':
    #     return dict(sorted(d.items(), key=lambda x: x[0]))
    # elif by.lower() == 'v':
    #     return dict(sorted(d.items(), key=lambda x: x[1]))
    # else:
    #     return None


#%%
def demonstrate_dict_sorting():
    """Demonstrate sorting a dictionary.
    """

    # from pprint import pprint         # when sorting by values, pprint doesn't show the resulting dictionary correctly

    songs = {3: '21 Guns', 1: 'Wake Me Up When September Ends', 2: 'Boulevard of Broken Dreams'}
    # green_day = {'name': 'Green Day', 'place': 'Rodeo, CA', 'year': 1987}
    green_day = {'name': 'Green Day', 'place': 'Rodeo, CA', 'year': '1987'}

    # # return sort_dictionary(songs, 'k')
    # return sort_dictionary(songs, 'v')

    return sort_dictionary(green_day, 'k')
    # return sort_dictionary(green_day, 'v')


#%%
# Test demonstrate_dict_sorting()
demonstrate_dict_sorting()


#%%
def dict_comprehension(l1, l2):
    """
    Demonstrate dict comprehension
    :param l1: a list (or another iterable) of dict keys
    :param l2: a list (or another iterable) of dict values
    :return: a dict created by dict comprehension
    """

    return {k:v for k, v in zip(l1, l2)}


#%%
# Test dict_comprehension(l1, l2)
print(dict_comprehension(['guitar and vocals', 'bass', 'drums'],
                         ['Billy Joe Armstrong', 'Mike Dirnt', 'Tre Cool']))
