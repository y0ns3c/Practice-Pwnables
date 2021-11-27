from _getuserfunc import getfunc, UserCodeError

from os import _exit

print("This program will execute your python code to run a 'bye' function.")
print("The function will be called with no arguments.")
print()
print("If your code is faulty, this program will exit with status 1")
print("The return value will be used as the exit status code.")
print()

try:
    bye = getfunc('bye', flag="{flag_leaked_with_exitcode}")
    _exit(bye())
except UserCodeError as err:
    print(err)
    _exit(1)
