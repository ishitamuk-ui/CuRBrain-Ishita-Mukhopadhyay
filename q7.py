import math
class Solution:
  def arraygcd(self):
    arr=[]
    n=int(input("enter the number of elements"))
    for i in range(n):
      i=int(input("enter the element"))
      arr.append(i)
    gcd=math.gcd(*arr)
    return gcd

sol=Solution()
print(sol.arraygcd())
  