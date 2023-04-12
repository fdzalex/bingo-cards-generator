# Bingo Card Generator

This Bingo Card Generator is a Python script that creates unique bingo cards and saves them to a CSV file. Each card contains 5 rows and 5 columns of numbers, with the center cell of each card being an empty space (free space). The generated cards follow the standard bingo number ranges for each column: B (1-15), I (16-30), N (31-45), G (46-60), and O (61-75).

## Usage

1. Install Python 3.x if not already installed.
2. Download the `main.py` file to your local machine.
3. Open a terminal or command prompt, navigate to the directory where the script is located.
4. Run the following command:

```sh
python main.py
```

By default, the script generates 10,000 unique bingo cards and saves them to a file named `bingo_cards.csv`. To change the number of generated cards, modify the `num_cards` variable in the `__main__` section of the script.

## Customization

- To generate a different number of cards, change the value of `num_cards` in the `__main__` section of the script.
- To change the output file name, modify the second argument of the `write_cards_to_csv` function call in the `__main__` section.
