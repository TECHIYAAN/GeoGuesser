# Techiyaan Codespire: GeoGuesser
### What is a GeoGuesser?

GeoGuesser is a game that lets you “travel the world” and tests your knowledge of the world we live in. It does this by displaying images of landmarks in the world and asks the user to enter the place where the landmark is located in a text box. If the user answers correctly, they win the round. 
 ***You have been provided with a skeleton file for this game.***  The following is a more detailed description of how to approach coding this game. 

### What are the steps needed to make such a game?
#### 1.	Selecting and accessing the images to display: 
This can be done in many ways. You could possibly download the images on your local machine and access these photos or you could try to read a dataset of images. In this project, we encourage you to compile a list of urls that lead to images in a text file. This file should then be read and used to extract the photos to display using a library, urllib. For more information, look at: https://docs.python.org/3/library/urllib.request.html
#### 2.	Storing the correct the answers 
Now that you have the images you want to display, you need to be able to associate these images with their answers. Like most programming problems, there are many ways to approach this. We suggest using a python data structure called dictionaries for this. A dictionary allows you to store variables in pairs. For more information, look at : https://www.w3schools.com/python/python_dictionaries.asp 
#### 3.	Randomly choose one of the images to display
You can use a python library called random to do this. For more information, look at: https://docs.python.org/3/library/random.html
#### 4.	Create the User Interface 
There are multiple ways to display a GUI (Graphic User Interface) in python due to the abundance of libraries. In this project, we will use tkinter library, we will use functions and classes from this library to display the image and take in the user input. For more information, look at: https://docs.python.org/3/library/tkinter.html
#### 5.	Check if the user answered correctly 
Now that you have the user answer, you need to check if the answer is correct. This can be done using a simple if statement. Once you know the status of the answer, you should display to the user if they were correct or wrong. This can also be done using a small GUI. 
### Basic Concepts Covered  
1.	File I/O 
2.	URL Handling 
3.	Arrays
4.	Dictionaries 
5.	GUI Building
6.	Image reading and modification 
7.	Reading user input 
8.	Importing Libraries 
9.	Randomization 
10.	Functions 

### Libraries used
1.	random (randrange)
2.	urlib
3.	requests
4.	tkinter
5.	PIL (Image and ImageTk)
6.	os 
#### Expectations and Deliverables 
You are expected to submit:
### a.	GeoGuesser.py
When the file runs, a GUI is expected to appear with the image and textbox. When the answer is entered, the user should be informed whether or not their answer is right or wrong accurately. 
### b.	Links.txt
This file should contain the list of urls from which the photos have been extracted. 

***Always feel free to ask questions during class or reach out to us via email: techiyaanstem@gmail.com*** 
