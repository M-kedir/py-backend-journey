# Task CLI (Python + SQLite)

A simple command-line task manager built with Python and SQLite.

This project is part of a backend learning journey focused on real-world fundamentals: clean structure, data persistence, and command-based workflows.

## Features

- Add a task from the terminal
- List all saved tasks
- Persist tasks in SQLite (`tasks.db`)
- Auto-create database table on startup

## Tech Stack

- Python 3.x
- SQLite (built into Python via `sqlite3`)
- Standard library only (`argparse`, `pathlib`, `sqlite3`)

## Project Structure

```text
py-backend-journey/
├─ task_cli/
│  ├─ __init__.py
│  ├─ main.py      # CLI commands (add, list)
│  ├─ db.py        # DB connection + schema initialization
│  └─ models.py    # Data model definitions
├─ tasks.db        # Created automatically after first run
└─ README.md
```

## Getting Started

### 1) Create and activate a virtual environment

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Run the application

From the project root:

```powershell
python -m task_cli.main -h
```

## Available Commands

### Add a task

```powershell
python -m task_cli.main add "Learn Python basics"
```

### List tasks

```powershell
python -m task_cli.main list
```

### Command help

```powershell
python -m task_cli.main -h
python -m task_cli.main add -h
python -m task_cli.main list -h
```

## Example Session

```powershell
python -m task_cli.main add "Learn Python basics"
python -m task_cli.main add "Build CLI backend project"
python -m task_cli.main list
```

Sample output:

```text
Task added successfully.
Task added successfully.
[1] Learn Python basics - todo
[2] Build CLI backend project - todo
```

## How It Works

- `main.py` parses terminal commands and routes them to functions.
- `init_db()` ensures the `tasks` table exists before command execution.
- `add` inserts a new row into SQLite.
- `list` reads and prints tasks ordered by creation id.

## Troubleshooting

- **No tasks shown:** Run `add` first, then `list`.
- **Import/module errors:** Make sure you run commands from the project root.
- **PowerShell script policy error on venv activation:** run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then restart PowerShell and activate again.

## Next Improvements

- Update task title/status
- Delete tasks
- Status validation (`todo`, `in_progress`, `done`)
- Unit tests with `pytest`
- Better output formatting (table style)
