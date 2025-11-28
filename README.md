# Data Science Through Yeller Quarry
## A Pandas Tutorial Series

---

*"To be a Yeller Quarry trapper was to be what miners have been in other climes, figures descending into a darkness of wings and teeth and greasy blood, emerging some weeks later—godwilling—with haul sacks of carcasses for Capital archivists and cages bursting with screeches and growls for traders in the living."*

---

## Overview

This tutorial series teaches pandas—Python's powerful data analysis library—through the lens of the Yeller Quarry, a fictional mining and trapping operation in the world of Densworld. You'll learn real data science skills while exploring expedition logs, creature catalogs, and trade records from this strange and dangerous place.

### Why Fictional Data?

Traditional data science courses use generic datasets: iris flowers, Titanic passengers, housing prices. These are fine for learning, but:

1. **Students can copy solutions** from the thousands of existing tutorials using the same data
2. **There's no intrinsic interest** in the data itself
3. **Domain knowledge is trivial**—everyone knows what a flower petal is

By using data from an unfamiliar fictional world, this course ensures:

1. **You must actually learn the methods**—no copying from Stack Overflow
2. **The data tells a story** that rewards careful exploration
3. **Domain knowledge matters**—understanding what a "yeller group" is helps you analyze yeller data

---

## The Datasets

| File | Records | Description |
|------|---------|-------------|
| `creatures.csv` | 25 | Creature catalog from the Capital Archives |
| `crews.csv` | 12 | Trapping crews operating in the Quarry |
| `traps.csv` | 35 | Individual trap deployments |
| `catches.csv` | 50 | Records of captured creatures |
| `prices.csv` | 75 | Capital market prices over time |
| `incidents.csv` | 30 | Accidents, injuries, and strange occurrences |

### Key Entities

- **The Boss**: A mysterious woman who led the Redmane Expedition into the caves. Red hair braided in a maze pattern. Disappeared during a creature attack on March 18, 1855.

- **Truck**: The Boss's second-in-command. Killed defending her from whatever lurks in the deep caves. His face was unrecognizable when they dragged his body out.

- **Gull**: A storyteller and trapper. Formed "Gull's Remnants" after the Redmane disaster. Tells tales of witches and spells around the campfire.

- **Ox**: A large, slow man with quick fingers. The best at tying knots in all the Quarry.

- **Black Yeller**: Leader of a mysterious group of five women who move as one. They entered the cave to retrieve The Boss and never came back by morning.

- **The Wharver**: A rusted creature from Grimslew Shore. Globed lizard with fins, hot belly that burns through nets. Steam chugs from its grit-clogged gills.

- **The Maw Beast**: Something that can digest anything. Found at 45 meters depth. The creature that killed Truck—or was it a witch?

---

## The Tutorials

| # | Tutorial | Notebook | Video |
|---|----------|----------|-------|
| 1 | The Creature Catalog | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/yeller-quarry-data-science/blob/main/notebooks/tutorial_01_creature_catalog.ipynb) | [Watch](#) |
| 2 | Trap Deployment Records | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/yeller-quarry-data-science/blob/main/notebooks/tutorial_02_trap_records.ipynb) | [Watch](#) |
| 3 | The Catch Ledger | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/yeller-quarry-data-science/blob/main/notebooks/tutorial_03_catch_ledger.ipynb) | [Watch](#) |
| 4 | The Art of Grouping | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/yeller-quarry-data-science/blob/main/notebooks/tutorial_04_grouping.ipynb) | [Watch](#) |
| 5 | Joining the Ledgers | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/yeller-quarry-data-science/blob/main/notebooks/tutorial_05_joining_ledgers.ipynb) | [Watch](#) |
| 6 | Time in the Quarry | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/yeller-quarry-data-science/blob/main/notebooks/tutorial_06_time_in_quarry.ipynb) | [Watch](#) |
| 7 | Patterns in the Darkness | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/yeller-quarry-data-science/blob/main/notebooks/tutorial_07_patterns_darkness.ipynb) | [Watch](#) |
| 8 | Cleaning the Archives | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/yeller-quarry-data-science/blob/main/notebooks/tutorial_08_cleaning_archives.ipynb) | [Watch](#) |
| 9 | Seeing the Quarry | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/yeller-quarry-data-science/blob/main/notebooks/tutorial_09_seeing_quarry.ipynb) | [Watch](#) |
| 10 | The Investigation (Capstone) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/yeller-quarry-data-science/blob/main/notebooks/tutorial_10_investigation.ipynb) | [Watch](#) |

---

## Setup Instructions

### Requirements
- Python 3.8+
- pandas
- Jupyter Notebook or JupyterLab

### Installation

```bash
pip install pandas jupyter
```

### Running the Tutorials

1. Clone or download this folder
2. Navigate to the folder in your terminal
3. Start Jupyter:
   ```bash
   jupyter notebook
   ```
4. Open the `notebooks/` folder
5. Start with `tutorial_01_creature_catalog.ipynb`

### File Structure

```
yeller-quarry-data-science/
├── README.md
├── yeller_data.py      # Optional helper module
├── data/
│   ├── creatures.csv
│   ├── crews.csv
│   ├── traps.csv
│   ├── catches.csv
│   ├── prices.csv
│   └── incidents.csv
└── notebooks/
    ├── tutorial_01_creature_catalog.ipynb
    ├── tutorial_02_trap_records.ipynb
    ├── tutorial_03_catch_ledger.ipynb
    ├── tutorial_04_grouping.ipynb
    ├── tutorial_05_joining_ledgers.ipynb
    ├── tutorial_06_time_in_quarry.ipynb
    ├── tutorial_07_patterns_darkness.ipynb
    ├── tutorial_08_cleaning_archives.ipynb
    ├── tutorial_09_seeing_quarry.ipynb
    └── tutorial_10_investigation.ipynb
```

### Optional: Helper Module

The `yeller_data.py` file provides convenience functions for loading datasets:

```python
from yeller_data import load_all

data = load_all()
creatures = data['creatures']
catches = data['catches']
```

This is optional—the tutorials load data directly from GitHub URLs.

---

## The World of Densworld

Yeller Quarry is one of eleven regions in Densworld, a fictional archive spanning fantasy, noir, and contemporary layers. Other regions include:

- **The Capital**: A sophisticated city with senators, archives, and intrigue
- **Dens**: A creeping wilderness of densmuck that dissolves everything artificial
- **Mirado**: A desert where a Colonel has been sieging a hovering tower for twenty years
- **Northtown**: Ascetic villages where children are warned not to wander
- **Dead River**: A transitional zone where only the mysterious Yeller can survive

The data in this course comes from the Yeller Quarry trapping operations that supply the Capital with exotic creatures for archival study, senatorial banquets, and the strange fashions of the wealthy.

---

## Credits

Densworld archive and course concept by Daniel.
Tutorial development with Claude.

*"Most archivists live in the Capital, were born in the Capital, schooled in the Capital, work and will die in the Capital. But the very best of them come from outside Yeller Quarry."*

---
