import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List Application')

        self.tasks = {}

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        add_task_button = tk.Button(root, text='Add Task', command=self.add_task)
        add_task_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=60, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        view_task_button = tk.Button(root, text='View Tasks', command=self.view_tasks)
        view_task_button.grid(row=2, column=0, padx=10, pady=10)

        complete_task_button = tk.Button(root, text='Complete Task', command=self.complete_task)
        complete_task_button.grid(row=2, column=1, padx=10, pady=10)

        delete_task_button = tk.Button(root, text='Delete Task', command=self.delete_task)
        delete_task_button.grid(row=3, column=0, padx=10, pady=10)

        exit_button = tk.Button(root, text='Exit', command=root.quit)
        exit_button.grid(row=3, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            task_id = len(self.tasks) + 1
            self.tasks[task_id] = {'task': task, 'completed': False}
            self.task_listbox.insert(tk.END, f'{task_id}: {task}')
            self.task_entry.delete(0, tk.END)
            messagebox.showinfo('Task Added', f'Task "{task}" added with ID: {task_id}')
        else:
            messagebox.showwarning('Empty Task', 'Please enter a task.')

    def view_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task_id, task_info in self.tasks.items():
            status = 'Completed' if task_info['completed'] else 'Pending'
            self.task_listbox.insert(tk.END, f'{task_id}: {task_info["task"]} - {status}')

    def complete_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task_id = int(self.task_listbox.get(selected_task)[0].split(':')[0])
            self.tasks[task_id]['completed'] = True
            messagebox.showinfo('Task Completed', f'Task ID {task_id} marked as completed.')
            self.view_tasks()
        else:
            messagebox.showwarning('No Task Selected', 'Please select a task from the list.')

    def delete_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task_id = int(self.task_listbox.get(selected_task)[0].split(':')[0])
            del self.tasks[task_id]
            messagebox.showinfo('Task Deleted', f'Task ID {task_id} deleted.')
            self.view_tasks()
        else:
            messagebox.showwarning('No Task Selected', 'Please select a task from the list.')

if __name__ == '__main__':
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
