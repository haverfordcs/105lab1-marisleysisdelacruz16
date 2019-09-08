"""
Lab 1: the power function
cs105 Introduction to Computer Science
Haverford College
Marisleysis De La Cruz
"""

def power_using_recursion(base, exp):
    """postcondition: the result is the base raised to the exp power,
                      or a close approximation for information that
                      isn't represented exactly (such as real numbers)."""
    if not (isinstance(base, int) or isinstance(base, float)):
        raise TypeError("Base should be either integer or float")

    if not isinstance(exp, int):
        raise TypeError("Exponent is supposed to be integer")

    if exp == 0:
        return 1
    if exp < 0:
            return 1/power_using_recursion(base,abs(exp))
    else:
        assert(exp > 0)
        base_to_the_exp_minus_one = power_using_recursion(base, exp-1)
        return base * base_to_the_exp_minus_one

# Test cases
'''
>>> power_using_recursion(2, -3)
0.0125

>>> power_using_recursion(3, -3) # doctest: +ELLIPSIS
0.038037...

>>> power_using_recursion(20.0, -2)  
0.0025

>>> power_using_recursion(5.3, -4) # doctest: +ELLIPSIS
0.0012673...

>>> power_using_recursion(0.3, -6)
1371.742112...

'''
