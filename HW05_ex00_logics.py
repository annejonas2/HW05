#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################

def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    number = raw_input('Give a number.\n')
    try:
        int_number = int(number)
        if int_number % 2 == 0:
            print "This number is even."
        else:
            print "This number is odd."
        return
    except:
        print "Needs to be a non-word numeral"
        even_odd()


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    ##couldn't get this one - here's as far as I got
    for i in range(0,100):
        if (i % 10 == 0) and (i > 0):
            print '\n'
        else:
            i = i + 1
            print   i  , 
   
def find_average(): 
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    temp_value = 0
    number = raw_input('Give a number.\n')
    count = 1
    while (number != "done"): #I can't figure out how to limit to numbers and still keep it working, even with try/else
        temp_value = int(number) + temp_value
        count = count + 1
        number = raw_input('Give a number.\n')
    return (float(temp_value) / (count - 1))

##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten() 
    print find_average()

if __name__ == '__main__':
    main()
