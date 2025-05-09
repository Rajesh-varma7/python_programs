try:
  age = int(input("Enter your Age"))
except:
  print("There is an error")
else:
  if age >= 18:
    print("You are eligible")
  else:
    print("You are not eligible")
finally:
  print("Thanks for Register")
  
