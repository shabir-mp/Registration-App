import tkinter
from tkinter import ttk, messagebox
line = "-"*40
def enter_data():
  accepted = accept_var.get()
  if accepted =="Accepted":
    firstname =  first_name_entry.get()
    lastname = last_name_entry.get()
    if firstname and lastname:
        title = title_combobox.get()
        age = age_spinbox.get()
        nationality = nationality_combobox.get()
        numcourses = numcourses_spinbox.get()
        numsemester = numsemesters_spinbox.get()
        reg_status = reg_status_var.get()
        data = (f"First Name: {firstname}\nLast Name: {lastname}\nTitle: {title}\nAge: {age}\nNationality: {nationality}\nCourses: {numcourses}\nSemesters: {numsemester}\nRegistration Status: {reg_status}\n{line}\n")
        print(data)
        f = open("registrationdata.txt","a+")
        f.write(data)
        f.close()
    else:
       tkinter.messagebox.showwarning(title="Name Error", message="First name and last name are required")
  else:
    tkinter.messagebox.showwarning(title="Terms and Condition Error", message="Please Accepted the Terms and Conditions")

window = tkinter.Tk()
window.title("Registration App")

frame = tkinter.Frame(window)
frame.pack()

#Save User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row= 0 ,column= 0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0 ,column=0)

last_name_label = tkinter.Label(user_info_frame, text="Last Name" )
last_name_label.grid(row=0 ,column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1 , column=0)
last_name_entry.grid(row=1 , column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, value=["", "Mr.", "Mrs."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=13, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text= "Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa","Antartica","Asia","Europe",])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Save Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)


registered_label = tkinter.Label(courses_frame, text="Registration Status")
reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered", variable=reg_status_var, onvalue="Registered", offvalue="Unregistered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Accept Terms
terms_frame = tkinter.LabelFrame(frame, text="Terms and Conditions")
terms_frame.grid(row=2,column=0,sticky='news',padx=20,pady=10)
accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0,column=0)

#Button
button = tkinter.Button(frame, text="Submit", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
tkinter.messagebox.showinfo(title="Thankyou", message="Thankyou for using Registration App by @shabirmp. This application is a registration simulation application. Please use as needed.")
