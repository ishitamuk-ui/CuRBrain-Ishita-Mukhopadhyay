class Solution:
  def count(self):
    n=int(input("enter the number"))
    count=0
    while(n>0):
      dig=n%10
      count+=1
      n=n//10
    if (count%2==0):
      print("True")
    else:
      print("False")

sol=Solution()
sol.count()