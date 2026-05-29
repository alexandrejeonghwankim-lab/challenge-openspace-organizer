# OpenSpace Organizer
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## 🏢 Description

Our BeCode Gebru-1 moved to a new office in Brussels. Its an openspace with 6 tables of 4 seats. Since we are a new trainee in this program, our coach comes up with the idea of changing seats everyday and get to know each other better by working side by side with our new colleagues. 

This script runs everyday to re-assign everybody to a new seat.

![coworking_img](https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDd8fGRpdmVyc2UlMjB0ZWFtfGVufDB8fDB8fHwy)

## 📦 Repo structure

```
.
├── src/
│   ├── openspace.py
│   ├── table.py
│   └── utils.py
├── main.py
├── new_colleagues.txt
└── README.md

```

## 🛎️ Usage

1. Clone the repository to your local machine.

2 .To run the script, you can execute the `main.py` file from your command line:

```
   python main.py
```

3. The script reads names from input file, and organizes your colleagues to random seat assignments. The resulting seating plan is displayed in your console and also saved to a "new_list.txt" file in your root directory. 

```python
from utils.table import Table
from utils.openspace import OpenSpace
from utils.file_utils import read_namelist_file


def main():
    # Read all the names inside the file "new_colleagues.txt"
    names = read_namelist_file("new_colleagues.txt")

    # Create a new OpenSpace object. This will automatically create tables and seats inside
    space = OpenSpace()

    # It takes the list of names and assigns your colleagues to seats randomly. 
    space.organize(names)

    # display assignments in the terminal
    space.display()

    # save the seat assigments to a new file
    space.store("new_list.txt")

if __name__ == "__main__":
    main()
```
## ⏱️ Timeline

This project took two days for completion.

## 📌 Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 

Connect with me on [LinkedIn](https://www.linkedin.com/in/alexander-jeong-hwan-kim-b4921b170/).

