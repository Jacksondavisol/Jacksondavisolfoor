import os
import random
import datetime

verbs = ["Fix", "Add", "Improve", "Update", "Refactor", "Remove"]
objects = ["logging", "token logic", "retry flow", "GitHub sync", "commit tracker"]

def generate_commit_message():
    return f"{random.choice(verbs)} {random.choice(objects)}"

def write_log_entry():
    timestamp = datetime.datetime.now().isoformat()
    message = generate_commit_message()
    with open("log.txt", "a") as f:
        f.write(f"[AUTO LOG] {timestamp} {message}\n")

if __name__ == "__main__":
    write_log_entry()
    print("Log entry created.")
