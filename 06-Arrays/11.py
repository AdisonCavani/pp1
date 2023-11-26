def month(f):
    arr = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return arr[f - 1]

month_num = int(input("Enter month number: "))
print(f"Month name: {month(month_num)}")