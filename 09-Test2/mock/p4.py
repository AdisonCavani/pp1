def f(subjects: dict):
  avg_arr = []

  for sub in subjects:
    sum = 0
    count = 0

    for num in subjects[sub]:
      sum += num
      count += 1

    avg_arr.append(sum / count)

  max = 0
  max_idx = -1

  for idx, val in enumerate(avg_arr):
    if max < val or max_idx == -1:
      max = val
      max_idx = idx
  
  for idx, val in enumerate(subjects):
    if idx == max_idx:
      return val

obj = {
  "math": [3, 4, 4],
  "geo": [5, 4, 4, 4],
  "comp": [5, 4]
}

print(f(obj))
