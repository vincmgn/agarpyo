# Agarpyo 🧩
> Welcome to Agarpyo, a reimagined version of the agar.io game.

## Project Overview 🎯

Agarpyo puts players in control of a character navigating through an environment filled with challenges and obstacles. The main objective is to collect resources, evade traps, and compete against other players to emerge as the ultimate champion.

## Prerequisite 🛟

Before you begin, ensure you have  [Anaconda](https://www.anaconda.com/download) installed 🐍
You don't need to install python separately.

## Set up the environment 🛠️

#### From a new environment 
1. Start Anaconda 🐍
2. In the menu, select **Environments**
3. At the bottom, click on **Create** 
4. Name this environments, for example : _Agarpyo_
5. Select the version : _Python 3.10.13_
6. Click on **Create**
7. In the menu, select **Home**
8. At the top, select the newly environment (here, _Agarpyo_)
9. Open VSCode, by clicking on **Launch** button

#### From a backup file (don't work on Mac)
1. Create a file in your Desktop name `agarpyo.yaml`
```yaml
name: Agarpyo
channels:
  - defaults
dependencies:
  - bzip2=1.0.8=he774522_0
  - ca-certificates=2023.12.12=haa95532_0
  - libffi=3.4.4=hd77b12b_0
  - openssl=3.0.13=h2bbff1b_0
  - pip=23.3.1=py310haa95532_0
  - python=3.10.13=he1021f5_0
  - setuptools=68.2.2=py310haa95532_0
  - sqlite=3.41.2=h2bbff1b_0
  - tk=8.6.12=h2bbff1b_0
  - tzdata=2023d=h04d1e81_0
  - vc=14.2=h21ff451_1
  - vs2015_runtime=14.27.29016=h5e58377_2
  - wheel=0.41.2=py310haa95532_0
  - xz=5.4.5=h8cc25b3_0
  - zlib=1.2.13=h8cc25b3_0
  - pip:
      - pygame==2.5.2
```
2. Start Anaconda 🐍
3. In the menu, select **Environments**
4. In At the bottom, click on **Import**
5. Import `agarpyo.yaml` from **Local Drive**
6. Click on **Import** button
7. In the menu, select **Home**
8. At the top, select the newly environment (here, _agarpyo_)
9. Open VSCode, by clicking on **Launch** button

## Run the project 🚀

1. Open VSCode terminal and check if your environment is activated with this command :
```bash
conda activate Agarpyo
```
2. Next, you just need to install (or check if you used de backup file) `pygame` in your environment
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
