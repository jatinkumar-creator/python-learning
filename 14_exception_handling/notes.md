#Syntax                          #error	                             #Exception
   #Found	                   #Before the program runs (compile time)	    #While it runs
  #Can try/except catch it?	   #No (except through compile()/eval())	         #Yes
  #Typical cause	                #Typo, missing colon, bad indentation	  #Bad data, missing file, logic bug
    #Example	                               #if x == 1                              #1 / 0


    # Topic 15: Exception Handling

## Syntax error vs exception
| | Syntax error | Exception |
|---|---|---|
| When found | | |
| Can try/except catch it? | | |
| Example | | |

## The exception hierarchy
(BaseException, Exception, and five families I know: ArithmeticError, LookupError, OSError, ValueError, ImportError)

## try / except / else / finally
| Block | Runs when | Typical use |
|---|---|---|
| try | | |
| except | | |
| else | | |
| finally | | |

(What happens with return inside try and finally?)

## Types of except blocks
| Form | Meaning | When to use |
|---|---|---|
| except X | | |
| except (X, Y) | | |
| except Parent | | |
| except Exception as e | | |
| bare except | | |
| except* | | |

Why order matters:

## raise
| Form | Meaning |
|---|---|
| raise X("msg") | |
| raise (bare) | |
| raise X from e | |
| raise X from None | |

## assert
(What it is for, what -O does, assert vs raise)

## User-defined exceptions
(How to define one, why a base class, extra attributes, naming)

## Cleanup
(with vs try/finally, what __exit__ receives, suppress)

## EAFP vs LBYL
(Which is Pythonic, with an example)

## Errors I triggered
| Code | Error name | Why |
|---|---|---|

## Predictions I got wrong today

## Questions I still have


Interview questions to answer :-
What is the difference between a syntax error and an exception?
Explain try, except, else, and finally. In what order do they run?
When does finally run? What happens if you return inside it?
Why is a bare except: a bad idea?
Why does the order of except clauses matter?
What is the difference between raise, raise e, and raise X from e?
What is the difference between assert and raise? Can asserts be turned off?
How do you create a custom exception, and why would you?
What is the difference between BaseException and Exception?
What does a with block do when an exception occurs inside it?
What is EAFP, and how does it differ from LBYL?
What is an ExceptionGroup, and what does except* do?






Problem	Fix
#SyntaxError: expected 'except' or 'finally' block	 -----------------    #A try needs at least one except or a finally
#SyntaxError: multiple exception types must be parenthesized  --------------  #Write except (A, B): with parentheses
#An error vanishes and the result is wrong  ---------------------------------#A bare except: or except Exception: pass is hiding it. Catch the specific error and log it
#A specific except never runs ----------------------------------------------#A broader one sits above it. Put the most specific handlers first
#NameError for e after the block	 -------------------------------------------#The as e name is deleted when the block ends. Copy it first (saved = e)
#TypeError: exceptions must derive from BaseException	-----------------    #You raised or caught something that isnt an exception class
#RuntimeError: No active exception to reraise	------------------  #A bare raise outside an except block
#Asserts stop working	----------------------------               #Python was started with -O. Dont use assert for validation
KeyError message shows extra quotes	--------------------------------  #A known quirk: str(KeyError("k")) quotes its argument


