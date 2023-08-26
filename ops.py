"""
A simple module for printing reesults of basic operations (x+y)

.. module:: add

.. moduleauthor:: Alec

"""
def add(x,y):
    """This function prints hello with a name

    Args:
        x,y (int):  The x,y to use.

    Returns:
        int.  The return code::

        0 -- this always return 0

    Raises:
        AttributeError, KeyError

    A really simple function. Really!

    >>> print_hello_with_name(1, 3)
    4

    """
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y