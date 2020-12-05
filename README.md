# Graph visual
## Description
Just little project of graph visualizer and generator. Supports random generation and graphical output.

Basic example:  
`python main.py --color 0 0 255 random 10`
This will generate random graph and display it with blue lines color.  
For more examples see "Command examples" 

## Requirements
1. pygame==1.9.6 (graphics support)
2. click==7.0 (CLI support)

## Usage
### Basics
Usage: python main.py \[options\] \<command\> \[options\] \<parameters\>

Options:
- --width <int> - sets up lines width
- --color <int> <int> <int> - sets up lines color (RGB)
- --vsize <int> - vertices circle radius
- --screen <int> <int> - sets up window size

Commands:
1. random - generate graph and show it
2. matrix - take adjacency matrix by stdin and visualize graph

### Commands description
#### 1. Random
Usage: python main.py \[options\] **random** \[options\] **N**

N - count of vertices in graph

Options:
- --fill <float> - how much edges will be generated between vertices (**between 0 and 1**)
- --weights <int> <int> - range of weights to generate (**include both borders**)

#### 2. Matrix
Usage: python main.py \[options\] **matrix** **N**  
Than you should input **N** lines of adjacency matrix. Or just paste from buffer.

N - count of vertices in graph

Without options

### Command examples
#### 1. Random
1. Basic example, will be generated graph with 10 vertices, random weights and connections  
`python main.py random 10`
2. Customize edges fill factor (not much connections)  
    `python main.py random --fill 0.2 15`
3. Any vertex connected with all other vertices (fill = 1)  
    `python main.py random --fill 1 15`
4. Customize weights random generator (sets randint(1000, 2000))  
    `python main.py random --weights 1000 2000 10`

#### 2. Matrix
1. Basic example, will be shown passed graph with 5 vertices  
    `python main.py matrix 5`


#### 3. Style customization
1. Apply blue color to random graph  
    `python main.py --color 0 0 255 random 10`
2. Apply 3px line width to random graph  
    `python main.py --width 3 random 10`
3. Resizing window  
    `python main.py --screen 900 900 random 25`
4. Apply 30px vertices radius on random graph  
    `python main.py --vsize 30 random 5`
5. Complicated options usage (will be generated random graph with 10 vertices and displaying with blue color and line width 2px)  
    `python main.py --color 0 0 255 --width 2 random --fill 0.3 10`
