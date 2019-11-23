 
# Hex Game : Feedback on my Python implementation 

## Introduction
There's some kind of tradition in Marmelab. As you can see in the blog, each people starts his adventure by coding game.
I don't derogate to this tradition and I know that's a really versatile experience to identify our strengths and weaknesses.
Even if I've already make some applications, I'm a backend developer so develop a game is not my strong suit but I'm sure that kind of challenge will be as difficult as rewarding.

### The Hex game
Okay, let's talk a little about the game I have to implement : The Hex Game !
Hex game is a strategy game, played by two players, on a diamond-shaped board.
[Piet Hein](https://en.wikipedia.org/wiki/Piet_Hein_(scientist)) and [John Nash](https://en.wikipedia.org/wiki/John_Forbes_Nash_Jr.) invented him independently during 1940s. 
Many size and shape are possible but 11x11 rhombus is commonly used as the default configuration. 

#### Rules of the game
The goal is to join sides with a chain of stones of your color.
Each players has stones of color black or white and alternatively places stones on the board. Like chess, player with 
white stones starts. 
Because of his conception, there's no draw in Hex Game. You can find more details about this particularity here ; 

More details in [wikipedia] (https://en.wikipedia.org/wiki/Hex_(board_game))

### Hexagon in mathematics

## The program

### Technical stack 
To realize this game, we'll only use Python and the console output. I've used Python 3.6.
To setup and run the game, you can use the Makefile provided. He relies on Docker to install Python and libraries .
In fact, the game only needs Pytest library.
 
### Concepts & expectations
To keep something simple, I'll only manage one player. Considers that like a very limited training mode. 
I'll also provide a basic error handling system. Because it's not really the point of this article, it's just to avoid 
some silly situations :
- Wrong input 
- Put a stone outside the board
- Try to take an already set case

## Considerations before starting

### Drawing hexagon
To simplify a lot the render, we will use the "⬢" UTF-8 character when a stone is put on the board and this one "⬡" when the case is empty.

### Headers and rows indications
We'll use the convention to put stones on board. This convention is pretty similar to the chess one.
Eg. :
- A1 -> First line, first column
- B2 -> Second line, second colum
- C8 -> third line, 8th column, etc

In headers and raws, we'll indicate this grid.

## Let's begin ! 

### The game loop

To manage game flow, I use an infinite loop. The program shut off only when the game is won. You can terminate a game 
before if you use the CTRL + C command.

### The serious part

## Graph, node and path
 

 

