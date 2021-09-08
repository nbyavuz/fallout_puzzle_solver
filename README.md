# fallout_puzzle_solver

Trying to create alternative solutions for fallout word selection puzzle

### Changelog

- **Word selection method** : Now selects words for some probabilistic mumbo-jumbo criterion, not randomly. (Special thanks to mkaynarca, for coming up with that mumbo-jumbo) 

**Probabilistic mumbo-jumbo**

I am kinda new to all these python or coding and shit, so here is the word selection process in a manner that is way too informal. 

- Create similarity matrix that shows each words likeness to other words
- Let's say that a word with 5 letters, say word-1 has;


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
