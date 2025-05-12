# Game-Simulation
A game simulation script I wrote to best the game rules below for an interview competition. The simulation accurately suggested the winning number.

You must select a number between 0 - 100 amongst 8 opponents. One player is not interested in winning and will submit a chaotic choice.

The winning conditions are as follows in order of Priority:
1. The entry that is the lowest number higher than the average of all received numbers will win.
2. In the event of a tie greater than 2 people, the next highest number will win.
3. If no such entry exists, then the highest number lower than the average will win.
