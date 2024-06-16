def calculate_bmi(weight, height):
  """Calculates the Body Mass Index (BMI) for a given weight and height.

  Args:
      weight: Weight in kilograms (kg).
      height: Height in meters (m).

  Returns:
      The calculated BMI value.
  """

  bmi = weight / (height * height)
  return bmi

def bmi_category(bmi):
  """Classifies BMI into categories based on predefined ranges.

  Args:
      bmi: The calculated BMI value.

  Returns:
      The BMI category (e.g., underweight, normal, overweight).
  """

  if bmi < 18.5:
    category = "Underweight"
  elif bmi < 25:
    category = "Normal weight"
  elif bmi < 30:
    category = "Overweight"
  else:
    category = "Obese"
  return category

# Get user input
weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

# Calculate BMI and category
bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

# Display results
print(f"Your BMI is: {bmi:.2f}")
print(f"BMI Category: {category}")
