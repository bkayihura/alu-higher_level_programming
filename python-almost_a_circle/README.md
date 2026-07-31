# Almost a Circle

## Description
This project implements an object-oriented `Rectangle` and `Square` model
in Python, inheriting from a shared `Base` class. It covers OOP concepts
such as inheritance, class/static methods, property getters/setters with
validation, and serialization to/from JSON and CSV.

## Files
- `models/base. `Base` class: manages `id`, and providespy` 
  `to_json_string`, `from_json_string`, `save_to_file`, `load_from_file`,
  `create`, `save_to_file_csv`, and `load_from_file_csv`.
- `models/rectangle. `Rectangle` class, inherits from `Base`.py` 
- `models/square. `Square` class, inherits from `Rectangle`.py` 
- ` unit tests for all classes (`python3 -m unittest discover tests`).tests/` 

## Usage
```python
from models.rectangle import Rectangle
from models.square import Square

r = Rectangle(10, 2, 0, 0, 1)
print(r)  # [Rectangle] (1) 0/0 - 10/2

s = Square(5)
print(s)  # [Square] (1) 0/0 - 5
```

## Author
Your  ALU Higher Level ProgrammingName 
