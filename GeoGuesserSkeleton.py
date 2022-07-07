#libraries needed 
from random import randrange
import urllib
from tkinter import *
from PIL import ImageTk, Image #this is needed to open and display images of type png and jpeg
import requests #note: deleting this makes the urllib.request throw an error
import os #used to delete image at end

#Step 1: read from file and store into array
# open file "links.txt" and store each line as an element in an array
?

#Step 2: create a dict that stores the answer of each of URL
answerkey = {?}

#Step 3: randomly choose a URL from array and keep track of location (index) and answer by storing them in variables. 
# Hint: Use the dictionary you made to get the answer
# Hint: Use a function from the random library?
location = ?
answer = ?

#Step 4: download image from choosen URL
# urllib library is used to handle URLs. request functions are used to open and read URLs
# this website for more information on requests: https://docs.python.org/3/library/urllib.request.html
# For other urllib functions: https://www.geeksforgeeks.org/python-urllib-module/
# Hint: Look at urlretrieve function to extract and store image on local machine

?


#Step 5: resize image to make sure it looks decent in GUI using Image library and save it 

im = Image.open(?)
resized_im = 


#Step 5: display GUI with image, user input and enter button
# Create intial GUI and display image    
root = Tk() # creates an object of Tk class
            # Assign title to GUI
im = ? # open the image to be displayed
canvas = Canvas(?) #adjust canvas size of GUI 
# Use functions pack, PhotoImage and create_image to be able to display image as desired
?



# creating bottom part of GUI
bottomroot = Frame(root)
bottomroot.pack(?) # use pack to attach the new frame to the bottom of the root frame
Label(?) # Create a Label that allows the user to know that they have to Enter Location 
# Create an Entry Field and place it in the desired location on the GUI
?
# function that runs when you pressthe button is pressed
def func():
     ?
# Create an enter button, ensure it performs the desired action when pressed and place it in the desired location on the GUI
?

# display GUI
root.mainloop()

#Step 7: checker for answer

# Check if the answer inputed by the user is correct and display whether it is correct or wrong by creating a new smaller GUI's in each case
?

#Step 8: Delete photo
os.remove(?)
