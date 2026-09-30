class Solution:
  def pallin(self):
    n=int(input("enter the number"))
    copy=n
    rev=0
    while(n>0):
      dig=n%10
      rev=rev*10+dig
      n=n//10
    if(rev==copy):
      print("pallindrome")
    else:
      print("sum is ",rev+copy)

sol=Solution()
sol.pallin()

