from flask import Flask, jsonify, request, render_template
from models import Task, WBSItem, DailyLogItem, RiskItem, ChangeHistoryItem
from models import STATUSES, PRIORITIES, TASK_TYPES, PHASES
from storage import load_tasks, save_tasks, create_task, update_task, delete_task, get_task

app = Flask(__name__)


def _task_to_dict(t: Task) -> dict:
    d = t.to_dict()
    d["total_estimated"] = t.total_estimated
    d["total_actual"] = t.total_actual
    d["status_icon"] = t.status_icon
    d["priority_icon"] = t.priority_icon
    return d


def _dict_to_task(data: dict) -> Task:
    def _parse_list(key, cls):
        items = data.get(key, [])
        return [cls(**item) if isinstance(item, dict) else item for item in items]

    t = Task(
        id=data.get("id", ""),
        title=data.get("title", ""),
        description=data.get("description", ""),
        status=data.get("status", STATUSES[0]),
        priority=data.get("priority", PRIORITIES[2]),
        task_type=data.get("task_type", TASK_TYPES[0]),
        owner=data.get("owner", ""),
        requester=data.get("requester", ""),
        start_date=data.get("start_date", ""),
        due_date=data.get("due_date", ""),
        core_objective=data.get("core_objective", ""),
        deliverables=data.get("deliverables", []),
        success_criteria=data.get("success_criteria", []),
        wbs_items=_parse_list("wbs_items", WBSItem),
        risks=[RiskItem(**r) if isinstance(r, dict) else r for r in data.get("risks", [])],
        external_dependencies=data.get("external_dependencies", []),
        buffer_hours=float(data.get("buffer_hours", 0)),
        daily_logs=_parse_list("daily_logs", DailyLogItem),
        resources=data.get("resources", []),
        change_history=[ChangeHistoryItem(**h) if isinstance(h, dict) else h for h in data.get("change_history", [])],
        tags=data.get("tags", []),
        created_at=data.get("created_at", ""),
        updated_at=data.get("updated_at", ""),
    )
    return t


@app.route("/")
def index():
    return render_template("index.html",
                           statuses=STATUSES,
                           status_icons=["🟩", "🟨", "🟦", "⬜", "❌"],
                           priorities=PRIORITIES,
                           task_types=TASK_TYPES,
                           phases=PHASES)


@app.route("/api/tasks", methods=["GET"])
def api_list_tasks():
    tasks = load_tasks()
    return jsonify([_task_to_dict(t) for t in tasks])


@app.route("/api/tasks", methods=["POST"])
def api_create_task():
    data = request.get_json(force=True)
    task = _dict_to_task(data)
    created = create_task(task)
    return jsonify(_task_to_dict(created)), 201


@app.route("/api/tasks/<task_id>", methods=["GET"])
def api_get_task(task_id):
    task = get_task(task_id)
    if not task:
        return jsonify({"error": "not found"}), 404
    return jsonify(_task_to_dict(task))


@app.route("/api/tasks/<task_id>", methods=["PUT"])
def api_update_task(task_id):
    task = get_task(task_id)
    if not task:
        return jsonify({"error": "not found"}), 404
    data = request.get_json(force=True)
    data["id"] = task_id
    updated = _dict_to_task(data)
    result = update_task(updated)
    if not result:
        return jsonify({"error": "update failed"}), 500
    return jsonify(_task_to_dict(result))


@app.route("/api/tasks/<task_id>", methods=["DELETE"])
def api_delete_task(task_id):
    ok = delete_task(task_id)
    if not ok:
        return jsonify({"error": "not found"}), 404
    return jsonify({"ok": True})
