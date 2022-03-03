'''
    Looks for a substring using pointers and comparing these pointer (L , R) pointers if they match
    A substring is a value that is still the same value vice verse i.e 'bab' is still "bab" vice versa
'''

import time
def subString(s):
    start_time =  time.time()
    res = ""

    if len(res) >= 0:
        for i in range(1, len(s) - 1):
            if s[i - 1] == s[i + 1]:
                res = s[i - 1] + s[i] + s[i + 1]
            
            if len(res) == 0:
                if s[i - 1] == s[i]:
                    res = s[i - 1] + s[i]
                elif s[i] == s[i + 1]:
                    res = s[i]+ s[i + 1]
    end__time = time.time()
    return ("The subsring is: " +res+ " of length: " + str(len(res)) + " time " + str(end__time - start_time))

print(subString("cbbd"))
