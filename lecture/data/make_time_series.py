import pandas as pd

# Load the data files
load_data = pd.read_csv(
    "load.csv", index_col=0, parse_dates=True, header=0, names=["load"]
)
solar_data = pd.read_csv("solar.csv", header=0)
wind_data = pd.read_csv("wind.csv", header=0)

# Combine based on load timestamps
combined_data = pd.DataFrame(index=load_data.index)
combined_data.index.name = "time"
combined_data["load"] = load_data["load"]
combined_data["solar"] = solar_data["electricity"].values
combined_data["wind"] = wind_data["electricity"].values

# Save the combined timeseries
combined_data.to_csv("timeseries.csv")
