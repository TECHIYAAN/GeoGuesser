#headers
from random import randrange
import urllib
from tkinter import *
from PIL import ImageTk, Image #this is needed to open and display images of type png and jpeg
import requests #note: deleting this makes the urllib.request throw an error
import os #used to delete image at end

#Step 1: read from file and store into array
with open('links.txt') as f:
    image_links = f.read().splitlines() #note: we want to get rid of "\n" which represents end of line
print(image_links)

#Step 2: create a dict that stores the answer of each of URL
answerkey = {0:"Uttar Pradesh, India", 1:"Mumbai, India", 2:"Delhi, India", 3:"Islamabad, Pakistan", 4:"Pokhara, Nepal", 5:"Telangana, India"}

#Step 3: randomly choose a URL from array and keep track of location and answer
location = randrange(len(image_links))
url = image_links[location]
answer = answerkey[location]
print("URL:", url, "is present at index:", location, "answer:", answer)

#Step 4: download image from choosen URL
# urllib library is used to handle URLs. request functions are used to open and read URLs
# this website for more information on requests: https://docs.python.org/3/library/urllib.request.html
# For other urllib functions: https://www.geeksforgeeks.org/python-urllib-module/

urllib.request.urlretrieve(url,"downloaded/geoguesser.png")

#Step 5: resize image to make sure it looks decent in GUI

im = Image.open("downloaded/geoguesser.png")
resized_im = im.resize((1000,700))
resized_im.save("downloaded/resized_geoguesser.png")

#Step 6: display GUI with image, user input and enter button

#function to store info in enter to "user_ans" and closes the screen
def func():
    global user_ans
    user_ans = e1.get()
    root.quit() #entry isn't read until root is closed

root = Tk() #creates an object of Tk class
root.title('GeoGuesser')
im = Image.open("downloaded/resized_geoguesser.png")
width, height = im.size
canvas = Canvas(root, width = width, height = height)
canvas.pack() #https://www.tutorialspoint.com/python/tk_pack.htm
img = ImageTk.PhotoImage(im) # This can be used everywhere Tkinter expects an image object. Website: https://pillow.readthedocs.io/en/stable/reference/ImageTk.html
canvas.create_image(20, 20, anchor=NW, image=img)

#creating bottom part of GUI
bottomroot = Frame(root)
bottomroot.pack(side= BOTTOM) #creates an additional frame atttahced to the bottom of the inital one
Label(bottomroot, text="Enter location").grid(row=0)
e1 = Entry(bottomroot)
e1.grid(row=0, column=1)
enter_button = Button(bottomroot, command=func, text="Enter", fg="black") #command field calls the func function when button is hit
enter_button.grid(row = 0, column = 2)

#display GUI
root.mainloop()

#Step 7: checker for answer
print(user_ans)

if (user_ans == answer):
    correct = Tk()
    Label(correct, text="Correct!", fg="green").pack()
    correct.mainloop()
else:
    wrong = Tk()
    Label(wrong, text="Wrong answer", fg="red").pack()
    wrong.mainloop()

#Step 8: Delete photo
os.remove("downloaded/geoguesser.png")
os.remove("downloaded/resized_geoguesser.png")