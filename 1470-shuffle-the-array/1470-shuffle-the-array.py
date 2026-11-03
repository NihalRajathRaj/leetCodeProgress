class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i=0
        j=n
        k=0
        result=[]
        while i<j and k<2*n:
            if(n==1):
                return nums
            if(k%2==0):
                result.append(nums[i])
                k+=1
                i+=1
            else:
                result.append(nums[j])
                k+=1
                j+=1
        return result