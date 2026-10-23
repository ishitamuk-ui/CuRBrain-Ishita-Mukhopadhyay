class solution:
  def score(self):
    n=int(input("enter the number of element"))
    arr=[]
    for i in range(n):
      ele=int(input("enter the scores"))
      arr.append(ele)
    ar=[]
    for i in arr:
      if i not in ar:
        ar.append(i)
    for i in range(len(ar)):
      for j in range(0,len(ar)-1-i):
        if (ar[j]>ar[j+1]):
          temp=ar[j]
          ar[j]=ar[j+1]
          ar[j+1]=temp
    if len(ar)>2:
      print(ar[-2])
    else:
      print(-1)

sol=solution()
sol.score()