# Welcome

Welcome to the website for the energy modelling workshop of the course Energy System Integration (202400343). This course is part of the curriculum of the [Sustainable Energy Technology master at the University of Twente](https://www.utwente.nl/en/set/).


This workshop is an introduction to energy system modelling in the context of Energy System Integration. It is based around an optimisation approach using PyPSA. Topics covered in this tutorial:

- time series analysis (e.g. wind and solar production, load curves)
- geographical data (e.g. location of power plants)
- demand scenario modelling using the ETM
- data visualisation
- capacity expansion planning
- storage and dispatchable generators
- multi-nodal networks
- interactive visualisation and dashboarding

## Content of this workshop

This workshop is organized into four chapters, each designed to deepen your understanding of the topics through a combination of tutorials and exercises.

1. **Tutorials**: Each chapter includes a detailed tutorial that guides you step-by-step through the topic. The tutorials are centered around practical code examples, with explanations in-between to help you understand the underlying concepts.

2. **Exercises**: At the end of each chapter, you’ll find exercises to work through. These exercises are intended to reinforce your learning and give you an opportunity to apply the concepts on your own. As you tackle the exercises, feel free to refer back to the tutorial and relevant [documentation](#useful-sources) for support.

Happy learning!

## Prerequisites 
1. Install Python and Poetry according to the [Installation Guide](#installation-guide-energy-system-integration), which covers how to set up your PyPSA environment
2. Download the workshop [data files from the course repository](https://github.com/thesethtruth/esi-course-utwente/tree/main/esi-modelling-workshop/data). We'll use these example datasets throughout the workshop.


## Useful sources

### Documentation
 - [PyPSA documentation](https://pypsa.readthedocs.io/en/latest/index.html)
 - [PyPSA examples](https://pypsa.readthedocs.io/en/latest/examples-index/lopf.html)
 - [seaborn](https://seaborn.pydata.org/index.html)
 - [Pandas](https://pandas.pydata.org/docs/)

### Data sources
 - [Renewables.ninja](https://renewables.ninja/)  
 *(renewable energy generation timeseries)*
 - [Energy Transition Model](https://energytransitionmodel.com/)  
 *(scenario modelling, demand curves, rich data source)*
 - [Technology data](https://github.com/PyPSA/technology-data/tree/master/outputs)  
 *(costs, emission factors, efficiencies, etc.)*




# Installation Guide: Energy System Integration

This guide will help you install Python on your computer. Additionally, it will guide you through installing VSCode as your IDE (Integrated Development Environment) and Poetry as your environment manager. Below is a brief introduction explaining why you need these three components and what they do.

> **Note:** You are free to choose your own IDE, package manager, or even operating system as long as you can use [PyPSA](https://pypsa.readthedocs.io/en/latest/getting-started/installation.html). This guide is written for Windows.

## Explainer: Why Python, VSCode, and Poetry?

To get started with programming and projects like PyPSA (Python for Power System Analysis), you'll need a few key tools. Here’s why Python, VSCode, and Poetry are essential:

### Python
**What is Python?**
Python is a popular, easy-to-learn programming language used for many applications.

**Why do you need Python?**
- **Core Language**: PyPSA is written in Python, so you need it to run and modify PyPSA.
- **Libraries**: Python has many libraries that simplify tasks. Poetry helps manage these libraries easily.

### VSCode (Visual Studio Code)
**What is VSCode?**
VSCode is a free, powerful code editor developed by Microsoft.

**Why do you need VSCode?**
- **Easy Coding**: Features like syntax highlighting and code completion make writing Python code simpler.
- **Seamless Integration**: VSCode works well with Python and Poetry, helping you run and manage your projects directly from the editor.

### Poetry
**What is Poetry?**
Poetry manages your Python projects, handling dependencies and virtual environments.

**Why do you need Poetry?**
- **Manage Libraries**: Easily install and update libraries for your projects.
- **Organize Projects**: Keeps your project dependencies isolated and organized, which is crucial when working in VSCode.

These tools work together to make your programming experience smoother and more enjoyable.

Remember, this guide is for Windows, but you can use these tools on any operating system. Happy coding!

## Installation Steps

### Step 1 - Install Python 

Install Python 3.12 from the official Python website: [Python Downloads for Windows](https://www.python.org/downloads/windows/). If you don't know which version you need, you will probably be using the [64-bit AMD version](https://www.python.org/ftp/python/3.12.7/python-3.12.7-amd64.exe).

### Step 2 - Install Poetry 

You can follow the official guide on [Poetry](https://python-poetry.org/docs/#installing-with-pipx), or follow the steps below.

#### Install pipx
```bash
py -m pip install --user pipx
```

It is possible (even most likely) the above finishes with a WARNING looking similar to this:
```
WARNING: The script pipx.exe is installed in `<USER folder>\AppData\Roaming\Python\Python3x\Scripts` which is not on PATH
``` 
If so, go to the mentioned folder, allowing you to run the pipx executable directly. Enter the following line (even if you did not get the warning):
```bash
.\pipx.exe ensurepath
```
#### Install poetry
```bash
pipx install poetry
```

### Step 3 - Install VScode

Download and install VScode from the official website: https://code.visualstudio.com/download

#### Recommended: Install extensions
This will make your life easier. Use the extensions tab on the left side (the blocks) to install:
1. **Python (Microsoft)**  
   *Linting, syntax highlighting and suggestions*
2. **Jupyter (Microsoft)**  
   *Allows you to run code interactively and easier debugging*

### Step 4 - Open a folder in VScode and start your project

Make a folder on your desired location. For instance, I use `C:\Users\Seth\coding\esi-course`.

Open this folder in VScode (through `File > Open Folder...` or `CTRL+K` and then `CTRL+O`).

### Step 5 - Download the contents of this course repo

Navigate to https://github.com/thesethtruth/esi-course-utwente and use the code button to download the course content as a .zip. Unzip this folder directly in the folder of you choice. 

#### Alternatively you can use Git

```bash
git clone https://github.com/thesethtruth/esi-course-utwente.git .
```

### Step 6 - Install all dependencies using Poetry 
Make sure you are in the right folder (the one that you just downloaded) and run this command:

```bash
# /esi-course-utwente
poetry install
```

This will install all the dependencies. Activate the environment with:

```
poetry shell
```
Select this environment as your Python interpreter in VSCode by using: `CRTL+SHIFT+P` and select the environment name from the list (you should see it in front of your terminal). If you can't see it, type `which python` in your terminal and use the option `Enter interpreter path...`. Paste the output of the `which python` in there. 

### Step 7 - Validate your installation

Run the example from lecture 6 directly using the Play button on top of the screen when you open the Python file. Or use the terminal directly: `python lecture-6/lecture-6-case-example.py`. This should run without errors.

#### Run it interactively
Use the Jupyter extension to run the file interactively. To do this, open the file and use `CRTL+SHIFT+P` > `Jupyter: Run Current File in Interactive Window`. This will open an interactive window, where you can explore variable, rerun code and inspect plots. 

#### Optionally: add a shortcut for running interactively

Normally, I run most of my code interactively with Jupyter because it is easier to develop and debug code while writing. For that reason, I have a keyboard shortcut (`SHIFT+ENTER`) that runs the Python file interactively.

To also use this, use `CRTL+SHIFT+P` > `Preferences: Open Keyboard Shortcuts (JSON)` and add this (only the part between the curly brackets):

```json
[
    ...
    {
        "key": "shift+enter",
        "command": "jupyter.runFileInteractive",
        "when": "editorTextFocus && !findInputFocussed && !jupyter.ownsSelection && !notebookEditorFocused && !replaceInputFocussed && editorLangId == 'python'"
    },
    ...
]
```