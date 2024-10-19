
# Import support funs
from src.booster_helpers import open_booster
from src.collection_helpers import add_cards_to_collection, analyze_collection

def grow_collection(set_df, collection_df, num_boosters):

    stats_list = []
    for _ in range(num_boosters):
        # Open a booster
        booster_card_ids_pulled = open_booster(set_df)

        # Add to collection
        collection_df = add_cards_to_collection(booster_card_ids_pulled,
                                                collection_df=collection_df.copy())

        # Analyze the collection
        prop_collected = analyze_collection(collection_df)

        # Store the statistic
        stats_list.append(prop_collected)
    
    return stats_list
