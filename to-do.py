class TodoListManager:
    def __init__(self):
        self.todo_list = []

    def display_menu(self):
        print("Menu - To-do list:")
        print("1. View to-do list")
        print("2. Add task to the list")
        print("3. Remove task from the list")
        print("4. Exit")
        print()

    def view_list(self):
        print("To-do list:")
        if not self.todo_list:
            print("No tasks on the list.")
        else:
            for index, task in enumerate(self.todo_list, start=1):
                print(str(index) + ". " + task)
        print()

    def add_task(self):
        task = str(input("Add here the new task:"))
        self.todo_list.append(task)
        print("Task '" + task + "' added successfully.")
        print()

    def remove_task(self):
        if not self.todo_list:
            print("No tasks on the list.")
            return

        task_index = int(input("Enter the number of the task to be removed:")) - 1
        if 0 <= task_index < len(self.todo_list):
            removed_task = self.todo_list.pop(task_index)
            print("Task '" + removed_task + "' removed successfully.")
        else:
            print("Invalid task number.")
        print()

    def run(self):
        sair_programa = False
        while not sair_programa:
            self.display_menu()
            choice = str(input("Choose your option (1-4): "))
            if choice == "1":
                self.view_list()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.remove_task()
            elif choice == "4":
                print("Exiting the program.")
                sair_programa = True
            else:
                print("Invalid option. Please try again.")
            print()


if __name__ == '__main__':
    manager = TodoListManager()
    manager.run()
