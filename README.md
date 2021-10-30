# Speed
Think you can type faster than your peers? Start a <i>Speed</i> 
tournament and you'll know! The rules are simple. Type the words you 
see as they move across the screen. Press enter to clear the buffer at 
any time. Type a word correctly and your score goes up.

## Getting Started
Make sure you have Python 3.8.0 or newer and asciimatics 1.12.0 or new installed 
and running on your machine. You can install Asciimatics by opening a terminal 
and running the following command.
```
python3 -m pip install asciimatics
```
After you've installed the required libraries, open a terminal and browse to the 
project's root folder. Start the program by running the following command.
```
python3 speed 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE 
and open the project folder. Select the main module inside the hunter folder and 
click the "run" icon.

## Project Structure
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- speed               (source code for game)
  +-- game              (specific game classes)
  +-- __init__.py       (python package file)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies
* Python 3.8.0
* Asciimatics 1.12.0

## Authors
* Tianna DeSpain - des17015@byui.edu
* Nephi Malit - byui@nephi.malit.me

## Basic Features
* The game begins with five words moving on the screen.
* The player tries to type the words they see on the screen.
* The player earns points for the words they type correctly.
* If the player presses the enter key their buffer is cleared.
* Play continues until the player presses the ESC key.

## Extra Features
* One in every twenty words has x5 bonus, identifiable by being uppercase
* A word counter in addition to the scoreboard, displaying the number of words completed
* Explosion animation displayed for words when they are typed correctly