"""Demonstrates sets.
"""


#%%
def demonstrate_sets():
    """Creating and using sets.
    - create a set and make an attempt to duplicate items
    - demonstrate some typical set operators:
        & (intersection)
        | (union)
        - (difference)
        ^ (disjoint)
    """

    green_day = {'Green Day', 1987, 'Rodeo, CA'}
    print(green_day)
    green_day.add(1987)
    print(green_day)
    print()

    print(green_day | {'Green Day', 'Mike Dirnt'})
    print(green_day & {'Green Day', 'Mike Dirnt'})
    print(green_day ^ {'Green Day', 'Mike Dirnt'})
    print(green_day - {'Green Day', 'Mike Dirnt'})


#%%
# Test demonstrate_sets()
demonstrate_sets()


