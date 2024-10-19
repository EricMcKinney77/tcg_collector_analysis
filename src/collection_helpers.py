# Card collection helper funs

import matplotlib.pyplot as plt

def create_collection(set_df):
    collection_df = set_df.copy()
    collection_df['num_collected'] = [0] * len(collection_df)
    return collection_df

def add_cards_to_collection(card_id_list, collection_df):

    # Add the cards from the booster to the collection
    for card_id_pulled in card_id_list:
        collection_df.loc[collection_df['card_id'] == card_id_pulled, 'num_collected'] += 1

    return collection_df

def plot_collection(collection_df, save_name=None):

    # Make a plot of the collection
    try:
        collection_df.plot(x='card_id', y='num_collected', kind='bar')
        plt.xlabel('card_id')
        plt.ylabel('num_collected')
        plt.ylim(0, 10)
        if save_name is not None:
            plt.savefig(f'figures/{save_name}.png')
        plt.close()
    except Exception as excpt:
        print(f'An error occurred: {excpt}')

def analyze_collection(collection_df, print_stats=None):

    # Store the number of possible cards
    num_possible_cards = len(collection_df)

    # Proportion of cards with at least one collected
    prop_w_at_least_one = sum(collection_df['num_collected'] >= 1) / num_possible_cards

    if print_stats is not None:
        print(f'prop_w_at_least_one = {prop_w_at_least_one}')

    return prop_w_at_least_one
