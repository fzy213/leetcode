class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        index = []
        numto = num[:];
        for i in range(0,len(numto)):
            for j in range(i+1,len(numto)):
                if numto[j]==target-numto[i]:
                    index.append(i)
                    index.append(j)
                    return (index[0],index[1])
if __name__ == '__main__':
    num = [2,5,5,11]
    target = 10
    solution = Solution()
    print solution.twoSum(num,target)

		
