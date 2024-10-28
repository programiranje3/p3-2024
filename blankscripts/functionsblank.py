"""Demonstrates details of writing Python functions: annotations, default args, kwargs.
"""


#%%
# Setup / Data
song = 'Wake Me Up When September Ends'
year = 2004

bj = 'Billy Joe Armstrong'
mike = 'Mike Dirnt'
tre = 'Tre Cool'
green_day = [bj, mike, tre]


#%%
def demonstrate_annotations(title, year):
    """Demonstrates how to use annotations of
    function parameters/arguments (<arg>: <type>) and of function return type (def f(...) -> <type>:).
    - print the function parameters/arguments
    - print the value of the __annotations__ attribute of this function
    - print the name and the docstring of this function
    - return a formatted string (including function parameters/arguments)
    """


#%%
# Test demonstrate_annotations(title, year)
print(demonstrate_annotations(song, year))


#%%
def show_song(title, author=bj, year: int = 2004):

    """Demonstrates default arguments/parameters.
    - print locals()
    - print the function arguments/parameters in one line
    """


#%%
# Test def show_song(title, author=bj, year: int = 2004):
show_song(song)


#%%
def use_flexible_arg_list(band: str, *members):
    """Demonstrates flexible number of arguments/parameters.
    - print the band name and the list of band members in one line
    """


#%%
# Test use_flexible_arg_list(band: str, *members)
use_flexible_arg_list('Green Day', *green_day)
use_flexible_arg_list('Green Day')


#%%
def use_all_categories_of_args(band, *members, is_active=True, **details):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """


#%%
# Test use_all_categories_of_args(band, *members, is_active=True, **details)
use_all_categories_of_args('Green Day', is_active=True, start=1987, end=3000)
use_all_categories_of_args('Green Day', *green_day, is_active=False,
                           start=1987, end=3000)
