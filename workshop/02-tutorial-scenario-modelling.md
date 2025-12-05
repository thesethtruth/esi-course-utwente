# Tutorial 2: Energy System Scenario Modelling

In this tutorial chapter, we will explore how to make specific changes to base scenarios in the Energy Transition Model (ETM), a comprehensive tool for energy system modeling.

## Learning objectives
- Understand the ETM interface and its key components
- Learn to modify existing scenarios in the ETM
- Explore the II3050 Decentral Incentives scenario for the Netherlands in 2050

```{note}
In this tutorial, we will make intentionally significant changes to the scenario to clearly demonstrate the model's behavior and the relationships between different parameters. In real-world applications, scenario modifications typically involve more nuanced adjustments based on detailed analysis and sector-specific knowledge.
```

## Context and background

We use the ETM to model demand scenarios that we later soft-couple to our optimisation model. The ETM is particularly relevant as it's used by grid operators to define the [scenarios](https://www.netbeheernederland.nl/publicatie/rapport-ii3050-scenarios) for the [Integral Grid Outlook](https://www.netbeheernederland.nl/publicatie/integrale-infrastructuur-verkenning-2030-2050) (II3050) at the Dutch national level. For European-scale modeling, the [Ten Year Network Development Plan](https://2022.entsos-tyndp-scenarios.eu/) (TYNDP) scenarios, defined by ENTSO-e and ENTSO-g, are [also available](https://zenodo.org/records/8214522) through the [North Sea Wind Power Hub](https://northseawindpowerhub.eu/) (NSWPH) research initiative.

## Starting the scenario

