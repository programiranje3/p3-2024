"""The class representing the concept of a music group/band.
It includes a list of Musician objects (band members) and the date when the band started performing together.

The corresponding exception classes are included as well.
File I/O and JSON encoding/decoding of Band objects are demonstrated too.
"""


#%%
# Setup / Data

import pickle
from datetime import date, datetime, time
# import json
import sys

# from music.musician_module import Musician
from music.musician import Musician
from util.utility import format_date, get_project_dir, get_data_dir

from testdata.musicians import *


#%%
class Band:
    """The class describing the concept of a music group/band.
    It includes a list of Musician objects (band members)
    and the dates when the band started/stopped performing together.
    """

    # Class variables: like static fields in Java; typically defined and initialized before __init__()
    # Insert a class variable (static field), such as genres, date_pattern,...

    styles = ['punk rock', 'alternative rock']

    def __init__(self, name, *members, start=date.today(), end=date.today()):
        # Code to check if the band name is specified correctly (possibly raises BandNameError)
        if not isinstance(name, str) or len(name) < 2:
            raise BandNameError(name)

        self.name = name
        self.members = members
        self.start = start
        self.end = end

        # self.__i = 0                                  # introduce and initialize iterator counter, self.__i

    def __str__(self):
        n = self.name + ': ' if self.members else self.name + '; '
        m = ', '.join([str(m) for m in self.members]) + "; " if self.members else ''
        s = self.start.year
        e = self.end.year
        return f'{n}{m}{s}-{e}'

    def __eq__(self, other):
        # Musician objects are unhashable, so comparing the members tuples from self and other directly does not work;
        # see https://stackoverflow.com/a/14721133/1899061, https://stackoverflow.com/a/17236824/1899061
        # return self == other if isinstance(other, Band) else False    # No! Musician objects are unhashable!
        # However, this works:
        return self.__dict__ == other.__dict__ if isinstance(other, Band) else False

        # # members must be compared 'both ways', because the two tuples can be of different length
        # m_diff_1 = [x for x in self.members if x not in other.members]
        # m_diff_2 = [x for x in other.members if x not in self.members]
        # m = len(m_diff_1) == len(m_diff_2) == 0

        # members must be compared 'both ways', because the two tuples can be of different length

    @staticmethod
    def is_date_valid(d):
        """It is assumed that a band does not perform together since more than ~60 years ago.
        So, the valid date to denote the start of a band's career is between Jan 01, 1960, and today.
        """
        return True if date(1954, 7, 5) <= d < date.today() and isinstance(d, date) else False

    def __iter__(self):
        """Once __iter__() and __next__() are implemented in a class,
        we can create an iterator object by calling the iter() built-in function on an object of the class,
        and then call the next() built-in function on that object.
        It is often sufficient to just return self in __iter__(),
        if the iterator counter such as self.__i is introduced and initialized in __init__().
        Alternatively, the iterator counter (self.__i) is introduced and initialized here.
        """

        self.__i = 0
        return self               # sufficient if the iterator counter is introduced and initialized in __init__()

    def __next__(self):
        if self.__i < len(self.members):
            m = self.members[self.__i]
            self.__i += 1
            return m
        raise StopIteration


#%%
# Check class variables
print(Band.styles)

#%%
# Test the basic methods (__init__(), __str__(),...)
green_day = Band('Green Day', *[billyJoeArmstrong, treCool, mikeDirnt],
                 start=date(1987, 7, 18), end=date.today())
print(green_day)

#%%
# Test the date validator (@staticmethod is_date_valid(<date>))
print(Band.is_date_valid(date(1954, 1, 1)))

#%%
# Test the iterator (initialize it with iter(<band>) and call next(<iterator) in a loop to return all <band> members)
green_day = Band('Green Day', *[billyJoeArmstrong, treCool, mikeDirnt],
                 start=date(1987, 7, 18), end=date.today())
i = iter(green_day)
while 23:
    try:
        print(next(i))
    except StopIteration:
        print('Done')
        break
