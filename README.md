# Agarpyo 🧩
> Welcome to Agarpyo, a reimagined version of the agar.io game.

## Project Overview 🎯

Agarpyo puts players in control of a character navigating through an environment filled with challenges and obstacles. The main objective is to collect resources, evade traps, and compete against other players to emerge as the ultimate champion.

## Prerequisite 🛟

Before you begin, ensure you have  [Anaconda](https://www.anaconda.com/download) installed 🐍
You don't need to install python separately.

## Set up the environnement 🛠️

1. Start Anaconda 🐍
2. In the menu, select **Environments**
3. At the bottom, click on **Create** 
4. Name this environments, for example : _Agarpyo_
5. Select the version : _Python 3.10.13_
6. Click on **Create**
4. In the menu, select **Home**
5. At the top, select the newly environment (here, _Agarpyo_)
6. Open VSCode, by clicking on **Launch** button

## Run the project 🚀

1. Open VSCode terminal and check if your environment is activated with this command :
```bash
conda activate Agarpyo
```
2. Next, you just need to install `pygame` in your environment
```bash
pip install pygame
```
3. Open the VSCode terminal and clone this repository
```bash
git clone https://github.com/B2-Info-23-24/agarpyo-b2-b-vincmgn
cd agarpyo-b2-b-vincmgn
```
4. Finally, start the program
```bash
python main.py
```

## Features 🎮

#### ➜ Menu:
- By default, the game starts in `Easy` difficulty and with `keyboard` control.
- The player can be controlled either by **`keyboard`** (W, A, S, D) or by **`mouse`**.
- Players can choose the game difficulty using **checkboxes**, with the options being:
    - `Easy`: Provides 5 food, 2 traps, and a speed of 100.
    - `Normal`: Provides 3 food, 3 traps, and a speed multiplier of 1.5x.
    - `Hard`: Provides 2 food, 4 traps, and a speed multiplier of 2x.

- In the menu, players can start a `keyboard` game by pressing the **p** key.
- The player takes a **random direction** when the game starts.

#### ➜ Keys:
- `l` : **Quit** the game at any time.
- `Escape` and `space` : Return to the game **menu**.

#### ➜ In-Game:
- **Eat** as much `food` as possible to **increase** the player's score and size.
- Avoid `traps` smaller than the player; otherwise, the player's size and speed will be **divided** by the difficulty level (Easy: **2**, Medium: **3**, or Hard: **4**).
- The default **timer** is set to 60 seconds.
- At the end of the game, a window summarizes all the **game statistics**.


## Technos 📚

- Python (3.10.13)
- Pygame (latest)
- Anaconda

## Author 👨‍💻
➜ @[vincmgn](https://github.com/vincmgn)

## Contributing 🤝
Feel free to contribute to this project by suggesting improvements!

## Licence 📜
This project is distributed under the `MIT License`. For more information, please refer to the [LICENSE](/LICENSE) file.

<br>
Have a good time ! 🎮
