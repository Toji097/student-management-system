import tkinter as tk

#When I call the tkinter library it allows me to use tools  to create a GUI that allows the use of buttons, labels and widgets.

root = tk.Tk()
#This essentially creates a main window for the application,we can use another other than root but root is a common convention.
#We also use Tk() in the tkinter library to create the main window.(Tk is a class in the tkinter library)


root.title("Management")
#This sets the title of the main window to "Management" and you will see this title at the top of the main window. It's like when I open vs code you see the symbol on the top right although it is old style.


appLabel = tk.Label(root, text = "Student Management System", fg = "#06a099", width = 35)
appLabel.config(font = ("Sylfaen", 30))
#This makes the title you will see in large on the main window, think of it like a chapter title in a book.
appLabel.grid(row = 0, columnspan = 2, padx = (10, 10), pady = (30, 10))
#This basically places the label in the middle, it takes a invisible grid and places the label in the location specified by row and column.

#Now I will make some 
nameLabel = tk.Label(root, text = "Enter your name", width = 40, anchor = "w", 
                     font = ("sylfaen", 12)).grid(row = 2, column = 0, padx(10, 0), pady = (30, 0))

root.mainloop()
#This is the main loop of the application, it keeps the window open and waits for user interaction,I added it at the end of the code to ensure that the window stays open until the user closes it.