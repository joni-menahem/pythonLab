def sort_cards(player_cards):
    # will sort based on color first (blue, green, orange, red) and then by value
    sorted_list = sorted(player_cards, key=lambda x: (x[0], int(x[1:])))
    return sorted_list


cards = ['b5', 'o9', 'g6', 'g9', 'g8', 'o1', 'b10', 'o4', 'g2', 'r10']

print(sort_cards(cards))
