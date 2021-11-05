"Mark43 Poker" Judger
=====================

Your task is to implement a program that judges a game of three-card poker.

Input Format
------------

The input should be read over `stdin`. Some of the lines will contain collections of cards. These cards will be represented in the format format `<rank><Suit>`. rank will be one of:

* an integer from `2` to `9` for numbered cards less than ten
* `T` for ten
* `J` for jack
* `Q` for queen
* `K` for king
* `A` for ace

Suit will be one of:
* `h` for hearts
* `d` for diamonds
* `s` for spades
* `c` for clubs

Some example cards are `4d` for four of diamonds, `Ts` for ten of spades, and `Ah` for ace of hearts.

Input Data
----------
The first line of input will contain a single integer representing the number of players. This number will always be greater than 0 and less than 8.

The following `n` lines, where `n` is the number of players, will contain a single integer representing the id of the player, followed by three space-separated cards representing a hand belonging to a player.

An example input is as follows:

```
3
0 2c As 4d
1 Kd 5h 6c
2 Jc Jd 9s
```

Output Format
-------------

The output, printed to `stdout`, should simply be the id of the winning player. In the example above, the correct output would be:

```
2
```

as player two has the winning hand.

In the event of a tie, the ids of the winning players should be output on one line, space-separated, in ascending order. For example, for the input:
```
4
0 Qc Kc 4s
1 Ah 2c Js
2 3h 9h Th
3 Tc 9c 3c
```

the correct output would be:

```
2 3
```
as those two players have equivalent hands (flushes, with a ten, a nine, and a three).

"Mark43 Poker" Rules
----------------------

The winner of a round of  is the player with the best hand. The possible types of hands, ranked best to worst, are as follows:

* **Straight Flush:** A straight flush is a hand that is both a straight and a flush. That is, all three cards have the same suit, and their ranks form a "run" (check out the explanation for a straight).

* **Three Of A Kind:** A three of a kind is a hand in which all three of the cards have the same rank. An example might be `4c 4h 4d`, as all three cards are fours.

* **Straight:** A straight is a hand in which the cards have ranks that are in a "run." This means that they are of the format `n, n+1, n+2`. For example, the hand `5h 3c 4d` is a straight, because the cards can be ordered `3c 4d 5h` to form a "run" of `3-4-5`. The full order of the cards is `A, 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A`. Note that `A` appears as both the highest and lowest card.  Face cards form runs when they appear in that order, so `Qh Kd As` is a straight, because they form a run of `Q-K-A`. Runs can also include numbers and face cards, so `9h Td Js` is straight because it forms a run of `9-T-J`. When considering a straight, aces can also be used as a 1. That means that `A-2-3` is also a run. An ace cannot, however, be both high and low in the same straight, so `K-A-2` does not qualify.  The highest possible straight is `Q-K-A` and the lowest possible is `A-2-3`.

* **Flush:** A flush is a hand in which all three cards have the same suit. An example might be `Ac 4c 8c`, as all three cards are clubs.

* **Pair:** A pair is a hand in which two of the cards have the same rank, but the third is different. An example is `4c 4d Ah`. This is a "pair of fours", because it has two fours.

* **High Card:** Any hand that doesn't fit into one of the other categories is considered a "high card" hand.

When comparing hands of the same type, the winner is the hand whose highest card is ranked higher. Therefore, `Ah 5h 2h` beats `Qd Jd 7d` because the first hand's highest card, an Ace, is ranked higher than the second hand's highest card, a Queen. If the highest cards are equal, then the second highest cards should be compared. If those are equal, the third highest cards should be compared. If all three are equal, then the hands are tied.

The exception to this comes when comparing pairs. If two hands are both a pair, the winning hand is the hand that has a higher pair. For example `8c 8h 4d` beats `5s 5h 2h` because the pair of `8`s beats the pair of `5`s. If the pair is tied, then the remaining card is used to decide the winner.  (Fun fact, the "extra" cards in a poker hand that are not part of the hand ranking but are used to break ties are called "kickers".)

Mark43 poker is actually just 3 Card Poker. You can read more about it [in this wikipedia article.](https://en.wikipedia.org/wiki/Three_card_poker) For a clear list of hand rankings, see [this page](https://www.table-games-online.com/3-card-poker/hand_ranking.html).

Using the test runner
----------------------

We have provided the test runner that we will use to check your solution, along with two sample tests. We have many more tests that we will run internally, so passing the two we sent *does not* imply that your solution is correct/complete.

To run the tests, first perform any compilation or preprocessing that your solution requires, then use the `run_tests` python script and pass the command that runs your program in as a string argument. For example, if your program is a python file called `poker.py` that you invoke with `python poker.py`, then you would run `./run_tests "python poker.py"`. Or, if your program is Java code that you have compiled to `Poker.class` and invoke with `java Poker`, you would run `./run_tests "java Poker"`.  Make sure you run this from the directory where the `run_tests` script and `tests` directory are located.

The `run_tests` script uses Python 3, so you may need to invoke it with `python3 ./run_tests "<your command>"` if your installed version of `python` points to Python 2.  (In which case, you should also upgrade it to Python 3 because [Python 2 was end-of-lifed on 1 January, 2020](https://pythonclock.org)).

Feel free to reach out to us if you have any problems using the test runner.

What to submit
--------------

Your submission **must** be a **zip file** containing the following:

* the source code of your program
* a plain text file titled `README` containing
    * detailed instructions for compiling and/or running your submission.  (The person grading your submission may be unfamiliar with the language you used, so be explicit here).  
    * a brief note about design decisions and known bugs or limitations in your submission.

If your submission requires a multi-step or otherwise complex compilation process, you **should** include a `Makefile` or other build script.

Your program **must** be able to run all of the included tests using our `run_tests` script as described above. We will use this exact script to grade your test, so if your submission doesn't run with `run_tests` for you, then it won't run for us.

Your submission **must not** contain your name in any file, as we use a blind grading process.

Your submission **should not** contain any compiled code.  We want to compile your submission ourselves.  If you have a good reason for including compiled code, you **should**  explain in your `README`.
