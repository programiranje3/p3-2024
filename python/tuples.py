"""Demonstrates tuples.
"""


#%%
def demonstrate_tuples():
    """Creating and using tuples.
    - create and print empty tuple, 1-tuple, 2-tuple, mixed-type n-tuple
    - accessing elements of a tuple using []
    - demonstrate that tuples are immutable
    """

    # t0 = ()
    # print(t)
    # print(type(t0))
    # print()

    # # t1 = ('Green Day', )
    # t1 = 'Green Day',
    # print(t)
    # print(type(t1))
    # print()

    # t2 = 'Green Day', 'Rodeo, CA'
    # print(t)
    # print(type(t2))
    # print(len(t2))
    # print()

    t = 'Green Day', 'Rodeo, CA', 1987, True
    print(t)
    print(type(t))
    print(len(t))
    print(t[0])
    print()

    # t[4] = 25


#%%
# Test demonstrate_tuples()
demonstrate_tuples()


#%%
def demonstrate_packing():
    """Packing and unpacking tuples.
    """

    t = 'Green Day', 'Rodeo, CA', 1987, True
    print(t)
    green_day, city, year, _ = t
    print(green_day)


#%%
# Test demonstrate_packing()
demonstrate_packing()


#%%
def demonstrate_zip():
    """Using the built-in zip() function with tuples and multi-counter for-loop.
    - demonstrate zip object
    - demonstrate converting a zip object to a list object
    - demonstrate that a zip object is an iterator (must be re-initialized after looping)
    """

    members = ('Billy Joe Armstrong', 'Mike Dirnt', 'Tre Cool', )
    birth_years = (1972, 1972, 1972, )
    birth_places = ('Oakland', 'Oakland', 'Frankfurt', )

    # print(zip(members, birth_years, birth_places))
    # print(list(zip(members, birth_years, birth_places)))

    green_day = zip(members, birth_years, birth_places)
    # print(list(green_day))        # this line alone exhausts the zip, so the following loop prints nothing!
    for i, j, k in green_day:
        print(i, j, k)

    # print(list(green_day))


#%%
# Test demonstrate_zip
demonstrate_zip()

