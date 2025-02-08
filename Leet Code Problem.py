# You are given an integer array nums of length n, and an integer array queries of length m.

# Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

# 
# Input: nums = [4,5,2,1], queries = [3,10,21]
# Output: [2,3,4]
# Explanation: We answer the queries as follows:
# - The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
# - The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
# - The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.

# def Subsequence(num,query):
    # num.sort()
    # sum =0
    # Answer =[]
    # for i in query:
    #     sum = 0
        # lenght =0
        # for i in range(len(num)):
        #     if sum + num[i]<=i:
        #         sum+=num[i]
        #         length+=1
        #     else:
        #         break               
        # Answer.append(length)
        
        
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

#  Time Complixity  O(nlogn)

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

def MsotFrequent(nums,k):
    #  We Know that to remove the duplicates we Use the Set Rule Because the Set Does not allow the Duplicate Values
    #  Insted of the Sets Can we us ethe Dictionary to stire the Frequency of the Elements
    #  We can use the Counter to get the Frequency of the Elements
    sets  = set(nums)
    d ={}
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    #  Her after that i have to sort the array oin the assending Order 
    for i in sets:
        
    

print(MsotFrequent([1,1,1,2,2,3],2))

