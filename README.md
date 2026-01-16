# goit-pycore-hw-04

## Topic 6. Working with Files and the Module System

This repository contains the solution for Homework 6 of the **Python Core (GoIT)** course.
The project demonstrates working with text files, using the `with` context manager, file system operations, CLI applications, and a console assistant bot.

---

## 🧩 Task 1 — Salary Analysis

### Description

Implemented the `total_salary(path)` function which:

* reads a text file with developers' salaries;
* calculates the **total** and **average** salary;
* handles possible errors (missing file, invalid data format).

### File format

```text
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
```

### Usage example

```python
total, average = total_salary("salary.txt")
print(f"Total salary: {total}, Average salary: {average}")
```

---

## 🐱 Task 2 — Cats Information

### Description

Implemented the `get_cats_info(path)` function which:

* reads a file containing cats data;
* returns a list of dictionaries with keys `id`, `name`, `age`;
* uses `with` and `split(',')`;
* handles file reading errors.

### File format

```text
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
```

### Example result

```python
[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"}
]
```

---

## 📂 Task 3 — Directory Structure Visualization

### Description

A CLI script that:

* accepts a directory path as a command-line argument;
* recursively displays the directory structure;
* uses **colorama** for colored output;
* handles errors (path does not exist or is not a directory).

### Install dependencies

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
pip install colorama
```

### Run

```bash
python task_3_directory_tree.py /path/to/directory
```

---

## 🤖 Task 4 — Console Assistant Bot

### Description

Implemented a CLI assistant bot which:

* runs in an infinite loop waiting for user commands;
* is case-insensitive;
* uses a command parser;
* stores contacts in a dictionary;
* exits on `exit` or `close` commands.

### Supported commands

| Command             | Description         |
| ------------------- | ------------------- |
| `hello`             | Greeting            |
| `add name phone`    | Add a contact       |
| `change name phone` | Update phone number |
| `phone name`        | Show phone number   |
| `all`               | Show all contacts   |
| `exit`, `close`     | Exit the program    |

### Run

```bash
python task_4_assistant_bot.py
```

---

## ✅ Completed Requirements

* ✔ Usage of `with`
* ✔ Text file processing
* ✔ Exception handling
* ✔ CLI interface
* ✔ Virtual environment
* ✔ Clean and structured code

---

## 📌 Author

**Denys**
Homework completed as part of the **GoIT Python Core** course
