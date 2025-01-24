# turtle-crossing-game
Turtle Crossing Game

This project is a simple Turtle Crossing game implemented in Python using the turtle module. The objective of the game is to help the turtle cross the road while avoiding moving cars. With each successful crossing, the game level increases, making the cars move faster. If the turtle collides with a car, the game ends.

1.Features

> Player Movement: The player controls a turtle that moves upward when the "Up" arrow key is pressed.

> Car Manager: Cars appear randomly on the screen and move horizontally across the screen.

> Scoreboard: Displays the current level at the top-left of the screen and shows "GAME OVER" when the game ends.

> Difficulty Progression: The speed of the cars increases with each level.

2.How It Works

> Game Initialization: The screen is set up with a size of 600x600 pixels, and the game starts with a turtle at the bottom of the screen.

> Player Controls: The player can move the turtle upward using the "Up" arrow key.

> Car Generation: Cars are generated at random intervals and positions and move from right to left.

> Collision Detection: If a car comes within 20 units of the turtle, the game ends.

> Level Up: If the turtle successfully crosses to the other side, the level increases, car speed increases, and the scoreboard updates.

> Game Over: The game ends when the turtle collides with a car, and "GAME OVER" is displayed.

3.Classes

i. Player

Handles the turtle's movement and tracks when the player finishes crossing.

Methods:

> move(): Moves the turtle upward.

> finish(): Checks if the turtle has reached the top of the screen.

> go_to_start(): Resets the turtle's position to the starting point.

ii. CarManager

Manages the creation and movement of cars.

Attributes:

> all_cars: A list of all the car objects.

> car_speed: The speed at which cars move.

Methods:

> create_car(): Creates a new car at a random position.

> move(): Moves all cars on the screen.

> level_up_speed(): Increases the speed of the cars as the level progresses.

iii. Scoreboard

Displays the current level and the game-over message.

Methods:

> increase_level(): Updates the level display when the player finishes crossing.

> game_over(): Displays "GAME OVER" when the game ends.

Installation and Usage

Prerequisites

Python 3.x installed on your system.

4.Clone the Repository

git clone <repository-link>
cd turtle-crossing-game

5.Run the Game

Ensure you have the required Python version.

Run the main.py file:

python main.py

Use the "Up" arrow key to control the turtle.

File Structure

|-- main.py                # Main game logic
|-- player.py              # Player class implementation
|-- car_manager.py         # CarManager class implementation
|-- scoreboard.py          # Scoreboard class implementation
|-- README.md              # Project documentation

Customization

Screen Dimensions: Modify screen.setup(width=600, height=600) in main.py to change the game screen size.

Car Speed: Adjust the initial speed in the CarManager class.

Level Display: Customize the font, position, or style of the scoreboard in the Scoreboard class.

Future Improvements

Add more player controls for side-to-side movement.

Implement more obstacles or challenges.

Add sound effects and background music.

License

This project is open-source and available under the MIT License.

Acknowledgements

This project was created for learning purposes and demonstrates the use of Python's turtle module to build interactive games.

