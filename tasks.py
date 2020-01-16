from invoke import Collection, task

from src.main.python.tasks import *

ns = Collection(docker)
# base tasks are in a module. This was the only way I could find
# to add the base tasks at the top level namespace.
# example:
#     invoke test
# instead of:
#     invoke base.test
for (task_name, task) in Collection.from_module(base).tasks.items():
    ns.add_task(task)
