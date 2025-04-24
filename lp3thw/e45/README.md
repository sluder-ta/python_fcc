# LP3THW Exercise 45
In this exercise, I've been instructed to make a game with the following requirements:
1. Make a different game from the one(s) previously made.
2. Use more than on file, and use import to use them.
3. Use one class per room and give the classes names that fit their purposes
 (like GoldRoom, KoiPondRoom).
4. Make a class that runs the rooms and knows about them. Consider having each room
return what room is next or setting a variable of what room is next.

## Initial Game Idea - Working title <Labours>
I like the idea of a short RPG. What if I used the Herculean Labors/Tasks as my rooms,
and you win the game by completing them all?
Labors:
- Slay the Nemean Lion
- Slay the Lernaean Hydra
- Capture the Ceryneian Hind
- Capture the Erymanthian Boar
- Clean the Augean tables
- Slay the Symphalian Birds
- Capture the Cretan Bull
- Steal the Mares of Diomedes
- Obtain the Girdle of Hippolyta
- Steal the Apples of the Hesperides
- Capture Cerberus

## Game Structure
For this game to work, I think I will have Heracles start in the chamber of King
Eurystheus and then choose which of the 12 labours to complete next. After each labour
(if Heracles survives) you return to the chamber to take on your next assignment. If
Heracles returns to the chamber and has completed all of he labours, you win! If
Heracles returns to the chamber after failing a task, you lose! Seems straightforward
enough.

### Class Use - Labours
I will use Labours as a class so that I can establish a general outline for each labour.
I will include some generic text for each of them, but I will modify each to adjust for
the labour required.

### Class Use - Hero
I will use a class to make Heracles a hero.

### Multiple File Usage
I can put my different classes into their own files and import them into my main game
file which will run the game engine.
