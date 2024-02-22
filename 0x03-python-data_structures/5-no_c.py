#!/usr/bin/python3
def no_c(my_string):
    rem_ove = [i for i in my_string if i != 'c' and i != 'C']
    return("".join(rem_ove))
