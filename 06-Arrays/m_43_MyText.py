def words_count(text: str):
  return len(text.split(" "))

def ordered_array(text: str):
  arr = text.split(' ')
  
  arr.sort(key=len, reverse=True)

  return arr

def alphabetically_ordered(text: str):
  arr = text.split(' ')
  arr.sort()

  return arr