from ...model import Task
from ...util import jsonify
from ...schema.apiv1 import TaskSchema
from ...anakonda import db

class TaskController:
    def get_tasks():
        tasks_schema = TaskSchema(many=True)
        tasks = Task.query.all()
        return jsonify(state=tasks_schema.dump(tasks))

    def get_task(task_id):
        return jsonify(status=501, code=101)

    def create_task():
        return jsonify(status=501, code=101)

    def update_task(task_id):
        return jsonify(status=501, code=101)

    def delete_task(task_id):
        return jsonify(status=501, code=101)
