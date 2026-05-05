import argparse
from task_cli.db import get_connection, init_db

def add_task(title: str) -> None: 
    with get_connection() as conn:
        conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        print("Task added successfully.")


def list_tasks() -> None:
    with get_connection() as conn:
        rows = conn.execute("SELECT id, title, status FROM tasks ORDER BY id").fetchall()

        if not rows:
            print("No tasks found.")
            return

        for row in rows:
            print(f"[{row['id']}] {row['title']} - {row['status']}")

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="task-cli", description="Simple task manager CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="Task title")
    subparsers.add_parser("list", help="List all tasks")
    return parser

def main() -> None:
    init_db()
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title)
    elif args.command == "list":
        list_tasks()
    
if __name__ == "__main__":
    main()
        