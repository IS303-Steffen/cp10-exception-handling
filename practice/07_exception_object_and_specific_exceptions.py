import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# =======
# EXCEPTION OBJECT & SPECIFIC EXCEPTIONS
# =======

'''
OVERVIEW
--------
after the "except" statement, you can specify an
Exception object that allows you to see the exact error that was caught.

There are also many specific Exceptions you can catch. That means you can
have multiple except statements, with different code for each type of exception.
This give you lots of control over how you respond to different types of
errors.

See the bottom of this page for some examples.

'''


# 1. USING THE GENERAL EXCEPTION OBJECT
# Follow along. First add "Exception as e" to the except statement.
# try printing out type(e).__name__ and also try printing out e directly.
# Then run the code with an invalid input. What kind of exception was thrown?

# Then after learning what type of exception it is, add a new except statement
# above the first one that specifically mentions the type of exception you want
# to catch. Feel free to add a more specific version of the message.


try:
    num_cust = int(input("\nHow many customers would you like to enter? " ))

    #For each customer:
    for count in range(1, num_cust + 1) :
        print("This is just an example, customer #", count)

except:
    print("Something went wrong")



'''
SOME COMMON TYPES OF EXCEPTIONS
-------------------------------

"AttributeError":       "Raised when an attribute reference or assignment
                         fails.",
"IndexError":           "Raised when a sequence subscript is out of range.",
"KeyError":             "Raised when a dictionary key isn't found.",
"NameError":            "Raised when a local or global name is not found.",
"TypeError":            "Raised when an operation or function is applied to an
                         object of inappropriate type.",
"ValueError":           "Raised when a function receives an argument of correct
                         type but inappropriate value.",
"ZeroDivisionError":    "Raised when the second argument of a division or
                         modulo operation is zero.",
"FileNotFoundError":    "Raised when trying to open a file that doesn't exist.",
"IOError":              "Raised when an I/O operation fails, such as `print`
                         function failure or failure to open a file.",
"ImportError":          "Raised when an `import` statement fails to find the
                         module definition or when a `from ... import` fails to
                         find a name that is to be imported.",
"OSError":              "Raised for operating system-related errors, like file
                         not found or disk full.",
"RuntimeError":         "Raised by the `raise` statement or, if no exception
                         is given, defaults to being runtime error.",
"SyntaxError":          "Raised when the parser encounters a syntax error."
'''


