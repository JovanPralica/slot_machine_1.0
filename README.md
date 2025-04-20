
# Slot Machine 1.0

Welcome to **Slot Machine 1.0**, a text-based slot machine game built with Python. This program allows users to simulate a fun and interactive slot machine experience in the console. 

## Features

- Interactive slot machine interface with various emojis.
- Multiple bet and deposit options.
- Special bonuses such as Cherry and Rocket bonuses.
- Dynamic grid rotation with a chance to win based on matching symbols.
- User balance updates after each round.
- Real-time game interaction using keyboard inputs (`SPACE` to bet and `W` to withdraw).

## Requirements

- Python 3.x
- `pynput` library for keyboard input handling.

## Installation

To get started, you'll need to install the `pynput` library. You can install it using `pip`:

```bash
pip install pynput
```

## How to Play

1. **Start the game**: After running the program, you'll be prompted to input your balance and bet amount.
   
   - Available deposits: `5, 10, 25, 100, 250`
   - Available bet amounts: `0.5, 1, 2.5, 5, 10`

2. **Place a bet**: Once the inputs are validated, you can start spinning the slot machine.

3. **Spin the reels**: Press the **SPACE** key to spin the slot machine. The machine will show a 3x3 grid of emojis, and you will be able to see if you've won.

4. **Withdraw**: If you'd like to end the game and withdraw your balance, press the **W** key.

5. **Winning Conditions**: You can win in several ways:
   - **Single Symbol Wins**: Matching symbols in rows or columns (e.g., three matching `🍒` or `🚀`).
   - **Special Bonuses**: Special symbols like `🍒` and `🚀` trigger bonus messages.
   - **Winning Multipliers**: The program displays multipliers based on the number of matching symbols.

## Controls

- **SPACE**: Spin the slot machine.
- **W**: Withdraw your balance and exit the game.

## Example Output

```
🎰💎🍀  SLOT MACHINE 1.0  🎰💎🍀

          🍒   🍊   🍇
          🚀   🍋   🍇
          🍒   🍒   🍇

         Balance:[50]
       Balance:[50] [WIN]
(W / SPACE) Withdraw / Bet:
```

## Special Bonuses

- **🍒 Cherry BONUS 🍒**: Activated when `🍒` symbols match in rows or columns.
- **🚀 Rocket BONUS 🚀**: Activated when `🚀` symbols match in rows or columns.

## Troubleshooting

- If the program doesn't run, make sure you have Python 3.x installed and the necessary libraries are installed.
- Ensure that your terminal window is large enough to display the grid and game messages clearly.

## License

All rights reserved. This code is proprietary and may not be copied, modified, distributed, or used for any purpose without explicit permission from the author. Redistribution of this code, whether in original or modified form, is strictly prohibited. By using or viewing this project, you agree to these terms.

## Acknowledgements

- This program uses the `pynput` library for keyboard input handling.
- The slot machine logic is based on a random emoji grid and simple game rules.

Enjoy the game and good luck! 🍀🎰
