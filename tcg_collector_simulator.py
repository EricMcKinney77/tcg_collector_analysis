# This file simulates a collection from a loaded simulated TCG set

import pandas as pd
import random
import matplotlib.pyplot as plt

# Load the set dataframe
set_df = pd.read_pickle('data/shimmering_skies.pkl')

# Create a collection based off of the set
collection_df = set_df.copy()
collection_df['num_collected'] = [0] * len(collection_df)

# Simulate opening a booster pack
NUM_COMMONS_IN_BOOSTER = 6
NUM_UNCOMMONS_IN_BOOSTER = 4
NUM_RARES_SUPER_RARES_OR_LEGENDARIES_IN_BOOSTER = 2
# TODO: NUM_FOILED_IN_BOOSTER = 1

# Randomly select commons without replacement
common_card_ids = set_df[set_df['rarity'] == 'common'].card_id.to_list()
common_card_ids_pulled = random.sample(common_card_ids, NUM_COMMONS_IN_BOOSTER)

# Randomly select commons without replacement
uncommon_card_ids = set_df[set_df['rarity'] == 'uncommon'].card_id.to_list()
uncommon_card_ids_pulled = random.sample(uncommon_card_ids, NUM_UNCOMMONS_IN_BOOSTER)

# Randomly select commons without replacement
rare_or_better_list = ['rare', 'super_rare', 'legendary']
rare_or_better_card_ids = set_df[set_df['rarity'].isin(rare_or_better_list)].card_id.to_list()
rare_or_better_card_ids_pulled = random.sample(rare_or_better_card_ids, NUM_RARES_SUPER_RARES_OR_LEGENDARIES_IN_BOOSTER)

booster_card_ids_pulled = common_card_ids_pulled + uncommon_card_ids_pulled + rare_or_better_card_ids_pulled # TODO: Foileds

# Add the cards from the booster to the collection
for card_id_pulled in booster_card_ids_pulled:
    collection_df.loc[collection_df['card_id'] == card_id_pulled, 'num_collected'] += 1

# Make a plot of the collection
collection_df.plot(x='card_id', y='num_collected', kind='bar')
plt.xlabel('card_id')
plt.ylabel('num_collected')
plt.ylim(0, 10)
plt.show()
