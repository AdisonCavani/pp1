def f(arr2D: list):
  sum_arr = []

  for arr in arr2D:
    arr = list(arr)
    sum = 0

    for num in arr:
      sum += num
    
    sum_arr.append(sum)
  
  for sum in sum_arr:
    if sum_arr.count(sum) > 1:
      return True

  return False

if __name__ == "__main__":
  print(f([[3,4,2],[5,1,6]]))
  print(f([[3,4,2],[5,1,7]]))
  print(f([[3,4],[5,1],[4,7]]))
  print(f([[3,4],[5,9],[4,7]]))