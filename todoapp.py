import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List App")

        self.tasks = []

        self.task_entry = tk.Entry(master)
        self.task_entry.pack(padx=10, pady=5, fill=tk.X)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(master)
        self.task_listbox.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
