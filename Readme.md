# Drone Patterns Project

## Overview
This project contains various algorithms and patterns for drone programming and general programming practice. The main focus is on implementing different algorithms and control patterns for drone operations.

## Project Structure


## Featured Components

### Binary Search Implementation
Located in `algo/search/binary/`, this implementation includes:
- `binary_search.py`: Generic recursive binary search algorithm
- `Runme.py`: Interactive interface for testing binary search
- `test_binary_search.py`: Unit tests for the binary search implementation

#### Binary Search Features
- Generic type support using Python's TypeVar
- Recursive implementation
- Supports multiple data types (int, float, string)
- Returns -1 if item not found
- Works with sorted lists only

#### Running the Binary Search Program
1. Navigate to the binary search directory: bash cd algo/search/binary
2. Run the program: bash python Runme.py
3. Usage:
- Select a data type by entering 'int', 'float', or 'string'
- Enter values to search for in the selected list
- Type 'back' to change data type
- Type 'quit' to exit the program

### Drone Control
The project includes various drone control patterns and utilities:
- Basic movement patterns
- Temperature and attitude monitoring
- Coordinate-based movement
- Threading implementations for parallel operations

## Requirements
- Python 3.10.17>=
- Virtual environment management with virtualenv

## Setup
1. Clone the repository
2. Create and activate virtual environment:

#### Linux/Mac
```bash
python -m venv .venv 
source .venv/bin/activate
```
or
```bash
python3.10 -m venv .venv 
source .venv/bin/activate
```

#### Windows
```bash
python -m venv .venv 
source .venv\Scripts\activate
```
or
```bash
python3.10 -m venv .venv 
source .venv\Scripts\activate
```