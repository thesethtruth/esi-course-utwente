# Exercises 4: Storage, dispatchable generation and interconnection

## Exercise 1: Analyzing market-based interconnection effects
*This exercise develops your understanding of how market prices influence power system operation and investment decisions.*

Using the market-based model from the tutorial:

1. Compare two scenarios using German market price data:
   - Scenario A: Base case (12 GW interconnection)
   - Scenario B: Limited interconnection (6 GW)
   - Scenario C: Strong interconnection (24 GW)

2. For each scenario, analyze and explain:
   - Changes in renewable capacity deployment
   - Differences in storage capacity needs
   - Monthly import/export patterns
   - System costs

3. Create a brief analysis explaining:
   - The main differences between scenarios
   - Why these differences occur
   - What this means for energy system planning

## Exercise 2: Making your own two-bus system
*This exercise helps you understand the basic concepts of creating and analyzing interconnected power systems using PyPSA.*

Using the tutorial code as a reference, create a two-bus system with the following specifications:

1. Create two buses: `generation_bus` and `load_bus`
2. Add wind generator and a solar generator to the `generation_bus`
3. Add a 6 GW biogas plant to the `generation_bus`
4. Add the storage components to the `load_bus`
5. Connect the buses with a transmission line having:
   - Capital cost: 3000 k€/MW
   - Efficiency: 97%
6. Add the load profile to the `load_bus` as done in the workshop
7. Solve the network

Create visualizations showing:
- The installed capacities
- Hourly generation profile
- Power flow between buses


## Exercise 3: Regional power system design
*This exercise helps you apply interconnection modeling concepts to real-world power system planning challenges.*

You are an energy system planner for a region with three areas:
- Industrial zone (high constant demand)
- Urban area (variable residential/commercial demand)
- Rural area (good renewable resources)

:::{note}
Storage is possible at every location. Renewable energy generation is only possible at the rural area node. Biogas generation is possible (max. 1000 MW) at the industrial zone node.
:::

Tasks:
1. Create a three-bus system representing these areas
2. For each area, define appropriate:
   - Load profiles
     - For the industrial zone use the `industry_useful_demand_for_chemical_other_electricity.input (MW)` curve as load
     - For the urban area use the `buildings_space_heater_heatpump_air_water_electricity.input (MW)` curve as load
     - For the rural area use the `agriculture_useful_demand_electricity.input (MW)` curve as load
   - Available generation options
   - Storage possibilities

:::{hint}
You can set the load per bus by using the original ETM demand and supply curves, as shown below.
```python
ETM_CURVES_FP = "data/merit_order.csv"
etm_demand_supply = pd.read_csv(ETM_CURVES_FP, index_col=0, header=0)
etm_demand_supply.index = n.snapshots
n.add(
   "Load",
   "industry",
   bus="electricity",
   p_set=etm_demand_supply['industry_useful_demand_for_chemical_other_electricity.input (MW)']
)
```
:::
1. Design two scenarios:
   - "Limited interconnection": 2500 MW maximum between any areas
   - "Strong interconnection": 5000 MW maximum between any areas

2. Compare the scenarios in terms of:
   - Total system costs
   - Renewable energy integration
   - Storage requirements
   - Local vs. shared resources

3. Make a recommendation for the optimal interconnection strategy, supporting your answer with data from your analysis.

Use example data from the tutorial for costs and renewable profiles, scaling them appropriately for your system.