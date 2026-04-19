#!/usr/bin/env python3
import json
import os
import sys

DATA_FILE = os.path.join(os.path.dirname(__file__), "todos.json")


def load_todos():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as f:
        return json.load(f)


def save_todos(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2)


def add(title):
    todos = load_todos()
    todos.append({"id": len(todos) + 1, "title": title, "done": False})
    save_todos(todos)
    print(f"Added: {title}")


def list_todos():
    todos = load_todos()
    if not todos:
        print("No todos yet.")
        return
    for t in todos:
        status = "x" if t["done"] else " "
        print(f"  [{status}] {t['id']}. {t['title']}")


def complete(todo_id):
    todos = load_todos()
    for t in todos:
        if t["id"] == todo_id:
            t["done"] = True
            save_todos(todos)
            print(f"Completed: {t['title']}")
            return
    print(f"No todo with id {todo_id}")


def delete(todo_id):
    todos = load_todos()
    remaining = [t for t in todos if t["id"] != todo_id]
    if len(remaining) == len(todos):
        print(f"No todo with id {todo_id}")
        return
    save_todos(remaining)
    print(f"Deleted todo {todo_id}")


USAGE = """Usage:
  python todo.py add <title>       Add a new todo
  python todo.py list              List all todos
  python todo.py complete <id>     Mark a todo as done
  python todo.py delete <id>       Delete a todo
"""


def main():
    args = sys.argv[1:]
    if not args:
        print(USAGE)
        return

    cmd = args[0]
    if cmd == "add" and len(args) >= 2:
        add(" ".join(args[1:]))
    elif cmd == "list":
        list_todos()
    elif cmd == "complete" and len(args) == 2:
        complete(int(args[1]))
    elif cmd == "delete" and len(args) == 2:
        delete(int(args[1]))
    else:
        print(USAGE)


if __name__ == "__main__":
    main()
