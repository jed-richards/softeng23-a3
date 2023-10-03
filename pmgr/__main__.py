from sys import argv
from pmgr.project import Project, TaskException


def show(args):
    proj_name = args[0]
    project = Project(proj_name)
    tasks = project.get_tasks()
    for task in tasks:
        print(task)

def add(args):
    proj_name = args[0]
    task_name = args[1]
    project = Project(proj_name)
    project.add_task(task_name)
    

def remove(args):
    proj_name = args[0]
    task_name = args[1]
    project = Project(proj_name)
    project.remove_task(task_name)


commands = ['show', 'add', 'remove']

if len(argv) < 3:
    print("pmgr <command> <args>")
    exit(1)

command = argv[1]

if command in commands:
    try:
        eval(command)(argv[2:])
    except TaskException as e:
        print(e)

