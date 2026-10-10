class Solution:
  def nextprime(self):
    n=int(input("enter the number"))
    i = n + 1
    while True:
            count = 0
            
            limit = int(i ** 0.5)
            for j in range(2, limit + 1):
                if (i % j == 0):
                    count += 1
                    break 
                    
            if count == 0 and i >= 2:
                return i
            else:
                i+=1
          

sol=Solution()
print(sol.nextprime())
      