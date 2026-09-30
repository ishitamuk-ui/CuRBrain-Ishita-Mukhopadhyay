class Solution():
  def freq(self):
    n=int(input("enter the number"))
    n1=int(input("enter element 1"))
    n2=int(input("enter element 2"))
    c1=0
    c2=0
    if (n<0 or n2>9 or n1>9):
      print("invalid")
      return
    while(n>0):
      dig=n%10
      if(n1==dig):
        c1+=1
      elif(n2==dig):
        c2+=1
      n=n//10
    diff=abs(c1-c2)
    print(diff)
sol=Solution()
sol.freq()