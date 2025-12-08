# Energy System Integration Course - University of Twente

This repository contains all materials for the Energy System Integration course at the University of Twente, including lecture materials and workshop content on the [ETM](https://energytransitionmodel.com/) (Energy Transition Model) and [PyPSA](https://docs.pypsa.org/latest/) (Python for Power System Analysis).

## For students

### 1. Installation Guide

Start here! Follow the comprehensive installation guide to set up your environment:

**[Installation Guide](installation-guide.md)**

The guide covers:
- Installing Anaconda (or micromamba) and Python
- Setting up VSCode
- Creating your conda environment
- Installing PyPSA and all dependencies

### 2. Lecture Materials

Once you have everything installed, explore the lecture materials in the `/lecture` folder:
- `lecture-case-example.py` - Example case to validate your installation
- `/lecture/data/` - Data files for the lecture examples

**Lecture and workshop slides** are available as PDFs in the `/slides` folder.

Run the example to make sure everything works:
```bash
conda activate esi-course
python lecture/lecture-case-example.py
```

### 3. Workshop Materials

The interactive workshop website is published online:

**[Workshop Website](https://thesethtruth.github.io/esi-course-utwente/intro.html)**

The website includes:
- Interactive tutorials on energy system modeling
- Hands-on exercises with PyPSA and the ETM
- Data analysis, scenario modeling, capacity expansion, and interconnection topics

You can also find the source files locally in the `/workshop` folder.

## For Maintainers

### Repository Structure

```
esi-course-utwente/
├── lecture/              # Lecture materials and example files
├── workshop/             # Jupyter Book workshop content
├── environment.yml       # Conda environment for students
├── pyproject.toml        # UV-managed dependencies for building
└── .github/workflows/    # CI/CD for building and deploying
```

### Dependency Management

This project uses **two separate dependency management systems**:

1. **Conda (for students)**: `environment.yml`
   - Used by students to set up their local development environment
   - Provides Python 3.12, PyPSA, and all scientific computing dependencies
   - Keep this stable and student-friendly

2. **UV (for building)**: `pyproject.toml`
   - Used for building the Jupyter Book website in CI/CD
   - Managed with [uv](https://github.com/astral-sh/uv) for fast, reliable builds
   - Keep dependencies minimal - only what's needed for building docs

### Building the Workshop Site

The workshop is built using Jupyter Book and automatically deployed via GitHub Actions.

#### Local Build

To build the workshop site locally:

```bash
# Install dependencies with uv (including dev dependencies for jupyter-book)
uv sync --extra dev

# Build the workshop
uv run jupyter-book build workshop
```

The built site will be in `workshop/_build/html`.

#### CI/CD Pipeline

The `.github/workflows/deploy.yml` workflow:
1. Triggers on push to `main` branch
2. Installs dependencies using UV
3. Builds the workshop with `jupyter-book`
4. Deploys to GitHub Pages (`gh-pages` branch)

### Important Version Constraints

**jupyter-book must be pinned to <2.0**

The pyproject.toml specifies `jupyter-book>=1.0.3,<2` because version 2.x introduced breaking changes with MyST that are incompatible with our workshop content. Do not upgrade to jupyter-book 2.x without first:
1. Testing all workshop content
2. Updating MyST syntax throughout the workshop
3. Verifying the build succeeds

### Making Changes

**Workshop Content**: Edit files in the `/workshop` folder. The site will rebuild automatically on push to main.

**Student Environment**: Update `environment.yml` for any changes to student dependencies. Test thoroughly before committing.

**Build Dependencies**: Update `pyproject.toml` for any changes to the documentation build process. Remember the jupyter-book <2 constraint.

### Troubleshooting Builds

If the build fails:
1. Check the GitHub Actions logs
2. Verify all workshop notebooks are valid
3. Ensure no notebooks have execution errors (execution is disabled but syntax must be valid)
4. Test the build locally with `jupyter-book build workshop`

For MyST syntax errors, see the [Jupyter Book documentation](https://jupyterbook.org/).
