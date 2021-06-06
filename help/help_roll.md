`!roll`
All forms of diceroll notations should work properly, including adding or detracting dice with each other, adding or detracting numbers from dicerolls, or even adding or detracting sums within brackets. Below are some examples.

```
Simple rolls

!roll 1d20+6
!roll 1d20-(2+6)
!roll 1d20-4+(1d4+3)

Advanced rolls

!roll 1d20x(N)
- exploding dice, will add extra dice on each roll above threshold N. If N is not defined, will default to maximum possible roll.

!roll 6d6^(N)
- highest N dicerolls will be kept, so 6d6^2 will keep the highest two dice.

!roll 6d6m(N)
- middle N dicerolls will be kept, so 6d6m2 will keep the middle two dice.

!roll 6d6v(N)
- lowest N dicerolls will be kept, so 6d6l2 wil keep the lowest two dice.

!roll 2d6r(N)
- will reroll any dice that are below threshold N. The reroll is possible to be below the threshold N.

!roll 2d6rr(N)
- will reroll any dice that are below threshold N. The reroll will be at the very minimum threshold N.

!roll 10d10s
- will sort the rolls in order, this will not change the result.
```