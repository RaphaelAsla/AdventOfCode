# Advent of Code
Personal repository for my Advent of Code solutions
## About Advent of Code
Advent of Code is an Advent calendar of small programming puzzles for a variety <br>
of skill levels that can be solved in any programming language you like.<br>
People use them as interview prep, company training, university coursework, practice problems, a speed contest, or to challenge each other.
## About aoc-tools
`aoc-tools` is a collection of tools created by [brtwrst](https://github.com/brtwrst) to help with parsing and submitting Advent of Code puzzles more efficiently. <br>
It provides utility functions for parsing input in various formats (strings, numbers, grids, key-value pairs, etc.). <br>
Additionally, it includes functionality for automatically submitting the output of the solutions to Advent of Code <br>
so you don't have to manually copy-paste it in the browser.
## How to run my solutions
First, clone the repository along with it's submodule.
```bash
git clone --recursive https://github.com/RaphaelAsla/AdventOfCode.git
cd AdventOfCode
cd aoc-tools
```
Then we'll have to install aoc-tools.
```bash
### Optional
python3 -m venv .venv && source .venv/bin/activate
### Install in edit mode so the packet can be updated just by git pulling
cd aoc-tools
pip install -e . --config-settings editable_mode=compat
### or
pip install -e . --user --config-settings editable_mode=compat
```
Once you’ve installed aoc-tools, when you run a solution for the first time, you will be prompted to enter your Advent of Code session-cookie. <br>
This cookie can be found in the Chrome DevTools while you're logged in to [adventofcode.com](adventofcode.com). <br>
Then the solution will automatically fetch your input for the current day and submit your output. <br>
I’ve commented out the submission part in all solutions, so you don’t have to worry about accidentally submitting your answers.
