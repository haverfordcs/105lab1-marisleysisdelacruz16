"""
Lab 1: the power function
cs105 Introduction to Computer Science
Haverford College
Marisleysis De La Cruz
"""

def simple_power_ui():
    # doctest use, as per http://docs.python.org/lib/module-doctest.html
    import doctest
    print("Trying out tests given at the beginning of this script")
    doctest.testmod()

if __name__ == "__main__":
    simple_power_ui()

# The execution starts here

def power_using_iteration(base, exp):
    """postcondition: the result is the base raised to the exp power,
                      or a close approximation for information that
                      isn't represented exactly (such as real numbers)."""
    if not (isinstance(base, int) or isinstance(base, float)):
        raise TypeError("Base should be either integer or float")

    if not isinstance(exp, int):
        raise TypeError("Exponent is supposed to be integer")

    result=1
    for power_using_iteration in range (abs(exp)):
        if exp == 0:
            return result
        if exp < 0:
            result *= 1.0/base
        else:
         while exp:
            result= result*base
            exp = exp-1
    return result


# Test Cases
'''
>>> power_using_iteration(1.0, -2)
1.0

>>> power_using_iteration(1.2, -3) #doctest: +ELLIPSIS
0.578703...

>>> power_using_iteration(5, -1) 
0.2

>>> power_using_iteration(10, -4)  
0.000100...

>>> power_using_iteration(0.6, -5)   
12.860082...
'''