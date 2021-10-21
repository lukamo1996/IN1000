## This gets the length of the array
def lengthGetter(el):
  return len(el)

## This swaps the arrays
def swapThem(i1, i2, arr):
  if i2 and type(i2) == "int":
    print(2323)
    temp = arr[:]
    arr[i1] = arr[i2]
    arr[i2] = arr[temp]

## This sorts the arrays in sortingArray based on index 0
def sorter(arr):
    for i in range(0, len(arr) - 1, 1):
        if len(arr[i]) == len(arr[i + 1]):
            if(arr[i][0] > arr[i + 1][0]):
                swapThem(int(i), int(i) + 1, arr)

## This solves the problem
def solve(arr):
  hash = {}
  sortingArr = []
  for el in arr:
    if el in hash: hash[el] = hash[el] + 1
    else: hash[el] = 1
  print(hash)
  for el in hash.keys():
    tempArr = []
    for i in range(0, hash[el], 1):
      tempArr.append(el)
    sortingArr.append(tempArr)
  sortingArr = sorted(sortingArr, key = lengthGetter, reverse = True)

  print(sortingArr)
  sorter(sortingArr)
  print(sortingArr)

solve([4,9,5,0,7,3,8,4,9,0])