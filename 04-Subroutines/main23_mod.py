def letter_count(text, letter):
  count = 0

  for i in text:
    if i == letter:
      count += 1

  return count