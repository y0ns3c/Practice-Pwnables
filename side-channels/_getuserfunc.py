import functools
from typing import Callable
import sys
import builtins
import types

class UserCodeError(Exception):
    pass

def input(prompt: str = None):
    if prompt != None:
        print(prompt)
    return sys.stdin.read()

def getfunc(func_name: str, *, flag: str, permit: 'list[str]' = []):
    user_global = {'__builtins__': restricted_builtins(permit), 'flag': flag}

    func_str = input(f"Enter your python code with {func_name} function: ")

    try:
        user_locals = dict()
        exec(f"{func_str}", user_global, user_locals)
        func = user_locals[func_name]
    except Exception as err:
        raise UserCodeError(f"Error from executing user code: {err}")

    if not isfunc(func, func_name):
        raise UserCodeError(f"Could not get '{func_name}' function")

    return func

def isfunc(obj, name: str):
    return callable(obj) and hasattr(obj, '__name__') and obj.__name__ == name

def restricted_builtins(permit):
    def disable_func(func: Callable):
        @functools.wraps(func)
        def wfunc(*args, **kwargs):
            raise UserCodeError(f"You cannot use the '{func.__name__}' function!")
        return wfunc

    def enable_func(func: Callable):
        @functools.wraps(func)
        def wfunc(*args, **kwargs):
            return func(*args, **kwargs)
        return wfunc

    result = dict(builtins.__dict__)

    restrict_def = ['compile', 'eval', 'exec', 'input', 'memoryview', 'open', 'print', '__import__', 'globals', 'locals', 'vars', 'getattr']
    ban = [x for x in restrict_def if x not in permit]

    for attr in result:
        if type(result[attr]) == types.BuiltinFunctionType:
            if attr in ban:
                result[attr] = disable_func(result[attr])
            else:
                result[attr] = enable_func(result[attr])

    return result
