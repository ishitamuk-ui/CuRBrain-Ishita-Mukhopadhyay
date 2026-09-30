class Solution:
  def reverse(self):
    n=int(input("enter the number"))
    rev=0
    copy=n
    if (n<0):
      n=-(n)
    while(n>0):
      dig=n%10
      rev=rev*10+dig
      n=n//10
    if(copy<0):
      print("the reverse and double number is -",rev*2)
    else:
      print("the reverse and double number is ",rev*2)

sol=Solution()
sol.reverse()