from pypsa import Network
import pandas as pd


# Load timeseries data
ts = pd.read_csv("data/timeseries.csv", index_col=0, header=0)
# trim to 4 weeks
ts = ts[0:672]
# load costs
costs = pd.read_csv("data/costs.csv", index_col=0, header=0)

# initialize network
n = Network()
# set snapshots based on timesteps
n.set_snapshots(ts.index)
# add buses
n.add("Bus", "electricity")

# add load
n.add(
    "Load",
    "demand",
    bus="electricity",
    p_set=ts.load,
)

# add solar and wind
for tech in ["wind", "solar"]:
    n.add(
        "Generator",
        tech,
        bus="electricity",
        p_max_pu=ts[tech],
        capital_cost=costs.at[tech, "capital_cost"],
        marginal_cost=costs.at[tech, "marginal_cost"],
        p_nom_extendable=True,
    )

# add storage
EP_RATIO = 6
n.add(
    "StorageUnit",
    "battery storage",
    bus="electricity",
    max_hours=EP_RATIO,
    capital_cost=costs.at["battery inverter", "capital_cost"]
    + EP_RATIO * costs.at["battery storage", "capital_cost"],
    efficiency_store=costs.at["battery inverter", "efficiency"],
    efficiency_dispatch=costs.at["battery inverter", "efficiency"],
    p_nom_extendable=True,
    cyclic_state_of_charge=True,
)

# Solve network
n.optimize(solver_name="highs")

# %% Analyze outcome
import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots(3, 1, figsize=(10, 10))
plt.subplots_adjust(hspace=0.4)

sns.set_theme("notebook", style="white")
n.generators.p_nom_opt.div(1e3).plot(
    ax=ax[0], kind="barh", title="Installed generation capacity (GW)", color="tab:red"
)
n.storage_units.p_nom_opt.div(1e3).mul(EP_RATIO).plot(
    ax=ax[1], kind="barh", title="Installed storage capacity (GWh)", color="tab:green"
)

# Calculate storage relative to load
storage_rel_to_load = n.loads_t.p["demand"] - n.storage_units_t.p["battery storage"]
storage_rel_to_load.index = n.generators_t.p.index
storage_rel_to_load = storage_rel_to_load.to_frame()
storage_rel_to_load.columns = ["storage"]


n.generators_t.p.div(1e3).plot(
    ax=ax[2], kind="area", title="Generation (MW)", legend=True, colormap="tab20c"
)

n.loads_t.p.div(1e3).plot(ax=ax[2], kind="line", color="tab:orange")
storage_rel_to_load.div(1e3).plot(
    ax=ax[2], kind="line", title="Timeseries (GW)", legend=True, color="tab:green"
)


ax[2].set_xticks(range(0, len(ts.index), 24))


for axx in ax:
    sns.despine(ax=axx, top=True, right=True)
    axx.set_ylabel("")
    axx.set_xlabel("")
