import pandas as pd

# Load the data
RAW_FILE = "merit_order.1238819.csv"
OUTPUT_FILE = "load.csv"
NORMALIZE = False
RESET_INDEX_YEAR = 2019


data = pd.read_csv(RAW_FILE, index_col=0, header=0)
data = data[[col for col in data.columns if ".input" in col]].sum(axis=1)

if NORMALIZE:
    data = data / data.max()

if RESET_INDEX_YEAR:
    data.index = pd.date_range(
        start=f"{RESET_INDEX_YEAR}-01-01", periods=len(data), freq="h"
    )

data = data.to_frame()
data.index.name = "time"
data.columns = ["load"]
data.to_csv(OUTPUT_FILE)
