from task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)

        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        try:
            current_task = next(filter(lambda t: t.name == task_name, self.tasks))

        except StopIteration:
            return f"Could not find task with the name {task_name}"

        current_task.completed = True

        return f"Completed task {task_name}"

    def clean_section(self):
        counter = 0

        for completed_task in self.tasks:
            if completed_task.completed:
                self.tasks.remove(completed_task)
                counter += 1

            return f"Cleared {counter} tasks."

    def view_section(self):
        output = [f"Section {self.name}:"]

        for task_details in self.tasks:
            output.append(task_details.details())

        return "\n".join(output)


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
