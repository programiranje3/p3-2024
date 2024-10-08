"""The very first module in a more structured version of the project.
"""


#%%
# Moving part of the code from main.py

# from datetime import date
# print(date(2024, 6, 19))
# print(__name__)
# print()


#%%
# Printing with ' ' and printing without '\n'

# print('Green Day', 'is an American punk rock band.')
# print('Green Day', end='')
# print(' is an American punk rock band.')


#%%
# A simple function and function call
def green_day_function():
    """
    A simple function
    :return: None
    """
    print('Green Day')


# print(green_day())

#%%
# Printing docstrings

# print(green_day.__doc__)

#%%
# break and continue

# green_day = ['Green Day', 1987, 'Rodeo, CA', True]
# print(green_day)
#
# # Looping through list elements - for and enumerate()
# for i in range(len(green_day)):
#     if i == 2:
#         break
#     print(green_day[i])
# print()


#%%
# Importing from Standard Library

# Date format strings
# https://docs.python.org/3/library/datetime.html?highlight=date%20format%20strings#strftime-and-strptime-format-codes

# from datetime import date
# print(date(2024, 6, 19))
# print(date(2024, 6, 19).strftime('%b %d, %Y'))


#%%
# Testing print(__file__)

# print(__file__)

#%%
# Taking care of the module __name__
if __name__ == '__main__':

    # from datetime import date
    # print(date(2024, 6, 19))
    # print(__name__)
    # print()
    #
    # print(green_day_function())
    # print()
    #
    # print(green_day_function.__doc__)
    # print()
    #
    # print('Green Day', 'is an American punk rock band.')
    # print('Green Day', end='')
    # print(' is an American punk rock band.')
    # print()
    #
    # green_day = ['Green Day', 1987, 'Rodeo, CA', True]
    # print(green_day)
    #
    # # Looping through list elements - for and enumerate()
    # for i in range(len(green_day)):
    #     if i == 2:
    #         break
    #     print(green_day[i])
    # print()

    # print(__file__)

    from datetime import date
    print(date(2024, 6, 19))
    print(date(2024, 6, 19).strftime('%b %d, %Y'))
