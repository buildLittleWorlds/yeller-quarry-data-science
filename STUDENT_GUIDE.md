# Welcome to Yeller Quarry
## A Data Science Adventure in Densworld

---

*You are about to descend into the darkness.*

---

### What Is This?

This is a data science course disguised as a monster-hunting expedition.

You'll learn **pandas**—the most important Python library for working with data—by analyzing records from Yeller Quarry, a fictional mining and trapping operation in a world called **Densworld**. Instead of sales figures and customer databases, you'll work with creature catalogs, trap deployment logs, catch ledgers, incident reports, and market prices for exotic specimens.

By the end, you'll know how to load, clean, filter, merge, aggregate, visualize, and analyze real datasets. You'll also know more than you expected about the feeding habits of Leatherback Burrowers and why nobody talks about what happened to The Boss.

### Why Learn This Way?

Your professor is a creative writing instructor who believes:

1. **Stories make things stick.** You'll remember that `groupby()` splits data into groups because you used it to figure out which trapping crew had the most fatalities—not because you read a definition.

2. **Invented worlds prevent cheating.** You can't Google "how to analyze Yeller Quarry catch data" because it doesn't exist anywhere else. You have to actually learn the skills.

3. **Domain knowledge matters.** Real data scientists don't just know pandas—they understand their data. By the end of this course, you'll understand *this* data: why wharver prices spiked in late March, why the Deep Tunnel Syndicate works alone, why catches come in prime numbers.

4. **Learning should be interesting.** If you're going to spend hours staring at code, the code should be doing something more compelling than calculating quarterly revenue.

---

## The World

**Densworld** is a fictional universe with its own history, geography, and natural laws. Yeller Quarry is one location within it—a massive extraction zone where crews descend into tunnels and marshes to trap creatures for sale to Capital merchants and archivists.

The year is **1855**. The technology is roughly Victorian. The creatures are not.

You don't need to know anything about Densworld to complete these tutorials. Everything you need is in the data and the narrative snippets that introduce each lesson. But if you find yourself curious about the wider world—the ore deposits, the political structure, the other quarries—that's by design.

### Key Concepts

**Yeller Groups**: Creatures in the Quarry sometimes move in synchronized groups of prime numbers—2, 3, 5, 7, or rarely 11. Nobody knows why. The trappers call this phenomenon "yellering."

**The Boss**: A legendary trapper who designed most of the traps still in use. She disappeared during the Redmane Expedition in March 1855. Her body was never recovered.

**Archivists**: Scholars in the Capital who study, catalog, and purchase Quarry specimens. Chief Archivist Mink runs the records division where you, the apprentice, are learning your trade.

**Live vs. Dead**: Live specimens are worth more but are far more dangerous to transport. Some creatures cannot survive capture.

---

## The Tutorials

Each tutorial teaches specific pandas skills through a narrative frame. You'll work through the notebook, learn the techniques, then complete exercises that require you to apply them.

| # | Tutorial | What You'll Learn | The Story |
|---|----------|-------------------|-----------|
| 1 | The Creature Catalog | Loading data, basic inspection | Your first day in the Archives |
| 2 | Trap Deployment Records | Filtering, boolean logic | Gull explains how traps work |
| 3 | The Catch Ledger | Sorting, aggregation | Calculating what the Quarry produces |
| 4 | The Art of Grouping | Groupby operations | Finding patterns across crews |
| 5 | Joining the Ledgers | Merging DataFrames | Cross-referencing multiple records |
| 6 | Time in the Quarry | Datetime operations | Tracking prices and seasons |
| 7 | Patterns in the Darkness | Pivot tables | The Constabulary asks for help |
| 8 | Cleaning the Archives | Handling messy data | Trappers can't spell |
| 9 | Seeing the Quarry | Visualization | Making charts for the senators |
| 10 | The Investigation | **Capstone project** | Three children are missing |

### The Capstone

Tutorial 10 is different. Instead of guided instruction, you'll conduct an independent investigation using everything you've learned. 

Three children have disappeared near the Quarry boundary. The constable thinks it's creature attacks. The trappers think it's something else. Chief Archivist Mink thinks it's a pattern.

Your job is to find it.

---

## How to Use This Course

### Option 1: Google Colab (Recommended)

Click any "Open in Colab" badge in the README. The notebook will open in your browser. You don't need to install anything.

1. Click the badge
2. Sign in with a Google account
3. Go to **File → Save a copy in Drive** to keep your work
4. Work through the notebook
5. Complete the exercises

### Option 2: Local Installation

If you prefer working locally:

```bash
git clone https://github.com/buildLittleWorlds/yeller-quarry-data-science.git
cd yeller-quarry-data-science
pip install pandas matplotlib seaborn jupyter
jupyter notebook
```

### The YouTube Videos

Each tutorial has an accompanying video walkthrough where your professor:

- Introduces the narrative context
- Demonstrates the pandas techniques
- Works through the code live
- Offers tips and explanations not in the notebook

**Watch the video first**, then work through the notebook yourself. Or work through the notebook first and use the video to check your understanding. Both approaches work.

---

## The Data

Six CSV files in the `data/` folder:

| File | Records | Description |
|------|---------|-------------|
| `creatures.csv` | 25 | Species catalog with danger ratings, depths, metal content |
| `crews.csv` | 12 | Trapping crews with leaders, specialties, formation dates |
| `traps.csv` | 35 | Trap deployments with locations, bait, outcomes |
| `catches.csv` | 50 | Actual catches with quantities, prices, conditions |
| `prices.csv` | 75 | Weekly market prices from Capital traders |
| `incidents.csv` | 30 | Accidents, attacks, disappearances, strange phenomena |

The data is internally consistent. Dates align. Creature IDs match across files. The patterns are real—if you look hard enough, you'll find them.

---

## A Note on Difficulty

This course assumes you know basic Python: variables, loops, functions, lists. If you don't, spend a few hours with any introductory Python tutorial first.

The pandas content starts from zero. Tutorial 1 assumes you've never seen a DataFrame before.

By Tutorial 10, you'll be doing real analysis. The difficulty curve is intentional.

---

## Questions?

If something doesn't work, check:

1. Are you running the code cells in order?
2. Did you load the data first?
3. Is your Colab runtime still connected?

If you find an error in the materials, let your professor know. This is a first experiment. Edges are still being sanded.

---

## One Last Thing

The world of Yeller Quarry is dark. Trappers die. Children go missing. The data reflects this.

If you find yourself unsettled, good. Data is never neutral. Every row in an incident report was someone's worst day. The numbers mean something.

That's the other lesson here, underneath the pandas syntax: data science is a human enterprise. The creatures in these files aren't real, but the skills you're learning will someday be applied to data that is.

Handle it carefully.

---

*"Most archivists live in the Capital, were born in the Capital, schooled in the Capital, work and will die in the Capital. But the very best of them come from outside Yeller Quarry."*

*Now you know why.*

---

**Ready?**

[Start Tutorial 1 →](https://colab.research.google.com/github/buildLittleWorlds/yeller-quarry-data-science/blob/main/notebooks/tutorial_01_creature_catalog.ipynb)