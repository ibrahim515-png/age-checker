
name = input("Enter your name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")

print(f"Hello {name}, you are {age} years old from {country}.")

if age >= 18:
    print(f"Hello {name}, welcome to {country}.")
else:
    print(f"آسف يا {name}، أنت صغير وغير مسموح لك بالدخول.")
