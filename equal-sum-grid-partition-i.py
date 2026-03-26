import pytest

class Solution(object): 

    def canPartitionGrid(self, grid):
        n = len(grid)
        m = len(grid[0])

        top = 0
        bottom = sum(sum(row) for row in grid)
        for y in range(n):            
            crow = sum(grid[y])
            top += crow
            bottom -= crow 
            if top == bottom:
                return True

        left = 0
        right = sum(sum(row) for row in grid)
        for x in range(m):
            ccol = sum(row[x] for row in grid)
            left += ccol
            right -= ccol
            if left == right:
                return True

        return False
        

def test():
    s = Solution()

    assert s.canPartitionGrid([[1,4],[2,3]]) == True
    assert s.canPartitionGrid([[1,3],[2,4]]) == False
