def f(fnc, prods: list):
  string = ""

  for idx, prod in enumerate(prods):
    if idx == 0:
      string += fnc(prod)
    else:
      string += "," + fnc(prod)

  return string

if __name__ == "__main__":
  prods = ["water", "cheese", "tomato"] 

  fnc1 = lambda x: "id:" + x[:2] 
  print(f(fnc1, prods))

  fnc2 = lambda x: (x[0] + x[-1]).upper()
  print(f(fnc2, prods))