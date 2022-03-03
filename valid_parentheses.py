'''
    Checks for the validity of parenthesis 
    returns True if they are correct

'''
def valid(theString):
    stack = []
    dataMap = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }

    for s in theString:
        if s in dataMap:
            if stack and stack[-1] == dataMap[s]:
                stack.pop()
            else:
                pass
        else:
            stack.append(s)
        
    
    return True if not stack else False

if __name__ == '__main__':
    print(valid("{}}{"))
    