height = float(input("Enter your height in m:")
weight = float(input("Enter your weight in kg:")

bmi = float(f"{weight/(height*2):.2f"}

if bmi < 18.5:
  print(f"Your bmi is {bmi}:, You are underweight.")
elif bmi < 25:
  print(f"Your bmi is {bmi}:, You are normal.")
elif bmi < 30:
  print(f"Your bmi is {bmi}:, You are overweight.")
else:
  print(f"Your bmi is {bmi}:, You are Obese.")
