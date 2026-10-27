# try:
#     x = 1
# print("after")                          # SyntaxError: expected 'except' or 'finally' block

# try:
#     pass
# finally:
#     pass
# except ValueError:                      # SyntaxError: except cannot come after finally
#     pass

# try:
#     pass
# except ValueError, TypeError:           # SyntaxError on Python 3.12 (parentheses needed); newer versions relax it
#     pass

# raise "something went wrong"            # TypeError: exceptions must derive from BaseException

# class NotAnError:
#     pass
# raise NotAnError()                      # TypeError: exceptions must derive from BaseException

# try:
#     1 / 0
# except NotAnError:                      # TypeError: catching classes that do not inherit from BaseException
#     pass

# raise                                   # RuntimeError: No active exception to reraise

# raise ValueError("x") from "not an exception"    # TypeError: exception causes must derive from BaseException

# assert (1 == 2, "this never fails")     # SyntaxWarning: assertion is always true, because it is a non-empty tuple
# print("the assert did nothing")

# try:
#     result = undefined_function()       # a typo
# except:                                 # a bare except hides the NameError completely
#     result = None
# print(result)                           # prints None, so the bug is invisible