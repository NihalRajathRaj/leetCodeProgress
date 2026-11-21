class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
       number = 0
       result = []
       digits = digits[::-1]
       for i in range(len(digits)):
            number += ((10**i) * digits[i])
       number += 1
       for j in str(number):
            result.append(int(j))
       return result