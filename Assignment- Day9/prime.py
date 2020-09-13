
'''
Creating a python file for finding whethere the given number is prime number or not.
'''

def is_prime(given_no):
    '''
    function to check for prime number.
    '''
    if given_no >= 1:
        for i in range(2, given_no):
            if (given_no % i) == 0:
                final_result = "Not Prime"
            else:
                final_result = "Prime"
    else:
        final_result = "Not Prime"
    return final_result
