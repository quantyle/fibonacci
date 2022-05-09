class Solution(object):
    def fib_iterative(self, n):
        '''
        iterative solution:
        '''
        res = 0
        a = 0
        b = 1
        
        for _ in range(n):
            a = res + b
            res = b
            b = a
        
        return res
        
    def fib_recursive(self, n):
        '''
        recursive solution
        '''        
        # 0 and 1 are unique cases, so just return them directly
        if n <= 1: return n
        
        # use the formula F(n) = F(n - 1) + F(n - 2) for all values n > 1
        res = self.fib_recursive(n - 1) + self.fib_recursive(n - 2)
        
        return res
        

'''
driver program
'''        
inputs = [1, 2, 3, 4, 5, 6, 7, 9, 10, 20, 25, 30]
solution = Solution()

'''
test iterative solution
'''
print("\n================ Iterative Fibonnaci ================ ")
for i in inputs: 
    res = solution.fib_iterative(i)
    print("F(%d)= %d" % (i, res))

'''
test recursive solution
'''
print("\n================ Recursive Fibonnaci ================ ")
for i in inputs: 
    res = solution.fib_recursive(i)
    print("F(%d)= %d" % (i, res))


