from ex1 import BinaryTreePriorityQueue

class ToDoList:
    def __init__(self):
        self.queue = BinaryTreePriorityQueue()

    def add_task(self, task, priority):
        self.queue.insert(task, priority)
        print(f"Task added: '{task}' with priority {priority}")

    def remove_highest_priority_task(self):
        removed = self.queue.pop()
        if removed:
            print(f"Removed task: '{removed.value}' with priority {removed.priority}")
        else:
            print("No tasks to remove.")

    def show_all_tasks(self):
        tasks = self._traverse_all_nodes(self.queue.root)
        if tasks:
            self._insertion_sort(tasks)
            print("All tasks (sorted by priority):")
            for value, priority in tasks:
                print(f"- {value} (priority {priority})")
        else:
            print("No tasks in the queue.")

    def _insertion_sort(self, tasks):
        for i in range(1, len(tasks)):
            key = tasks[i]
            j = i - 1
            while j >= 0 and tasks[j][1] < key[1]:
                tasks[j + 1] = tasks[j]
                j -= 1
            tasks[j + 1] = key

    def _traverse_all_nodes(self, node):
        if not node:
            return []
        return [(node.value, node.priority)] + self._traverse_all_nodes(node.left) + self._traverse_all_nodes(node.right)

    def show_task_by_priority(self, priority):
        task = self._find_task_by_priority(self.queue.root, priority)
        if task:
            print(f"Task with priority {priority}: '{task.value}'")
        else:
            print(f"No task found with priority {priority}")

    def _find_task_by_priority(self, node, priority):
        if not node:
            return None
        if node.priority == priority:
            return node
        left_result = self._find_task_by_priority(node.left, priority)
        if left_result:
            return left_result
        return self._find_task_by_priority(node.right, priority)


if __name__ == "__main__":
    todo = ToDoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("add - Add task")
        print("remove - Remove highest priority task")
        print("show - Show all tasks")
        print("priority - Show task by priority")
        print("exit - Exit")
        choice = input("Print a command : ").lower()

        if choice == "add":
            task = input("Enter task description: ")
            priority = int(input("Enter priority: "))
            todo.add_task(task, priority)
        elif choice == "remove":
            todo.remove_highest_priority_task()
        elif choice == "show":
            todo.show_all_tasks()
        elif choice == "priority":
            priority = int(input("Enter priority for task what you are looking for: "))
            todo.show_task_by_priority(priority)
        elif choice == "exit":
            print("Goodbye")
            break
        else:
            print("Invalid command")
