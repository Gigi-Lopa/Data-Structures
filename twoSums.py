"""
    Finds the value need to produce the target value

"""
def twoSums(arr, target):
    
    verified = {

    }
    for i, val in enumerate(arr):
        if target - val in verified:
            return ([verified[target - val], i])
        elif val not in verified:
            verified[val] = i

print(twoSums([3,2,7], 10))