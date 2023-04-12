import csv
import random

# Function to generate a single bingo card
def generate_card():
    card = []
    # Generate 5 random unique numbers for each column within their respective number ranges
    card.append(random.sample(range(1, 16), 5))   # B column (1-15)
    card.append(random.sample(range(16, 31), 5))  # I column (16-30)
    card.append(random.sample(range(31, 46), 5))  # N column (31-45)
    card[2][2] = 0  # Center cell of N column is empty (free space)
    card.append(random.sample(range(46, 61), 5))  # G column (46-60)
    card.append(random.sample(range(61, 76), 5))  # O column (61-75)
    
    # Rotate card to have columns as rows
    orderedCard = [list(x) for x in zip(*card)]
    return orderedCard

# Function to convert card to a list of strings (rows)
def card_to_str(card):
    return [','.join([str(cell) for cell in row]) for row in card]

# Function to generate a specified number of unique bingo cards
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

# Function to write generated cards to a CSV file
def write_cards_to_csv(cards, filename):
    with open(filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        for card in cards:
            for row in card:
                csv_writer.writerow(row)
            csv_writer.writerow([])  # Add an empty row between cards to separate them

# Main execution
if __name__ == "__main__":
    num_cards = 10000
    # Generate the specified number of unique bingo cards
    cards = generate_unique_cards(num_cards)
    # Write the generated cards to a CSV file
    write_cards_to_csv(cards, "bingo_cards.csv")
