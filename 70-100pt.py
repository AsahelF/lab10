##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!
rectangle1 = drawpad.create_rectangle(300,200,500,400, fill = 'purple')
line1 = drawpad.create_line(300,200,400,100) 
line2 = drawpad.create_line (500,200,400,100)

#Door
door = drawpad.create_rectangle(380,330,420,400, fill = 'yellow')

#Windows
window1 = drawpad.create_rectangle(325,230,375,280, fill = 'yellow')
window2 = drawpad.create_rectangle(425,230,475,280, fill = 'yellow')

root.mainloop()
