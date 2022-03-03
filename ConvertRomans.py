''''
    Converts Roman Characters into intergers e.g MCMXCIV into an interger of 1994
'''
class conRomans:
    def romanChars(s):
        romans ={
        "I" :1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }
        specialRomans = {
            "IV" : 4,
            "IX" : 9 ,
            "XC" : 90, 
            "XL" : 40,
            "CM" : 900,
            "CD" : 400
        }
        c = 0
        i = 0
        while i < len(s):
            if i != len(s) -1:
                if (s[i] + s[i + 1]) in specialRomans:
                    c = c + specialRomans[s[i] + s[i + 1]]
                    i += 2
                else:
                    c = c + romans[s[i]]
                    i += 1
            else:
                c = c + romans[s[i]]
                i += 1
        return(c)

print(conRomans.romanChars("MMMM"))