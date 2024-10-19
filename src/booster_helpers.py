# Function for simulating opening a booster pack

import random

# Import the parameters for a booster pack
import config.booster as bstr

# Simulate opening a booster pack
def open_booster(set_df, seed_num = None):

    # Set the random number generator seed for reproducibility if provided
    if seed_num is not None:
        random.seed(seed_num)
    
    # Randomly select commons without replacement
    common_card_ids = set_df[set_df['rarity'] == 'common'].card_id.to_list()
    common_card_ids_pulled = random.sample(common_card_ids, 
                                           bstr.NUM_COMMONS_IN_BOOSTER)

    # Randomly select commons without replacement
    uncommon_card_ids = set_df[set_df['rarity'] == 'uncommon'].card_id.to_list()
    uncommon_card_ids_pulled = random.sample(uncommon_card_ids, 
                                             bstr.NUM_UNCOMMONS_IN_BOOSTER)

    # Randomly select commons without replacement
    rare_or_better_list = ['rare', 'super_rare', 'legendary']
    rare_or_better_card_ids = set_df[set_df['rarity'].isin(rare_or_better_list)].card_id.to_list()
    rare_or_better_card_ids_pulled = random.sample(rare_or_better_card_ids, 
                                                   bstr.NUM_RARES_SUPER_RARES_OR_LEGENDARIES_IN_BOOSTER)

    # Combine cards into booster
    booster_card_ids_pulled = common_card_ids_pulled + uncommon_card_ids_pulled + rare_or_better_card_ids_pulled # TODO: Foileds

    return booster_card_ids_pulled

# Simulate opening n boosters
def open_n_boosters(num_boosters, set_df, seed_num=None):

    # Initialize the output
    total_cards_pulled = []

    # Set the random number generator seed for reproducibility if provided
    if seed_num is not None:
        random.seed(seed_num)

    # Open num_boosters boosters
    for _ in range(num_boosters):
        booster_card_ids_pulled = open_booster(set_df)
        total_cards_pulled += booster_card_ids_pulled
    
    return total_cards_pulled