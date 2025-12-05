# Exercises 1: Data analysis

## Exercise 1: Reproducing energy generation analysis
*This exercise helps you understand the basic workflow and calculations.*

1. Download the datasets from [Renewables.ninja](https://renewables.ninja/):
   - Wind generation data 
   - Solar generation data 

2. Create two visualizations:
   - Plot the hourly wind and solar generation patterns
   - Calculate and plot the monthly capacity factors
   
3. Calculate the Full Load Hours (FLH) for both wind and solar generation

## Exercise 2: Analyzing demand patterns
*This exercise develops your analytical skills with energy data.*

1. Download the data export from the Energy Transition model from the course repository: [merit_order.csv](https://github.com/thesethtruth/esi-course-utwente/blob/main/esi-modelling-workshop/data/merit_order.csv)

:::{note}
The Energy Transition Model use MW(h) as the standard unit. You can assume that this data is also in MW(h).
:::

2. Analyze the electricity demand data to identify:
   - The three largest contributors to total energy consumption and their total energy consumption on TWh
   - The three largest contributors to peak demand and their peak demand in MW

3. What time periods show the highest demand for these demand categories? Investigate:
   - Daily patterns
   - Weekly patterns
   - Seasonal patterns

4. Write a short analysis explaining how these patterns might affect system integration challenges

## Exercise 3: Applying to a new context
*This exercise helps you apply the learned concepts to a different situation.*

You are an energy system consultant analyzing data for a new industrial park development.

Given the following data:
- Hourly electricity demand from three different types of industries  
  *(use the top 3 demand categories from the previous exercise)*
- Local wind and solar generation potential

Tasks:
1. Create a visualization that shows the temporal match between renewable generation and industrial demand

2. Analyse, visualize and investigate:
   - The capacity factors of renewables
   - The ratio between peak and average demand for each industry
   - Supply-demand matching score
   - Periods of excess generation
   - Periods of supply shortage

3. Write recommendations for:
   - The optimal mix of wind and solar capacity
   - Strategies to manage peak demand
