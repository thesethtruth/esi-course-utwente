# Exercises 3: Capacity expansion modelling

## Exercise 1: Reproducing the baseline scenario
*This exercise helps you understand the basic PyPSA model setup and optimization workflow.*

Your task is to reproduce the baseline scenario from the tutorial with the following modifications:
1. Create a new network using the same input data but with a lower battery storage EP_RATIO of 2 hours instead of 6
2. Run the optimization with renewable generation limits
3. Create a bar plot comparing your results with the original baseline scenario (500 GW solar, 230 GW wind, 130 GW storage)
4. Explain in 2-3 sentences how the change in storage duration affects the optimal system configuration

## Exercise 2: Analyzing cost sensitivity
*This exercise develops your understanding of how different cost assumptions impact system design.*

The tutorial explored scenarios with doubled generation and storage costs. Your task is to:

1. Create three scenarios:
   - Baseline
       - Include flow batteries (FLOW_EP_RATIO = 100)
       - Remove upper limits on generation technologies
   - Cheap wind and flow batteries  
   *(halve the cost for flow batteries, reduce the cost of wind by 25%)*
   - Cheap solar and li-ion batteries  
   *(halve the cost for li-ion batteries, reduce the cost of solar by 25%)*

2. Create plots showing:
   - Installed capacities for each technology
   - Relative system costs compared to baseline
3. Write a brief analysis explaining why the system reacts differently to cost reductions versus the cost increases shown in the tutorial

## Exercise 3: Adding dispatchable generation
*This exercise helps you apply PyPSA modeling by integrating conventional generation technologies into a renewable-focused system.*

In this exercise, you will extend the baseline scenario by adding the option to invest in combined cycle gas turbine (CCGT) power plants. These plants can provide flexible backup generation but come with fuel costs and CO2 emissions.

Add a new generator to the network with the following parameters:
1. Technology parameters for CCGT:
   - Capital cost: 800 k€/MW
   - Marginal cost: 70 €/MWh (including fuel costs)
   - CO2 emission factor: 0.37 tonnes/MWh
   - Efficiency: 60% (not needed but assumed for the emission factor)

Your tasks:
1. Modify the `create_network` function from the tutorial to include the CCGT generator
2. Run three scenarios:
   - Baseline (from tutorial)
   - Baseline + CCGT without CO2 price
   - Baseline + CCGT with CO2 price of 100 €/tonne
3. Create visualizations showing:
   - Installed capacities for all technologies in each scenario
   - Annual CO2 emissions for each scenario
   - Generation mix during the week in February (like in the tutorial)
4. Write a brief analysis explaining:
   - Under what conditions does the model choose to invest in CCGT capacity?
   - What is the impact the system configuration?
   - How does the CO2 price affect the role of gas in the system? What does that tell you in terms of policy design?

:::{hint}
Consider adding the CO2 price by changing the marginal cost of the CCGT in the scenario by adding the emissions cost (CO2 price × emission factor) to the fuel cost.
:::