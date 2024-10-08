"""The very first Python script - main.py.
"""


# #%%
# # Hello world: the print() built-in function and the + operator.
# print('Green Day')
# print('Green Day ' + 'is an American punk rock band.')
# print('Green Day', 'is an American punk rock band.')
# print()
#
# green_day = 'Green Day'
# print(f'{green_day} is an American punk rock band.')
#
# #%%
# # The input() built-in function
# band = input('Band name: ')
# print(f'{band}')
#
#
# #%%
# # A simple function and function call
# def band():
#     band = input('Band name: \n')
#     year_formed = input('Formed: \n')
#     print(f'{band} is a band formed in {year_formed}.')
#
# band()
#
#
# #%%
# # A simple loop and the range() built-in function
# for i in range(5):
#     print(i)
#
#
# #%%
# # A simple list, accessing list elements, printing lists
# green_day = ['Green Day', 1987, 'Rodeo, CA', True]
# print(green_day)
#
# #%%
# # Looping through list elements - for and enumerate()
# for i in range(len(green_day)):
#     print(green_day[i])
# print()
#
# for i, j in enumerate(green_day):
#     print(str(i+1) + ':', j)
#
#
# #%%
# # Global variables: __name__, __file__, __doc__,...
# print(__name__)
# # print(__file__)
# print(__doc__)

#%%
# Importing from another script
from inception import *
# from blankscripts import *
print(green_day_function())