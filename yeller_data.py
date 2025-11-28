# Data Loading Helper for Yeller Quarry Tutorials
# Run this cell at the start of any tutorial to load all datasets

import pandas as pd

# GitHub raw content URL (change YOUR_USERNAME to actual username)
BASE_URL = "https://raw.githubusercontent.com/YOUR_USERNAME/yeller-quarry-data-science/main/data/"

def load_yeller_data():
    """Load all Yeller Quarry datasets from GitHub."""
    print("Loading data from the Capital Archives...")
    
    data = {}
    files = ['creatures', 'crews', 'traps', 'catches', 'prices', 'incidents']
    
    for name in files:
        try:
            data[name] = pd.read_csv(BASE_URL + name + ".csv")
            print(f"  ✓ {name}: {len(data[name])} records")
        except Exception as e:
            print(f"  ✗ {name}: Failed to load - {e}")
    
    print("\nData loaded successfully. Available datasets:")
    print("  creatures, crews, traps, catches, prices, incidents")
    
    return data

# Quick individual loaders
def load_creatures():
    return pd.read_csv(BASE_URL + "creatures.csv")

def load_crews():
    return pd.read_csv(BASE_URL + "crews.csv")

def load_traps():
    return pd.read_csv(BASE_URL + "traps.csv")

def load_catches():
    return pd.read_csv(BASE_URL + "catches.csv")

def load_prices():
    return pd.read_csv(BASE_URL + "prices.csv")

def load_incidents():
    return pd.read_csv(BASE_URL + "incidents.csv")
