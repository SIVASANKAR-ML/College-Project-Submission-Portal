import frappe


def get_context(context):
    context.page_title = "Student Project Portal"
    projects = frappe.get_all(
        "College Project",
        filters={"status": "Published"},
        fields=["name", "project_title", "description", "deadline", "status", "teacher"]
    )
    context.projects = projects
    return context
