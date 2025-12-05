# Installation Guide: Energy System Integration

This guide will help you install Python on your computer. Additionally, it will guide you through installing VSCode as your IDE (Integrated Development Environment) and Anaconda as your environment manager. Below is a brief introduction explaining why you need these three components and what they do.

> **Note:** You are free to choose your own IDE, package manager, or even operating system as long as you can use [PyPSA](https://pypsa.readthedocs.io/en/latest/getting-started/installation.html). This guide is written for Windows.

## Explainer: Why Python, VSCode, and Conda?

To get started with programming and projects like PyPSA (Python for Power System Analysis), you'll need a few key tools. Here's why Python, VSCode, and conda are essential:

### Python
**What is Python?**
Python is a popular, easy-to-learn programming language used for many applications.

**Why do you need Python?**
- **Core Language**: PyPSA is written in Python, so you need it to run and modify PyPSA.
- **Libraries**: Python has many libraries that simplify tasks. Conda helps manage these libraries easily.

### VSCode (Visual Studio Code)
**What is VSCode?**
VSCode is a free, powerful code editor developed by Microsoft.

**Why do you need VSCode?**
- **Easy Coding**: Features like syntax highlighting and code completion make writing Python code simpler.
- **Seamless Integration**: VSCode works well with Python and conda, helping you run and manage your projects directly from the editor.

### Anaconda
**What is Anaconda?**
Anaconda is a distribution of Python that comes with a package manager (conda) and many scientific libraries pre-installed. It includes Anaconda Navigator, a graphical interface that makes managing environments easy.

**Why do you need Anaconda?**
- **Manage Libraries**: Easily install and update libraries for your projects.
- **Organize Projects**: Keeps your project dependencies isolated and organized, which is crucial when working in VSCode.
- **Pre-configured**: Comes with Python already installed, so you don't need a separate Python installation.

> **For advanced users:** You can also use micromamba instead of Anaconda if you prefer a lightweight command-line tool.

These tools work together to make your programming experience smoother and more enjoyable.

Remember, this guide is for Windows, but you can use these tools on any operating system. Happy coding!

## Installation Steps

### Step 1 - Install Anaconda

Download and install Anaconda from the official website: [Anaconda Downloads](https://www.anaconda.com/download)

Follow the installation wizard and accept the default settings. This will install Python 3.12 and conda automatically.

> **Note:** Advanced users can use micromamba if they prefer a lightweight CLI alternative.

### Step 2 - Install VScode

Download and install VScode from the official website: https://code.visualstudio.com/download

#### Recommended: Install extensions
This will make your life easier. Use the extensions tab on the left side (the blocks) to install:
1. **Python (Microsoft)**
   *Linting, syntax highlighting and suggestions*
2. **Jupyter (Microsoft)**
   *Allows you to run code interactively and easier debugging*

### Step 3 - Open a folder in VScode and start your project

Make a folder on your desired location. For instance, I use `C:\Users\Seth\coding\esi-course`.

Open this folder in VScode (through `File > Open Folder...` or `CTRL+K` and then `CTRL+O`).

### Step 4 - Download the contents of this course repo

Navigate to https://github.com/thesethtruth/esi-course-utwente and use the code button to download the course content as a .zip. Unzip this folder directly in the folder of you choice.

#### Alternatively you can use Git

```bash
git clone https://github.com/thesethtruth/esi-course-utwente.git .
```

### Step 5 - Create and activate a conda environment with PyPSA

Open a terminal in VSCode (Terminal > New Terminal) or use Anaconda Prompt. Make sure you are in the course folder.

Create the environment using the provided `environment.yml` file:

```bash
conda env create -f environment.yml
```

This will create a new isolated environment called `esi-course` with Python 3.12, PyPSA, and all required dependencies.

Activate the environment:

```bash
conda activate esi-course
```

Select this environment as your Python interpreter in VSCode by using: `CTRL+SHIFT+P` > `Python: Select Interpreter` and choosing the `esi-course` environment from the list. If you can't see it, type `where python` (Windows) or `which python` (macOS/Linux) in your activated terminal and use the option `Enter interpreter path...` to paste the path.

### Step 6 - Validate your installation

Make sure your conda environment is activated (`conda activate esi-course`), then run the example from this lecture directly using the Play button on top of the screen when you open the Python file. Or use the terminal directly: `python lecture/lecture-case-example.py`. This should run without errors.

#### Run it interactively
Use the Jupyter extension to run the file interactively. To do this, open the file and use `CTRL+SHIFT+P` > `Jupyter: Run Current File in Interactive Window`. This will open an interactive window, where you can explore variables, rerun code and inspect plots.

#### Optionally: add a shortcut for running interactively

Normally, I run most of my code interactively with Jupyter because it is easier to develop and debug code while writing. For that reason, I have a keyboard shortcut (`SHIFT+ENTER`) that runs the Python file interactively.

To also use this, use `CTRL+SHIFT+P` > `Preferences: Open Keyboard Shortcuts (JSON)` and add this (only the part between the curly brackets):

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

## Useful Conda Commands

Here are some helpful commands for managing your conda environment:

```bash
# Activate/deactivate the environment
conda activate esi-course
conda deactivate

# List all conda environments
conda env list

# List all packages in the current environment
conda list

# Update all packages in the environment
conda update --all

# Update a specific package (e.g., PyPSA)
conda update pypsa

# Remove the entire environment if you want to start fresh
conda env remove -n esi-course
```

## Troubleshooting

### Environment not showing in VSCode
- Make sure you've activated the environment first: `conda activate esi-course`
- Restart VSCode after creating the environment
- Use `CTRL+SHIFT+P` > `Python: Select Interpreter` and manually browse to the Python executable

### PyPSA import errors
- Make sure PyPSA is installed: `conda list pypsa`
- If it's missing or you have issues, recreate the environment:
  ```bash
  conda env remove -n esi-course
  conda env create -f environment.yml
  ```

### For micromamba users
If you're using micromamba instead of Anaconda, replace `conda` with `micromamba` in all commands above.

**Pro tip:** Create an alias so you can just type `conda` instead of `micromamba`:
- **Windows (PowerShell):** Add `Set-Alias -Name conda -Value micromamba` to your PowerShell profile
- **macOS/Linux (bash/zsh):** Add `alias conda=micromamba` to your `~/.bashrc` or `~/.zshrc`

Then you can use all the commands exactly as written in this guide!