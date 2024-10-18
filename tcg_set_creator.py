# This file generates a csv file which provides all of the metadata of a simulated TCG set to collect from

import pandas as pd

# Import the parameters for a particular set
import config.shimmering_skies as tcg

# Generate card numbers for each rarity
# Card numbers
card_nums_list = [x + 1 for x in range(tcg.NUM_CARDS)]

# Card rarities
card_rarity_list = []
for card_rarity_name, card_rarity_num in tcg.NUM_CARDS_DICT.items():
    individual_rarity_list = [card_rarity_name] * card_rarity_num
    card_rarity_list = card_rarity_list + individual_rarity_list

# TODO: Card foiled

# Combine into a single dataframe
card_data = {'card_num': card_nums_list, 'rarity': card_rarity_list}
set_df = pd.DataFrame(card_data)

# Store the dataframe as a pickle file
set_df.to_pickle('data/shimmering_skies.pkl')
