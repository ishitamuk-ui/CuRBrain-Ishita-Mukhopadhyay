class Solution :
  def range(self):
    n=int(input("enter the no"))
    count=0
    for i in range(2,n):
      c=0
      for j in range(2,i):
        if(i%j==0):
          c+=1
      if(c==0):
        count+=1
    return count

sol=Solution()
print(sol.range())