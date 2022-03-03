import random
class genArray:


    def getArray(self,arrSize):
        arr = []
        for _ in range(0, arrSize):
            arr.append(random.randint(0,10))

        return arr  