class Solution:
    def sortSubArray(self, arr, initial, final, new):

        #start
        if(arr[new]<=arr[initial]):
            arr.insert(initial, arr[new])
            arr.pop(new+1)
            return arr
            
            #end
        if(arr[new]>= arr[final]):
            return arr
        
        for i in range(initial, final):
            if(arr[new]>=arr[i] and arr[new]<=arr[i+1]): 
                arr.insert(i+1, arr[new])
                arr.pop(new+1)
                return arr
        return arr
        
        
    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            self.sortSubArray(arr, 0, i-1, i)
        return arr
