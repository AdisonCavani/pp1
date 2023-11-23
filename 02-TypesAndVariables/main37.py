personal_data = "Mr. John May, born on 1998-02-16"

born = personal_data.split()

print(f"Description: {personal_data}")
print(f"Name: {personal_data[4:9]}")
print(f"Surname: {personal_data[9:12]}")
print(f"Initials: {personal_data[4]}{personal_data[9]}")
print(f"Born: {personal_data[-10:]}")
