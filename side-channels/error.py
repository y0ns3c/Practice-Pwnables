from _getuserfunc import getfunc, UserCodeError

from os import _exit
import random

print("This program will execute your python code to run a 'compute' function.")
print("The function will be called with 1 integer argument and print its result as a boolean value.")
print()
print("If your code is faulty, this program will exit with status 1")
print("If the function throws a IndexError, this program will exit with status 2.")
print("If the function throws a ArithmeticError, this program will exit with status 3.")
print("Otherwise, this program will exit with status 0")
print()

try:
    compute = getfunc('compute', flag="{flag_gather_em_bits}")
    print(compute(random.randrange(0, 10)) == True)
except UserCodeError as err:
    print(err)
    _exit(1)
except IndexError:
    _exit(2)
except ArithmeticError:
    _exit(3)
except:
    pass

_exit(0)
