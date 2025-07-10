

## Random Python Practice

A collection of small Python exercises and mini-projects, focusing especially on object-oriented programming (OOP) principles like **encapsulation**, **private attributes**, and **class-based design**.

---

## Project Structure

```text
random-python-practice/
│
├── practice_questions/
│   └── OOP/
│       ├── app/
│       │   ├── abstract_base_device.py
│       │   └── ...
│       ├── tests/
│       │   ├── test_abstract_base_device.py
│       │   └── ...
│       ├── bankaccount_encapsulation.py
│       ├── book_encapsulation.py
│       ├── player_encapsulation.py
│       └── ...
│
├── .github/
│   └── workflows/
│       └── python-lint.yml
│
├── .flake8
├── README.md
├── requirements.txt
└── venv/
```



---

## Local Setup (Linter, Formatter, CI)

This repo uses **PEP8 standards** enforced through:

- `black` (auto code formatter)
- `flake8` (style checker/linter)
- GitHub Actions workflow (CI on push)

###  Setup Instructions

```bash
# Clone the repo and enter the directory
git clone <repo-url>
cd random-python-practice

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install black flake8

# Format and lint code
black .
flake8
```


##  Classes & Examples
## SafeBox
A simple class for storing and verifying a 4-digit code.

```python
sf1 = SafeBox()
sf1.set_code("1234")        # ➜ '1234'
sf1.set_code("123")         # ➜ 'code you entered is less than 4 digits'
sf1.check_code("1234")      # ➜ 'entered real one'
sf1.check_code("0000")      # ➜ 'entered incorrect code'
```

##  Book (Encapsulation)
Demonstrates how a protected attribute can still be modified externally, breaking encapsulation.

```python
b1 = Book("LOTR", 200)
b1._pages = 250             # Not recommended!
print(b1.get_pages())       # ➜ 250
```

## BankAccount (Private Attributes)
Illustrates how private attributes are accessed internally vs externally via name mangling.

```python
account1 = BankAccount("John", 500)
account1.__balance = 400     # Creates new attribute, doesn't affect original
print(account1.get_balance())  # ➜ 500
print(account1._BankAccount__balance)  # ➜ 500 (actual private value)
```

## Player Class
A small simulation of healing and damaging a player using input validation.

```python
p1 = Player()
p1.health_points()     # Prompt user to add HP
p1.damage_points()     # Prompt user to apply damage
```

## Testing
Test files are located in practice_questions/OOP/tests/. Run all tests:

```bash
python -m unittest discover -s practice_questions/OOP/tests
```


## CI/CD Pipeline
This repo uses GitHub Actions to auto-check code on push:

- `black` ensures consistent formatting

- `flake8` checks for `PEP8` violations

No code is allowed into main unless it passes both.
 

## Install formatting and linting tools:

```bash
pip install -r requirements.txt
```



## Pre-commit Hooks

This project uses [pre-commit](https://pre-commit.com/) to automatically run code formatters and linters (like `black` and `flake8`) before each commit.

### How to use

1. Make sure you have your virtual environment activated:
   ```bash
   source venv/bin/activate   # macOS/Linux
   # or
   venv\Scripts\activate      # Windows
   ```

2. Install pre-commit if you haven’t already:
   ```bash 
    pip install pre-commit
   ```

3. Install pre-commit if you haven’t already:
   ```bash 
    pre-commit install
   ```
From now on, whenever you run git commit, pre-commit will automatically
check your code for style and formatting issues and block the 
commit if there are problems to fix.

## Running pre-commit manually

You can also run the hooks against all files manually with:

   ```bash 
    pre-commit run --all-files
   ```



## Notes
- This project is actively being cleaned up and standardized

- Some older files are still being updated for formatting/linting

- New features and refactors coming soon