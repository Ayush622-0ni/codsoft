from tkinter import *

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, END)

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except:
        pass

def mark_complete():
    try:
        selected = listbox.curselection()[0]
        task = tasks[selected]
        if not task.startswith("✔️ "):
            tasks[selected] = "✔️ " + task
        update_listbox()
    except:
        pass

def update_listbox():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)

# GUI setup
root = Tk()
root.title("To-Do List")
root['bg']='light blue'

entry = Entry(root, width=30)
entry.pack(pady=10)


Button(root, text="Add Task",bg='pink', width=15, command=add_task).pack(pady=5)
Button(root, text="Delete Task",bg='pink', width=15, command=delete_task).pack(pady=5)
Button(root, text="Mark Complete",bg='pink', width=15, command=mark_complete).pack(pady=5)

listbox = Listbox(root, width=40)
listbox.pack(pady=10)

root.mainloop()
