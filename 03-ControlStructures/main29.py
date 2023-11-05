washing_product = "shoes"
rinse = True
spin = False

time = 0

if washing_product == "jacket":
    time += 40
elif washing_product == "underwear":
    time += 70
else:
    time += 20

if rinse:
    time += 15
if spin:
    time += 9

print(f"Total washing time: {time} minutes")