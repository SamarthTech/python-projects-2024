# Description of the Python File

This is a graphical user interface (GUI) application of a dice roller developed using the Tkinter library. The resulting Python file reflects an implementation of a simple dice rolling application with the following functionality.

#### Roll Dice Button:

- When the "Roll the Dice" button is clicked, the application executes this action by simulating the roll of the dice. It then gives such an impression by showing animations on the faces of the dice for a short time.
- The face of the dice flickers a few times in rapid succession and, thus recreates the visual effect of a rolldice.
- The face of dice is randomly chosen from six different images describing sides of the die.

### Show Dice Roll:

- After the animation is done, it displays the final face on the screen.
- A message appears showing the value of the dice (e.g. "You rolled a 5!"), matched to the face shown

### Graphical User Interface (GUI):

- It has an user-friendly interface, titled with a large-sized picture of the dice and a button to roll the dice.
- Images of the dice are scaled appropriately to fit inside the window of the GUI.
### Responsive GUI:
- The application automatically changes the size of its window to fit itself on the different types of screen resolution so it always looks good on those.

## Commands to Run This File:

Install libraries you require To work with images, you'll need Pillow library. You install it to your virtual environment with the command
> pip install pillow

### Directory Structure: 
- Make sure that your project directory contains a folder named dice, which holds the dice images (dice1.png to dice6.png).
- Make sure that your project open 'Dice roller with GUI' folder not the python-projects-2024