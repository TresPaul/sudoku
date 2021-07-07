# A mediocre sudoku solver

I hate puzzles like sudokus. They're repetitive and frustrating. Every time I try to do one I think to myself, "jeez if only this could be automated". So I decided to try to do what I much rather prefer, which is thinking about the algorithms used to solve sudokus.


## Method

This solver is meant to reflect how I would go about doing a sudoku. First the possibilities for each open space is pruned by removing numbers that appear in the cell's row, column, or block, iterating over all the cells repeatedly until nothing is changed. Then, unique possibilities are found in the combined possibility space for each row, column, and block, which then have to be the result for the cell they are in; this is again repeated until nothing changes. These two steps are then alternated until a solution is found. (At the moment it does not halt if a solution is not found because the `changed` flag isn't in the scope in which the alternating is done, and this would thus require refactoring or passing around the flag in function arguments, which is inelegant. And I also didn't want to have to deep copy the whole puzzle on each iteration to watch for changes.)


## Usage

```
python sudoku.py <puzzle>
```

The solver works for "easy" to (some) "hard" puzzles (as found on sudoku.com). "Hard" and "expert" puzzles (can) have features that prevent solving with the algorithms described above, and I have not figured out how they work yet.


## Ideas

Since I threw this together in like a day, it could be much better. Firstly, it could stop when it can't make any more progress, instead of infinitely looping. The interface can perhaps also ask for the puzzle input if a file is not passed on the command line.

Algorithmically, it inefficiently rechecks all cells instead of only those that are influenced by a change. This could be solved by walking through until a change is found, and from there recursively "following" the changes that have to be made along each row, column, and block. The code can also be made to be object-oriented, such as with puzzle class with an `update` function which automatically recursively calls `update` on the cells affected by the first `update` call.

Extension with more algorithms might benefit from using numpy.

Also I might have shown a bit too much enthusiasm for list comprehensions in some spots.
