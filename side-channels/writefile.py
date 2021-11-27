from _getuserfunc import getfunc, UserCodeError

from os import _exit

print("This program will execute your python code to run a 'quiet' function.")
print("The function will be called with no arguments.")
print()
print("If your code is faulty, this program will exit with status 1")
print("You will be allowed to use the 'open' builtin function.")
print()

try:
    quiet = getfunc('quiet', flag="{flag_slipped_a_note}", permit=['open'])
    quiet()
except UserCodeError as err:
    print(err)
    _exit(1)
