def calculate_bmi(weight, height):
  bmi = weight / (height * height)
  return bmi

def bmi_category(bmi):
  if bmi < 18.5:
    category = "Underweight"
  elif bmi < 25:
    category = "Normal weight"
  elif bmi < 30:
    category = "Overweight"
  else:
    category = "Obese"
  return category


weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"Your BMI is: {bmi:.2f}")
print(f"BMI Category: {category}")
