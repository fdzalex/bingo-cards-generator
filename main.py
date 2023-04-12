import csv
import random

def generate_card():
    card = []
    card.append(random.sample(range(1, 16), 5))
    card.append(random.sample(range(16, 31), 5))
    card.append(random.sample(range(31, 46), 5))
    card[2][2] = 0  # Center is empty
    card.append(random.sample(range(56, 61), 5))
    card.append(random.sample(range(61, 76), 5))
    orderedCard = [list(x) for x in zip(*card)]
    return orderedCard

def card_to_str(card):
    return [','.join([str(cell) for cell in row]) for row in card]

def generate_unique_cards(num_cards):
    final_cards = []
    unique_cards = set()
    while len(unique_cards) < num_cards:
        generated_card = generate_card()
        card = card_to_str(generated_card)
        card_str = '-'.join(card)
        if card_str not in unique_cards:
            unique_cards.add(card_str)
            final_cards.append(generated_card)
    return final_cards

def write_cards_to_csv(cards, filename):
    with open(filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        for card in cards:
            for row in card:
                csv_writer.writerow(row)
            csv_writer.writerow([])  # Add an empty row between cards

if __name__ == "__main__":
    num_cards = 10000
    cards = generate_unique_cards(num_cards)
    write_cards_to_csv(cards, "bingo_cards.csv")
