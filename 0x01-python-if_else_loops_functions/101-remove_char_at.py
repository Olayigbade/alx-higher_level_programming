#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = list(str)
    str2[n] = ''
    return ''.join(str2)
