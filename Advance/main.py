from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

user_data = {}

def calculate_bmi(weight, height_cm):
   
    height_m = height_cm / 100.0
    bmi = weight / (height_m * height_m)
    return bmi

def update_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())
        username = username_entry.get()

        if not username:
            raise ValueError("Please enter a username")

        bmi = calculate_bmi(weight, height_cm)
        bmi_label.config(text=f"Your BMI: {bmi:.2f}")

        user_data[username] = {"weight": weight, "height_cm": height_cm, "bmi": bmi}

    except ValueError as e:
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

   
    bmi_data = [data["bmi"] for data in user_data.values() if data["bmi"]]
    if len(bmi_data) < 2:
        error_label.config(text="Insufficient data to plot trend", fg="red")
        return

    plt.figure(figsize=(8, 5))
    plt.plot(bmi_data, marker='o', linestyle='-')
    plt.xlabel("Data Point")
    plt.ylabel("BMI")
    plt.title(f"BMI Trend for {username}")
    
    
    canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

def analyze_trends():
    username = username_entry.get()
    if username:
        plot_trends(username)
    else:
        error_label.config(text="Please enter a username", fg="red")

root = Tk()
root.title("BMI Calculator")


input_frame = Frame(root)
input_frame.pack(padx=10, pady=10)

label_frame = Frame(input_frame)
label_frame.pack(side=LEFT)

entry_frame = Frame(input_frame)
entry_frame.pack(side=LEFT)


username_label = Label(label_frame, text="Username:")
username_label.pack()

username_entry = Entry(entry_frame)
username_entry.pack()


weight_label = Label(label_frame, text="Weight (kg):")
weight_label.pack()

weight_entry = Entry(entry_frame)
weight_entry.pack()


height_label = Label(label_frame, text="Height (cm):")
height_label.pack()

height_entry = Entry(entry_frame)
height_entry.pack()


calculate_button = Button(root, text="Calculate BMI", command=update_bmi)
calculate_button.pack()


bmi_label = Label(root, text="Your BMI:")
bmi_label.pack()


error_label = Label(root, text="", fg="red")
error_label.pack()

# View Data button
view_data_button = Button(root, text="View Data", command=view_data)
view_data_button.pack()


menu = Menu(root)
root.config(menu=menu)
trend_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Analyze Trends", menu=trend_menu)
trend_menu.add_command(label="Plot BMI Trend", command=analyze_trends)

root.mainloop()
