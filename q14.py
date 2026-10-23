class Sol:
  def sales(self):
    n=int(input("enter the number of element"))
    arr=[]
    for i in range(n):
      ele=int(input("enter the sales"))
      arr.append(ele)
    threshold=int(input("enter the threshold value"))
    ar=[]
    for i in range(n):
      if(arr[i]>=threshold):
        ar.append(arr[i])
    l=len(ar)
    for i in range(l):
      print(ar[i])

solution=Sol()
solution.sales()