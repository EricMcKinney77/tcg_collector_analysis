# This file simulates a collection from a loaded simulated TCG set

import pandas as pd

# Import support funs
from src.booster_helpers import open_booster, open_n_boosters
from src.collection_helpers import create_collection, add_cards_to_collection, plot_collection, analyze_collection
from src.simulation_helpers import grow_collection

# Load the set dataframe
set_df = pd.read_pickle('data/shimmering_skies.pkl')

# Create a collection based off of the set
collection_df = create_collection(set_df)

# Simulate opening n boosters
booster_card_ids_pulled = open_n_boosters(20, set_df)

# Add pulled cards to collection
collection_df = add_cards_to_collection(booster_card_ids_pulled,
                                        collection_df=collection_df.copy())

# Analyze collection
analyze_collection(collection_df)

# Plot a bar chart of the collection
plot_collection(collection_df, '10_boost_collection')

# Make a plot of stats per booster puchased
# Collect a list of statistics per booster purchase
stats_list = grow_collection(set_df, collection_df, 20)

import matplotlib.pyplot as plt

plt.plot(stats_list)
plt.xticks(range(0,len(stats_list) + 1))
plt.yticks([x / 10 for x in range(0, 11)])
plt.ylim((0, 1))
plt.grid()
plt.show()
plt.close()
