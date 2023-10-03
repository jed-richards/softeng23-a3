from pathlib import Path
import os

class TaskException(Exception):
    pass

class Project(object):
    def __init__(self, name):
        self.name = name
        
        projdir = Path.cwd() / '.projects'
        if not projdir.exists():
            projdir.mkdir()

        self.filepath =  projdir / (self.name + '.txt')
        if not self.filepath.exists():
            self.filepath.touch()

    def delete(self):
        projdir = Path.cwd() / '.projects'
        self.filepath =  projdir / (self.name + '.txt')
        self.filepath.unlink()

    def add_task(self, task_name):
        tasks = self.get_tasks()
        if task_name in tasks:
            raise TaskException('Task "{}" already exists.'.format(task_name))

        with open(str(self.filepath), 'a') as wf:
            wf.write(task_name + '\n')

    def remove_task(self, task_name):
        tasks = self.get_tasks()
        if task_name not in tasks:
            raise TaskException('Task "{}" does not exist.'.format(task_name))
        else:
            tasks.remove(task_name)

        with open(str(self.filepath), 'w') as wf:
            for task in tasks:
                wf.write(task + '\n')

    def get_tasks(self):
        tasks = []
        with open(str(self.filepath), 'r') as rf:
            for line in rf:
                tasks.append(line.rstrip())
        return tasks


