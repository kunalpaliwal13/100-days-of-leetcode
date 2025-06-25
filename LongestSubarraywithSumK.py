# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        dih ={0:0}
        sum =0
        length=0
        
        for i in range(len(arr)):
            sum +=arr[i]
            if sum not in dih:
                dih[sum] = i+1
            if (sum - k) in dih:
                length = max(i+1-dih[sum-k], length)
                
        return length
                
        
    
