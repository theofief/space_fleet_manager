# 🚀 Space Fleet Manager – Text-Based Fleet Management Game

**Space Fleet Manager** is a command-line game where you take on the role of a space fleet manager. Recruit crew members, maintain your spaceships, and handle random events to keep your fleet running strong.

---

## 📦 Required Libraries

### 🔹 Standard Python Modules

- `json`: read and write data in JSON format  
- `random`: generate random events  
- `atexit`: run functions before the program exits

### 🔹 Custom Files (must be in the same directory as the main script)

- `fleet.py`: fleet management functions  
- `spaceship.py`: spaceship attributes  
- `crew.py`: crew member handling  
- `Operator.py`: special operator characters  
- `mentalist.py`: characters with unique abilities  
- `member.py`: base crew member logic

---

## 🛠️ Installation & Setup

1. **Install Python**  
   Download and install [Python 3.10 or higher](https://www.python.org/downloads/)

2. **File Organization**  
   Place all Python files listed above in the same folder as the main script

3. **Data Initialization**  
   Run the script once to automatically generate `fleet.json` (contains save data and settings)

---

## 🎮 How to Play

### 1. Starting the Game

- If **Auto Load** is enabled, the game loads previous data automatically  
- Otherwise, it starts with an empty fleet

### 2. Main Menus

- 🛸 **Fleet Management**: add, modify, remove spaceships, view fleet info  
- 👨‍🚀 **Crew Management**: recruit crew, assign roles, level up members  
- ⚙️ **Settings**: toggle auto-save/load, adjust options  
- 💾 **Save & Load**: automatic save on exit (if enabled)  
- ❌ **Quit**: exit the game safely (auto-save if enabled)

### 3. Menu Navigation

- Menus use numbered options  
- Just enter the number corresponding to your choice

---

## ✨ Main Features

### ✅ Auto Initialization

- Automatically creates `fleet.json` if not found  
- Default options include disabled auto-save/load (can be toggled in settings)

### 🛸 Fleet Management

- Add custom spaceships (name, type, condition)  
- Modify or delete ships  
- Display full fleet overview

### 👨‍🚀 Crew Management

- Add crew with specific roles (pilot, technician, mentalist, etc.)  
- Improve their experience  
- Use their special abilities in missions

### 🌌 Random Events

- Spaceships may be damaged or destroyed randomly  
- Events bring unpredictability and challenge to gameplay

---

## 🧪 Example Session

1. Launch the game  
2. Open the main menu  
3. Add a new spaceship  
4. Recruit a crew  
5. Handle random events and manage your fleet wisely

---

*Feedback and contributions are welcome!*