Click on the `Open scenario` button to access the [Decentral Incentives](https://energytransitionmodel.com/saved_scenarios/14552) scenario, one of the II3050 scenarios for the horizon year 2050.

```{note} 
When opening a predefined (saved) scenario, a session scenario is created. This session scenario is your personal copy with all original settings. You can freely make changes, but saving them requires creating an account.
```

![ETM interface showing the II3050 Decentral Incentives scenario start screen](images/etm_startscreen.png)

```{note}
**Scenario Background**: The Decentral Incentives scenario represents a future where:
 - The Netherlands embraces decentralized climate action
 - Local communities and private initiatives drive the energy transition
 - Citizen-led projects lead renewable energy adoption
 - Traditional heavy industry sees decline
 - Heating solutions become diverse and localized, ranging from heat pumps to green hydrogen
```

## Overview of the ETM interface

Below is a comprehensive overview of the main interface elements in the ETM.

![Overview of the ETM interface showing main components](images/etm_overview.png)

### 1. Sidebar navigation

The sidebar provides access to six major categories:
1. Demand
2. Supply
3. Flexibility
4. Emissions
5. Costs & efficiencies
6. Results & data

Selecting a major category reveals its subcategories in an accordion menu between the sidebar and chart element.

### 2. Chart display

The chart element shows relevant visualizations based on your selected categories. Features include:
- Chart locking via the top-right lock icon
- Additional charts through the `+ See more charts` button
- Dynamic updates based on scenario modifications

### 3. Dashboard overview

The dashboard displays key performance indicators (KPIs) including:
- CO2 reduction
- Energy use reduction
- Cost metrics

Customize  the visible KPIs using the settings wheel in the black button on the dashboard's right side.

```{note}
The ETM generates all results on demand. Any input change or view modification triggers a model run, typically taking 3-7 seconds to update. For more details about the ETM's architecture, consult the [documentation](https://docs.energytransitionmodel.com/main/intro/).
```

Now, let use make some changes to the scenario. As we use the ETM to model the demand we will use as input for our optimisation model, we focus on demand categories for now. 

## Modifying household heating parameters

Navigate to `Demand > Households > Space heating & hot water`. In the base scenario, solar thermal plays a significant role in hot water generation, producing 22 PJ in 2050. Let's examine how this assumption affects both renewability and grid requirements.

![ETM interface showing household space heating and hot water settings](images/etm_spaceheating.png)

When we adjust the solar thermal slider to 0%, we observe:
- A modest 0.1% decrease in overall renewability
- A notable increase in biomass imports
- Changes in heat network supply composition

The increase in biomass imports appears to be related to the high proportion of heating networks, which partially rely on biomass as an energy source.

![ETM visualization of heat network energy sources showing significant biomass contribution](images/etm_heat_network.png)

To analyze the impact on the electricity network:
1. Click the `+ See more charts` button in the top-right corner
2. Search for `Electricity network capacity and peaks`
3. Add the chart and use the lock icon to keep it visible
4. The network capacity table should now appear in your chart section

From this we observe that the required additional network capacity at the MV net level is estimated at 29.6 GW. 

![ETM with the network table shown](images/etm_spaceheating_add_network_table.png)

### Testing extreme heating scenarios

#### Scenario 1: 100% air heat pumps

The base scenario already includes a substantial share of air-based heat pumps. Alternative technologies like hybrid heat pumps and district heating networks typically create lower network peaks due to their respective capability to switch fuels or buffer energy. Let's examine the impact of switching to 100% air heat pumps.

When setting the air heat pump slider to 100%, we observe a moderate increase in network capacity requirements of approximately 1 GW.

![ETM interface showing settings and impacts of 100% air heat pump scenario](images/etm_spaceheating_airheatpump.png)

Key observations from this change:
- Overall energy consumption decreases due to the energy efficiency of heat pumps
- System costs reduce (primarily due to removing costly district heating infrastructure)
- Black-out hours increase from 0 to 5 hours annually, suggesting emerging grid stress
- Network impact remains relatively manageable

#### Scenario 2: 100% electric boilers

Taking our analysis to an extreme, let's examine a scenario with 100% electric boilers. This represents a deliberately inefficient choice, as electric boilers have a Coefficient of Performance (COP) of 1, compared to heat pumps' COP of 3.5 or higher. This means electric boilers require 3.5 times more electricity to produce the same heat output.

![ETM interface showing impacts of 100% electric boiler scenario](images/etm_spaceheating_electricboiler.png)

The results clearly demonstrate why this would be problematic:
- Network capacity requirements increase by nearly 6 GW at the medium-voltage level compared to the base scenario
- Black-out hours surge to 178 hours per year, indicating severe grid stability issues
- The electrical system cannot adequately support this level of inefficient demand

This extreme scenario effectively illustrates why efficiency matters in heating technology selection and its direct impact on grid infrastructure requirements.

Reset your changes. 

:::{admonition} Reset your scenario
:class: tip
You can always reset your settings back to the base scenario by clicking the `reset` button, found left of the slider elements you've changed. Or reopen the [Decentral Incentives](https://energytransitionmodel.com/saved_scenarios/14552) scenario to reset all your changes.
:::

## Modifying Transport Parameters

### Smart Charging for Electric Vehicles

Navigate to `Demand > Transport passenger transport > Car technology` to verify that all personal transport is electric. Then proceed to `Flexibility > Flexibility storage > Batteries in electric vehicles` to examine charging behavior.

![Initial EV charging behavior showing daily cycles](images/etm_evcharging_before.png)

Increase the "Deployable capacity" slider under Technical specifications to 80% to simulate more EVs participating in smart charging strategies.

![Modified EV charging behavior showing weekly cycles](images/etm_evcharging_after.png)

This modification produces several significant changes:
- Charging patterns shift from daily to weekly cycles due to increased depth of charge
- EVs now function as weekly energy buffers
- System costs increase by 0.3 billion/year
- Biomass imports show an increase
- Overall energy imports decrease from 11.9% to 11.4%

```{note}
These changes occur because EVs now participate in energy market arbitrage, affecting the merit order and technology dispatch. The resulting load profile is substantially different due to the increased charging flexibility, which may require reconsideration of the overall energy system configuration.
```

## Downloading the hourly load curves

Navigate to `Data export > Hourly curves for electricity`. Click the 'Electricity load curves' button with the CSV icon to download the data.

![ETM interface showing the download location for hourly electricity curves](images/etm_download_curves.png)

These demand curves will serve as input for our optimization model, creating a soft coupling between our model and the ETM. By using these curves, we effectively treat demand modeling as an exogenous component of our optimization model.

## Conclusion

In this tutorial, we explored how different technological choices in household heating and transport can significantly impact the energy system. Through our scenario analysis in the ETM, we observed that:

- Technology efficiency matters greatly: The comparison between heat pumps (COP > 3.5) and electric boilers (COP = 1) demonstrated how efficiency directly affects grid capacity requirements and system stability
- System interactions are complex: Changes in one sector (like EV charging strategies) can have unexpected effects across the system, influencing everything from biomass imports to overall system costs
- Grid impacts vary: While some changes (like 100% air heat pumps) led to manageable grid impacts, others (like 100% electric boilers) resulted in severe stability issues

These insights highlight why detailed scenario analysis is crucial for energy system planning and why real-world decisions require careful consideration of multiple factors beyond simple technology substitution.
