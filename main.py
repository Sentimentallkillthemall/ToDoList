class ToDoList:
    def __init__(self):
        self.list = []

    def add_task(self, task):
        self.list.append(task)

    def delete_task(self, task_index):
        self.list.pop(task_index)

    def show_list(self):
        print(self.list)


Todo = ToDoList()
print(Todo.list)
Todo.add_task(task='Wash the dishes')
Todo.add_task(task='Do homework')
Todo.show_list()
Todo.delete_task(task_index=1)
Todo.show_list()
