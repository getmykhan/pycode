a = [7, 9, 10 , 13, 14, 17, 19,20]

b = 17

mid = len(a) //2

if a[mid] < b:
  print("true")
  min_ = (len(a) - mid)
  #print(min_)

  for i in range(min_):
    mid = mid + 1
    if a[mid] == b:
      print("Greater than side")
      print("It is at index", mid)
      break

elif a[mid] == b:
  print("Equal")


elif a[mid] > b:
  print("lola")
  min_ = (len(a) - mid)

  for i in range (min_, 0, -1):
    mid = mid - 1
    if a[mid] == b:
      print("Yes Less than")
      break

else:
  print("Element does not exist in the list")