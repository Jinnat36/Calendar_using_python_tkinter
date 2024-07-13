# import all methods and classes from the tkinter 
from tkinter import *

# import calendar module
import calendar

# Function for showing the calendar of the given year
def showCal() :

	# Create a GUI window
	gui = Tk()
	
	# Set the background colour of GUI window
	gui.config(background = "white")

	# set the name of tkinter GUI window 
	gui.title("CALENDAR")

	# Set the configuration of GUI window
	gui.geometry("550x550")

	# get method returs current text as string
	fetch_year = int(year_field.get())

	# calendar method of calendar module return
	# the calendar of the given year .
	cal_content = calendar.calendar(fetch_year)

	# Create a label for showing the content of the calendar
	cal_year = Label(gui, text = cal_content, font = "Consolas 10 bold")

	# place method is used for placing 
	# the widgets at respective positions 
	cal_year.pack()
	
	# start the GUI 
	gui.mainloop()

# Driver Code
if __name__ == "__main__" :

	# Create a GUI window
	root = Tk()
	
	# Set the background colour of root window
	root.config(background = "skyblue")

	# set the name of tkinter root window 
	root.title("CALENDAR")

	# Set the configuration of root window
	root.geometry("400x300")

	# Create a CALENDAR : label with specified font and size
	cal = Label(root, text = "CALENDAR",font = ("times", 30, 'bold'),fg="navy blue",background="skyblue")

# Create a label to display the image
	image = PhotoImage(file="cal.png")
	image_label = Label(root, image=image,background="skyblue").place(x=130,y=60)

	# # Create a Enter Year : label 
	year = Label(root, text = " Enter Year : " , bg = "skyblue",fg="navy blue",font=("times",15, 'bold'))

	
	# Create a text entry box for filling or typing the information. 
	year_field =Entry(root,width=10,bd=3)


	# Create a Show Calendar Button and attached to showCal function
	Show = Button(root, text = "Show Calendar",bg = "Red", command = showCal,bd=3)

	exit = Button(root, text = "Exit",bg = "Red", command = exit,bd=3)
	
	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure.
	cal.place(x=90,y=10)

	year.place(x=100,y=210)

	year_field.place(x=220,y=215)

	Show.place(x=120,y=250)
	
	exit.place(x=240,y=250)

	# start the root 
	root.mainloop()	
