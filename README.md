# CS-351 Directed Graph Project

## Overview
This project implements a **directed weighted graph** with two traversal algorithms:
- Depth-First Search (DFS)
- Breadth-First Search (BFS)

The program reads data from `graph.txt`, builds the graph, and prints and saves traversal orders.

---

## Files
| File | Description |
|------|--------------|
| `graph_interfaces.py` | Interface definitions for Graph, Vertex, and Edge |
| `graph_impl.py` | Implementations of Graph, Vertex, and Edge |
| `program.py` | Main driver that reads data, runs traversals, and writes outputs |
| `graph.txt` | Graph data file (Oregon city connections) |
| `dfs.txt` / `bfs.txt` | Output traversal results |

---

## How to Run
1. Clone the repository.
2. Ensure `graph.txt` is in the same directory.
3. Run the program:
   ```bash
   python program.py
4. when you are prompted to enter a start vertex name, enter one from the graph.txt file
5. dfs and bfs outputs will appear in the console and also be saved in dfs.text and bfs.txt

    Ex: Salem (It is case sensitive so be sure to start with a capital letter)

    Example output:

    DFS Traversal:
    Salem
    Portland
    Astoria
    Seaside
    Tillamook
    Newport
    Corvallis
    Eugene
    Bend
    Redmond
    Madras
    The_Dalles
    Hood_River
    Pendleton
    Ontario
    Burns
    Crater_Lake
    Medford
    Roseburg
    Coos_Bay
    Florence
    Ashland

    BFS Traversal:
    Salem
    Portland
    Eugene
    Corvallis
    Astoria
    Hood_River
    Newport
    Bend
    Crater_Lake
    Roseburg
    Seaside
    The_Dalles
    Tillamook
    Florence
    Redmond
    Burns
    Medford
    Coos_Bay
    Pendleton
    Madras
    Ashland
    Ontario


---

Author:

Aris Whitney
CS-351 --Fall 2025

---

Notes:
1. Graph is directed
2. Vertices are uniquely identified by name
3. bfs and dfs implmentations do not revisit nodes
4. Traversal outputs are written to dfs.text and bfs.txt