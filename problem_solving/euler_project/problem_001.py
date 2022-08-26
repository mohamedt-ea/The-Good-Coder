# https://projecteuler.net/problem=1
# Main Topic : 
#   Natural numbers 
#       -->  are those numbers used for counting (Wiki)
#       --> The term "natural number" refers either to a member of the set of positive integers 1, 2, 3, . . 
#           or to the set of nonnegative integers 0, 1, 2, 3 (Wolfram)
#       

"""
    Question:
        If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

        Find the sum of all the multiples of 3 or 5 below 1000.
    
    Key: is that wanted number that could be divided by 3 or 5 or both like(15).

    Side Topics: 
        - Modulo The term modulo comes from a branch of mathematics called modular arithmetic --> https://en.wikipedia.org/wiki/Modular_arithmetic.
"""

def multiplies_3(number):
    if number == 3:
        return True

    if (number % 3 and number > 3) or (number < 3):
        return False
    else:
        return True

def multiplies_5(number):
    if number == 5:
        return True

    if (number % 5 and number > 5) or (number < 5):
        return False
    else:
        return True

def get_sum_of_multiplies_3_5_below(number):
    sum = 0
    for i in range(number):
        if multiplies_3(i) or multiplies_5(i):
            sum += i

    return sum


if __name__ == "__main__":
    print(get_sum_of_multiplies_3_5_below(1000))
     