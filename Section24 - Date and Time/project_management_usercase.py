# Project Management Usercase

from datetime import *

class Project:
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.task = []

    def add_task(self, task):
        self.task.append(task)


# A project can have multiple tasks
class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.resource = []

    def add_resource(self, resource):
        self.resource.append(resource)


# Resource personnel who's going to work on the task
class Resource:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill


project = Project('Artificial Intelligence', date(2022, 1, 1), date(2022, 12, 1))
task = Task('Create Bot', 90)
resource = Resource('John', 'Python')

task.add_resource(resource)
project.add_task(task)

for each_task in project.task:
    print(each_task.name)
    for each_resource in each_task.resource:
        print(resource.name)
        print(resource.skill)
