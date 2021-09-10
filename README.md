# fallout_puzzle_solver

Trying to create alternative solutions for fallout word selection puzzle

### Changelog

**9.9.21 - Fallout Puzzle Solver - ver. 1.0 - YEA BOIIIII**

- **Now you can work with your own wordlist you cheater cunt. Go hack some terminals.**
- **I will move the good old test version to a new branch but i don't know how to do that. Might fail. So, IDK.** 
-  Websites below might be useful.



https://jetholt.com/hacking/

https://codepen.io/Smurff/pen/xzQPYy

http://aramor.epizy.com/fallout-terminal/










**8.9.21 - Fallout Puzzle Solver - ver. 0.5 - Test** 

-**This version is for testing the picking algorithm** 

Results was like dayum. We gave this piece of garbage 1000 words with 12 letters and get the password in 4-7 turns. Not so piece of garbage at all. 

Unfortunately you can not use your own wordlist for this version, as i said, it is for testing the algorithm. But don't worry, since we have pleasant results, we will start working on a basic console application. Might take a bit tho. I am not a CS student and we all have shits to do. 


- **Word selection method** : Now selects words for some probabilistic mumbo-jumbo criterion, not randomly. (Special thanks to mkaynarca, for coming up with that mumbo-jumbo) 

**Probabilistic mumbo-jumbo**

I am kinda new to all these python or coding and shit, so here is the word selection process in a manner that is way too informal. 

- Create similarity matrix that shows each words likeness to other words
- Let's say that a word with 5 letters, say word-x has;


0 similarity with 4 words

1 similarity with 2 words

2 similarity with 1 word

3 similarity with 0 words

4 similarity with 0 words 

and finally 5 similarity with 1 word which is itself.

- That means, if we choose word-x, depending on it's similarity with the password;


with 4/8 probability it will eliminate 4 words

with 2/8 probability it will eliminate 6 words

with 1/8 probability it will eliminate 7 words

with 1/8 probability it will eliminate 7 words

- With these results, we expect it to eliminate 42/8 = 5.25 words (mean operation)
- We calculate this for every word in the possible words 
- We take the word with "most expected elimination score" 
