## Cellular Automata Sandbox
![img.png](img.png)
**No AI was used in code development**. Only doc generation from code previously developed.

### The Nature of Code - Cellular Automata

A cellular automaton (cellular automata plural, or CA for short) is a model of a system of cell objects with the following characteristics:

* **The cells live on a grid.** (I’ll include examples in both one and two dimensions in this chapter, though a CA can exist in any finite number of dimensions.)
* **Each cell has a state**, though a cell’s state can vary over time. The number of possible states is typically finite. The simplest example has the two possibilities of 1 and 0 (otherwise referred to as on and off, or alive and dead).
* **Each cell has a neighborhood**. This can be defined in any number of ways, but it’s typically all the cells adjacent to that cell.

https://natureofcode.com/cellular-automata/

### What inspired me into doing this project
- https://www.youtube.com/watch?v=wbPgoZ2d0Nw
- https://dan-ball.jp/ (ANT)
- https://www.youtube.com/watch?v=W1zKu3fDQR8
- https://www.youtube.com/watch?v=JEPHf9n3Dgc

### How to run the 2D automata
#### Disclaimer
Well... this one uses **[pygame](https://www.pygame.org/contribute.html)**, so you may need to run `pip install pygame` before running the program. I'd recommend using a virtual environment (venv) specifically for this. Here are the instructions:
You may just run: 
1. Create a virtual environment:
   ```bash
   python -m venv $venv_name
   ```
2. Get into your venv
   ```bash
   $venv_name/bin/activate
   ```

#### Running the 2D automata
```bash
python 01_basics/2d_automata_w_pygame.py
```

or a more customized approach:

```bash
python 01_basics/2d_automata_w_pygame.py --height $height_size --width $width_size --tick $generations_per_sec
```

### How to run 1D automata
The `generateWithOneInTheMiddle` function is executed through the script's command-line interface. To run it, use the following command:

Get your ruleset number [here](https://plato.stanford.edu/entries/cellular-automata/supplement.html)!

**Try me out!**
```bash
python 01_basics/1d_automata.py 86 --generations 100
```

**Template command**
```bash
python 01_basics/1d_automata.py <ruleSetNumber: int> --generations <number_of_generations>
```
