from tkinter import *
import matplotlib.pyplot as plt
user_data = {}
def calculate_bmi(weight, height):
  bmi = weight / (height * height)
  return bmi

def update_bmi():
  try:
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    username = username_entry.get()

    if not username:
      raise ValueError("Please enter a username")

    bmi = calculate_bmi(weight, height)
    bmi_label.config(text=f"Your BMI: {bmi:.2f}")

    user_data[username] = {"weight": weight, "height": height, "bmi": bmi}
  except ValueError as e:
    print(f"Error: {e}")
    error_label.config(text=f"Error: {e}", fg="red")
  else:
    error_label.config(text="")

def view_data():
  data_window = Toplevel(root)
  data_window.title("User Data")
  data_text = Text(data_window)
  data_text.pack()
  if not user_data:
    data_text.insert(INSERT, "No data stored yet!")
  else:
    data_text.insert(INSERT, "Username\tBMI\n")
    for username, data in user_data.items():
      data_text.insert(INSERT, f"{username}\t{data['bmi']:.2f}\n")

def plot_trends(username):
  if username not in user_data:
    print(f"No data for user: {username}")
    return
  bmi_data = [data["bmi"] for data in user_data[username].values()]
  plt.plot(bmi_data)
  plt.xlabel("Data Point")
  plt.ylabel("BMI")
  plt.title(f"BMI Trend for {username}")
  plt.show()

root = Tk()
root.title("BMI Calculator")
username_label = Label(root, text="Username:")
username_label.pack()
username_entry = Entry(root)
username_entry.pack()
weight_label = Label(root, text="Weight (kg):")
weight_label.pack()
weight_entry = Entry(root)
weight_entry.pack()
height_label = Label(root, text="Height (m):")
height_label.pack()
height_entry = Entry(root)
height_entry.pack()
calculate_button = Button(root, text="Calculate BMI", command=update_bmi)
calculate_button.pack()
bmi_label = Label(root, text="Your BMI:")
bmi_label.pack()
error_label = Label(root, text="")
error_label.pack()
view_data_button = Button(root, text="View Data", command=view_data)
view_data_button.pack()
menu = Menu(root)
trend_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Analyze Trends", menu=trend_menu)

def analyze_trends():
  username = username_entry.get()
  if username:
    plot_trends(username)
  else:
    print("Please enter a username")

trend_menu.add_command(label="Plot BMI Trend", command=analyze_trends)
root.config(menu=menu)

root.mainloop()