# print(next(i))


#%%
def next_member(band):
    """Generator that shows members of a band, one at a time.
    yield produces a generator object, on which we call the next() built-in function.
    A great tutorial on generators: https://realpython.com/introduction-to-python-generators/.
    """

    for m in band.members:
        input('Next:')
        yield(m)
        print('Yeah!')


#%%
# Test next_member(band)
# (initialize it with next_member(<band>) and call next(<generator>) in a loop to return/generate all <band> members)
green_day = Band('Green Day', *[billyJoeArmstrong, treCool, mikeDirnt],
                 start=date(1987, 7, 18), end=date.today())
g = next_member(green_day)
while 9:
    try:
        print(next(g))
    except StopIteration:
        break
# print(next(g)

#%%
# Demonstrate generator expressions
g = (p for p in range(3))
# print(g)
while 2:
    try:
        print(next(g))
    except StopIteration:
        break

#%%
# Demonstrate JSON encoding/decoding of Band objects

# Using the json_tricks module from the json-tricks external package (https://github.com/mverleg/pyjson_tricks).
# From the package documentation:
# The JSON string resulting from applying the json_tricks.dumps() function stores the module and class name.
# The class must be importable from the same module when decoding (and should not have changed).
# If it isn't, you have to manually provide a dictionary to cls_lookup_map when loading
# in which the class name can be looked up. Note that if the class is imported, then globals() is such a dictionary
# (so try loads(json, cls_lookup_map=globals())).
# Also note that if the class is defined in the 'top' script (that you're calling directly),
# then this isn't a module and the import part cannot be extracted. Only the class name will be stored;
# it can then only be deserialized in the same script, or if you provide cls_lookup_map.
# That's why the following warning appears when serializing Band objects in this script:
# UserWarning: class <class '__main__.Band'> seems to have been defined in the main file;
# unfortunately this means that it's module/import path is unknown,
# so you might have to provide cls_lookup_map when decoding.

# Single object
from json_tricks import loads, dumps
# green_day = Band('Green Day', *[billyJoeArmstrong, treCool, mikeDirnt],
#                  start=date(1987, 7, 18), end=date.today())
# green_day_json = dumps(green_day, indent=4)
# print(green_day_json)
# print()
#
# green_day_restored = loads(green_day_json)
# print(green_day_restored)
# print(green_day_restored == green_day)

# List of objects

theBeatles = Band('The Beatles', *[johnLennon, paulMcCartney, georgeHarrison, ringoStarr],
                  start=date(1957, 7, 6), end=date(1970, 4, 10))
theRollingStones = Band('The Rolling Stones', *[mickJagger, keithRichards, ronWood, charlieWatts],
                        start=date(1962, 7, 12))
theYardbirds = Band('The Yardbirds', *[jimMcCarty, chrisDreja, keithRelf, jeffBeck, paulSamwellSmith])

bands = [theBeatles, theRollingStones, theYardbirds]

bands_json = dumps(bands, indent=4)
print(bands_json)
print()

bands_restored = loads(bands_json)
# print(bands_restored)
for b in bands_restored:
    print(b)


#%%
class BandError(Exception):
    """Base class for exceptions in this module.
    """

    pass


#%%
class BandNameError(BandError):
    """Exception raised when the name of a band is specified incorrectly.
    """

    def __init__(self, name):
        """ It is usually sufficient just to call Exception.__init__() and pass self and an f-string that
        includes the other argument(s) and prints the error message;
        it can be followed by self.<other> = <other> statement(s) for completeness."""

        Exception.__init__(self, f'not a valid band name \'{name}\'')


#%%
# Demonstrate exceptions

#%%
# Catching exceptions - try-except block
# If an exception is caught as e, then e.args[0] is the type of exception (relevant for exception handling).
# To write error messages to the exception console, use sys.stderr.write(f'...').

green_day = Band('Green Day', *[billyJoeArmstrong, mikeDirnt, treCool],
                 start=date(1987, 8, 12), end=date(3000, 12, 12))
