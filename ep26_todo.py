# Episode 26: Project: to-do manager
# Step By Step Coding · Python basics
#
# Try it: Add add_task("your own task") and press Run
# Then: Add complete(0) before the loop and press Run
# ---------------------------------------------

todos = []
def add_task(title):
    task = {"title": title, "done": False}
    todos.append(task)
add_task("Buy milk")
add_task("Write script")
add_task("Record episode")
def complete(index):
    todos[index]["done"] = True
complete(1)
for i, t in enumerate(todos):
    mark = "x" if t["done"] else " "
    print(f"{i + 1}. [{mark}] {t['title']}")
done = len([t for t in todos if t["done"]])
print(f"{done} of {len(todos)} done")
