**Let’s introduce Space Fleet Manager!**

**Introduction**

In this game, you take on the role of a space fleet manager. You need to recruit crew members, maintain your spaceships in good condition, and handle various random events to keep your fleet operational.

**Required Libraries**

*Standard Modules*

These libraries are included by default with Python:

•  **json**: for reading and writing data in JSON format.

•  **random**: for generating random events.

•  **atexit**: for running a function before the program closes.

**Custom Files**

The following files must be in the same directory as the main script:

•  **fleet.py**: defines fleet management functionalities.

•  **spaceship.py**: contains spaceship characteristics.

•  **crew.py**: manages the crew.

•  **Operator.py**: for specialized operators.

•  **mentalist.py**: for characters with special abilities.

•  **member.py**: for basic crew members.

**Installation and Setup**

1.  **Install Python**: Download and install [Python 3.10 or higher](https://www.python.org/downloads/).

2.  **File Organization**:

•  Place all files (fleet.py, spaceship.py, etc.) in the same directory as the main script.

3.  **Data Initialization**:

•  Run the script once to create a fleet.json file. This file will contain the game settings.

**How to Play**

**1. Starting the Game**

•  When you start the game, the program will automatically load saved data if the “Auto Load” option is enabled.

•  Otherwise, the game will start with an empty fleet.

**2. Main Menus**
•  Allow you to manage all the fleet
•  Save your game
•  Access to settings
•  Quit (and auto save on exit if enabled)
  
The game is organized into menus:

•  **Fleet Management**:

•  Add, modify, or remove spaceships.

•  Display detailed fleet information.

•  **Spaceship Management**:

•  Add or remove crew members.

•  Modify the spaceship’s status (operational, damaged, destroyed).

•  Run readiness checks.

•  **Crew Management**:

•  Assign roles or increase crew members’ experience.

•  Perform actions specific to their roles.

•  **Random Events**:

•  Unexpected events may affect your spaceships.

**3. Commands**

•  The menus display numbered options.

•  Simply enter the corresponding number for your choice.

**4. Saving and Loading**

•  Game data is automatically saved upon closing  (if enabled in settings).

•  You can load previous data on startup.

**Main Features**

**Initialization**

•  The JSON file is created automatically if absent.

•  Default settings include:

•  Auto-save (if enabled in settings).

•  Auto-load data (if enabled in settings).

**Fleet Management**

•  Add spaceships with custom names, types, and conditions.

•  Remove spaceships or modify their characteristics.

**Crew Management**

•  Add crew members with specific roles (pilot, technician, mentalist, etc.).

•  Gain experience or use special abilities to improve performance.

**Random Events**

•  Spaceships may be randomly damaged or destroyed.

•  These events add challenge to managing your fleet.

**Main Commands**  

Here are some basic commands you can use:

•  **Show Settings**: View and modify game options.

•  **Add a Spaceship**: Enhance your fleet by adding spaceships.

•  **Manage a Crew Member**: Customize the roles and skills of your crew.

**Example Session**

1.  Start the game.

2.  Access the main menu.

3.  Add a new spaceship to your fleet.

4.  Recruit a crew for the spaceship.

5.  Manage random events to ensure your fleet’s survival.