try:
    for i in range(0, 4):
        print(green_day.members[i])
except Exception as e:
    # print(e)
    # print(f'{e.__class__.__name__}: {e.args[0]}')
    sys.stderr.write(f'{e.__class__.__name__}: {e.args[0]}')


#%%
# Catching multiple exceptions and the 'finally' clause

green_day = Band('Green Day', *[billyJoeArmstrong, mikeDirnt, treCool],
                 start=date(1987, 8, 12), end=date(3000, 12, 12))
try:
    for i in range(0, 3):
        print(green_day.members[i])
    # print(5/0)
except IndexError as e:
    sys.stderr.write(f'{e.__class__.__name__}: {e.args[0]}')
except ZeroDivisionError as e:
    sys.stderr.write(f'{e.__class__.__name__}: {e.args[0]}')
finally:
    print('\nFinally always runs')


#%%
# Using the 'else' clause (must be after all 'except' clauses)

green_day = Band('Green Day', *[billyJoeArmstrong, mikeDirnt, treCool],
                 start=date(1987, 8, 12), end=date(3000, 12, 12))
try:
    for i in range(0, 3):
        print(green_day.members[i])
    print(5/0)
except IndexError as e:
    sys.stderr.write(f'{e.__class__.__name__}: {e.args[0]}')
except ZeroDivisionError as e:
    sys.stderr.write(f'{e.__class__.__name__}: {e.args[0]}')
else:
    print('\nNo exception raised')
finally:
    print('\nFinally always runs')


#%%
# Catching 'any' exception - empty 'except' clause

green_day = Band('Green Day', *[billyJoeArmstrong, mikeDirnt, treCool],
                 start=date(1987, 8, 12), end=date(3000, 12, 12))
try:
    for i in range(0, 4):
        print(green_day.members[i])
    print(5/0)
except Exception:
    sys.stderr.write(f'Exception occurred')


#%%
# Catching user-defined exceptions

try:
    green_day = Band('G', *[billyJoeArmstrong, mikeDirnt, treCool],
                     start=date(1987, 8, 12), end=date(3000, 12, 12))
except BandNameError as e:
    sys.stderr.write(f'{e.__class__.__name__}: {e.args[0]}')


#%%
# Demonstrate working with files

theBeatles = Band('The Beatles', *[johnLennon, paulMcCartney, georgeHarrison, ringoStarr],
                  start=date(1957, 7, 6), end=date(1970, 4, 10))
theRollingStones = Band('The Rolling Stones', *[mickJagger, keithRichards, ronWood],
                        start=date(1962, 7, 12))
theYardbirds = Band('The Yardbirds', *[jimMcCarty, chrisDreja, keithRelf, jeffBeck, paulSamwellSmith])

bands = [theBeatles, theRollingStones, theYardbirds]


#%%
# Writing to a text file - <outfile>.write(str(<obj>), <outfile>.writelines([str(<obj>)+'\n' for <obj> in <objs>])

file = get_data_dir() / 'bands.txt'
with open(file, 'w') as f:
    # for b in bands:
    #     f.write(str(b) + '\n')
    f.writelines([str(b) + '\n' for b in bands])
print('Done')

#%%
# Demonstrate reading from a text file - <infile>.readline(), <infile>.readlines(), <infile>.read()
file = get_data_dir() / 'bands.txt'
with open(file, 'r') as f:
    # while 1:
    #     try:
    #         print(f.readline())
    #     except:
    #         break
    # print(f.readlines())
    print(f.read())

#%%
# Demonstrate writing to a binary file - pickle.dump(<obj>, <outfile>)
file = get_data_dir() / 'bands.bin'
with open(file, 'wb') as f:
    pickle.dump(bands, f)
print('Done')

#%%
# Demonstrate reading from a binary file - pickle.load(<infile>)
file = get_data_dir() / 'bands.bin'
with open(file, 'rb') as f:
    bands_restored = pickle.load(f)
# print(bands_restored)
for b in bands_restored:
    print(b)


