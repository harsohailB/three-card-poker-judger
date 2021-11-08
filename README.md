# Mark43 Three Card Poker - Solution (Python)

## Running the Code

1. Navigate to `game` folder which contains game code and `run_tests`

```
cd game
```

2. Run the following command to run the `run_tests` file with the game code

```
python3 run_tests "python3 main.py"
```

## Design Decisions

### Modularization

As the three card game of poker in real life has multiple entities that have their own roles, the code presented uses object oriented programming follow the same principle by splitting these entities into different objects. The classes of these objects are as follows:

- Game - `game.py`

  - Acts as a dealer by being responsible for creating players and assigning cards
  - Responsible for determining the winner through comparing players

- Player - `player.py`

  - Responsible keeping track of its cards and evaluating them

- Card - `card.py`

  - Holds the rank and suit of a card

- Deck - `deck.py`

  - Holds all the cards that would be in a deck

- Main Driver - `main.py`

  - Entrypoint of the poker game that parses input to create game and output winners

### Deck - Singleton Design Pattern

The singleton design pattern was used for the `Deck` class as only one deck should ever exist in a game of three card poker. Therefore, through making this class a singleton class, we can only ever have a single instance of it. Refer to the docs in `deck.py` for more details on this.

### Hand - Enum class

The `Hand` class was created as an enum to simply store the strengths of all the hands in three card poker. This allows for simple comparisons when trying to calculate a winner.
