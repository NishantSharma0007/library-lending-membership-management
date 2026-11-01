# Library Lending & Membership Management Backend

## Project Overview

The **Library Lending & Membership Management Backend** is a Python command-line application developed as part of Module 8 – Object-Oriented Programming.

This project manages library items, member accounts, borrowing operations, returns, due dates, and overdue fines using Object-Oriented Programming (OOP) concepts.

It uses JSON for data storage so that library records remain available even after restarting the program.

## Features

- Register books, magazines, and reference books.
- Register student and faculty members.
- Support research student membership.
- Borrow and return library items.
- Check item availability before checkout.
- Apply different borrowing periods using polymorphism.
- Calculate overdue days and fines.
- Prevent duplicate item and member IDs.
- Maintain active loan records.
- Save and restore records using JSON.
- Display library reports.
- Demonstrate multiple inheritance using NotificationMixin.

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- ABC (Abstract Base Classes)
- Datetime
- OS / Pathlib

**External Packages:** None. Only Python standard library modules are used.

## OOP Concepts Implemented

1. Classes and Objects
2. Constructors (`__init__()`)
3. `self` keyword
4. Instance and Class Attributes
5. Instance, Class, and Static Methods
6. Encapsulation
7. Inheritance
8. Single Inheritance
9. Multilevel Inheritance
10. Multiple Inheritance
11. Hierarchical Inheritance
12. Method Overriding
13. `super()` Keyword
14. Polymorphism
15. Abstraction
16. Abstract Base Classes (`ABC`)
17. Abstract Methods

## Class Architecture

### Library Items

- `LibraryItem` – Abstract base class.
- `Book` – Inherits from LibraryItem.
- `Magazine` – Inherits from LibraryItem.
- `ReferenceBook` – Applies non-lendable or zero-day borrowing rules.

### Members

- `Member` – Base member class.
- `StudentMember` – Student membership.
- `ResearchStudent` – Extends StudentMember.
- `FacultyMember` – Faculty membership.
- `NotificationMixin` – Provides notification functionality.
- `NotifiedMember` – Demonstrates multiple inheritance.

### Library Management

`LibraryManager` manages the catalogue, members, and active loans.

## Project Structure

```text
library_backend/
│
├── main.py
├── models.py
├── library_service.py
├── storage.py
├── data.json
└── README.md
```

## Required Python Modules

| Module | Purpose |
|---|---|
| abc | Abstract classes and methods |
| datetime | Issue dates, due dates, and fines |
| json | Saving and loading library records |
| os / pathlib | File path handling |

## How to Run the Project

**Step 1:** Clone the repository.

```bash
git clone YOUR_REPOSITORY_URL
```

**Step 2:** Open the project folder.

```bash
cd library-lending-membership-management
```

**Step 3:** Run the application.

```bash
python main.py
```

## Sample Terminal Interaction

```text
1. Register book
2. Register member
3. Borrow item
4. Return item
5. View reports
6. Exit

Choice: 3

Member ID: M101
Item ID: B201

Borrow successful: B201 issued to M101

Due date: 2026-11-10

Choice: 5

Active loans: 1
B201 | M101 | Due: 2026-11-10
```

*Sample dates and IDs are illustrative. Actual due dates are calculated using the current date and the item's borrowing period.*

## Reports

The application provides reports for:

- All registered library items.
- Available library items.
- Active loans.
- Overdue loans.
- Members and their current borrowed-item counts.

## Data Persistence

The project uses JSON serialization and deserialization to save and restore library items, members, and loan records.

This ensures that data remains available across program restarts.

## Learning Outcomes

By completing this project, we learn how to:

1. Design a clean OOP-based application.
2. Create reusable classes and objects.
3. Implement different types of inheritance.
4. Apply encapsulation and abstraction.
5. Use polymorphism and method overriding.
6. Manage borrowing and returning operations.
7. Calculate overdue fines using dates.
8. Store and restore application data using JSON.

## Author

Developed as part of **Python Technical Training – Module 8: Object-Oriented Programming**.

**Project:** Library Lending & Membership Management Backend  
**Language:** Python  
**Difficulty:** Intermediate to Advanced  
**Application Type:** Command-Line Backend