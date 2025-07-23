# Advanced Zoo Management System

This is a modular, testable, and extensible Zoo Management System built in Python using Object-Oriented Programming principles.

## 🚀 Features

* Add, remove, find, and list animals (Lions, Elephants, Snakes).
* Save and load animals using JSON or CSV.
* Role-based access control (admin/user roles).
* CLI interface to interact with the zoo.
* Logging system.
* Full test suite using `pytest`.

---

## 🧠 Project Structure

```
Zoo/
├── animals/            # Lion, Elephant, Snake classes
├── zoo/                # Zoo class
├── storage/            # CsvStorage and JsonStorage
├── auth/               # Permissions module
├── cli/                # Command Line Interface
├── logs/               # Logging output
├── tests/              # Unit tests
├── animals.json        # Sample animal data
├── *.csv               # CSV data files
└── README.md
```

---

## 🔧 Installation

```bash
git clone <https://github.com/Callmemahdi/Zoo>
cd Zoo
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt
```

---


## 🔐 Permissions

* Admin: can add, remove, save, and load animals.
* User: can only view animals.

Permissions are controlled via the `auth/permissions.py` module.

---

## ✅ Running Tests

Run all unit tests:

```bash
pytest
```

---

## 🧪 Technologies Used

* Python 3.10+
* Pytest
* Logging
* CSV & JSON

---

## 📂 Example Files

* `animals.json` – Default animal dataset.
* `lions.csv`, `snakes.csv` – Data for specific species.

---

## 👨‍💻 Author

Mahdi Sattarzadeh | Tir 1403
