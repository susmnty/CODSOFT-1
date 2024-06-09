import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry_task.get()
    if task:
        task_id = len(tasks) + 1
        tasks.append({'id': task_id, 'task': task, 'status': 'pending'})
        list_tasks()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def update_task():
    task_id = int(entry_task_id.get())
    new_task = entry_task.get()
    for task in tasks:
        if task['id'] == task_id:
            task['task'] = new_task
            list_tasks()
            entry_task.delete(0, tk.END)
            entry_task_id.delete(0, tk.END)
            return
    messagebox.showerror("Update Error", "No task found with the given ID.")

def delete_task():
    task_id = int(entry_task_id.get())
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    list_tasks()
    entry_task_id.delete(0, tk.END)

def list_tasks():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, f"ID: {task['id']}, Task: {task['task']}, Status: {task['status']}")

root = tk.Tk()
root.title("To-Do List Application")

frame = tk.Frame(root)
frame.pack(pady=10)

entry_task = tk.Entry(frame, width=50)
entry_task.pack(side=tk.LEFT, padx=10)

btn_add_task = tk.Button(frame, text="Add Task", command=add_task)
btn_add_task.pack(side=tk.LEFT)

frame_update = tk.Frame(root)
frame_update.pack(pady=10)

entry_task_id = tk.Entry(frame_update, width=5)
entry_task_id.pack(side=tk.LEFT, padx=10)

btn_update_task = tk.Button(frame_update, text="Update Task", command=update_task)
btn_update_task.pack(side=tk.LEFT)

btn_delete_task = tk.Button(frame_update, text="Delete Task", command=delete_task)
btn_delete_task.pack(side=tk.LEFT)

listbox_tasks = tk.Listbox(root, width=75, height=15)
listbox_tasks.pack(pady=10)

root.mainloop()
