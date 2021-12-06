## --- Day 2: Dive! ---
Now, you need to figure out how to pilot this thing.

It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.
Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.

The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

_forward 5_

_down 5_

_forward 8_

_up 3_

_down 8_

_forward 2_

Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

_forward 5 adds 5 to your horizontal position, a total of 5._

_down 5 adds 5 to your depth, resulting in a value of 5._

_forward 8 adds 8 to your horizontal position, a total of 13._

_up 3 decreases your depth by 3, resulting in a value of 2._

_down 8 adds 8 to your depth, resulting in a value of 10._

_forward 2 adds 2 to your horizontal position, a total of 15._

After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
