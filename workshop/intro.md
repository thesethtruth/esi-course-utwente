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
1. Install Python and Conda according to the [Installation Guide](#installation-guide-energy-system-integration) below, which covers how to set up your PyPSA environment
2. Download the workshop [data files from the course repository](https://github.com/thesethtruth/esi-course-utwente/tree/main/workshop/data). We'll use these example datasets throughout the workshop.


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



```{include} ../installation-guide.md
```