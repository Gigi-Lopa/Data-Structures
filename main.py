from cgi import print_form
import math
from genArray import genArray

class binarySearch:
    def binary__search(self,val):
        arr = [0, 1, 2, 3, 4, 5]
        lowIndex = 0
        highIndex = len(arr) - 1

        while lowIndex <= highIndex:
            
            middleIndex =  math.floor((lowIndex + highIndex) / 2)

            if arr[middleIndex] < val:
                lowIndex = middleIndex + 1
            
            elif arr[middleIndex] > val:
                highIndex = middleIndex - 1
            
            else:
                lowIndex = highIndex + 1 
                print(f"Found Match at index {middleIndex}")

class sortingAlgorithms:
    def QuickSort(self, arr, low, high):
        def get__pivot(arr, low, high):
            mid = (high + low) // 2 
            pivot = high
            if arr[low] < arr[mid] and  arr[mid] < arr[high]:
                pivot = mid
            elif arr[low] < arr[high]:
                pivot = low

            return pivot

        def partition(arr, low, high):
            pivotIndex = get__pivot(arr, low, high)
            pivotValue = arr[pivotIndex]
            arr[pivotIndex], arr[low] = arr[low], arr[pivotIndex]
            border = low

            for i in range(low, high + 1):
                if arr[i] < pivotValue:
                    border += 1
                    arr[i], arr[border] = arr[border], arr[i]
            
            arr[low], arr[border] = arr[border], arr[low]
         
            return border
        
        def quick__sort(arr, low, high):
            if low < high:
                pivot = partition(arr, low, high)
                quick__sort(arr, low , pivot -1) #Left side
                quick__sort(arr, pivot + 1, high) #right side
        quick__sort(arr, low, high)
        
    def BubbleSort(self, arr):
        for i in range(0, len(arr)):
            for j in range(0, len(arr) - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        
        print(arr)
        

    def InsertSort(self, arr):
        
        for i in range(0, len(arr)):
            curVal = arr[i]
            j = i-1
            while j >= 0 and curVal < arr[j] :
                arr[j + 1] = arr[j], curVal
                j -= 1
        

    def ComboSort(self):
        pass

class FibonacciSuquence:
    def getFib(self, val):
        a = 0
        b = 1

        if val == b:
            print(a)
        else:
            print(a)
            print(b)

            for i in range(2, val):         
                c =  a + b
                a = b
                b = c
                if c > val:
                    break
                else:
                    print(c)
        

if __name__ == '__main__':
    genArray1 =  genArray()
    arr = genArray1.getArray(10)
    
    bs = binarySearch()
    #bs.binary__search(4)
    
    fb = FibonacciSuquence()
    #fb.getFib(100)   

    sa = sortingAlgorithms()
    #sa.QuickSort(arr, 0 , len(arr)-1)
    #sa.InsertSort(arr)
    sa.BubbleSort(arr)

    