import frappe
import base64
from frappe.utils import now_datetime

@frappe.whitelist()
def get_student_projects(user=None):
    if not user:
        user = frappe.session.user

    user_doc = frappe.get_doc("User", user)
    department = user_doc.get("department")  # correct fieldname

    if not department:
        return []

    projects = frappe.get_all(
        "College Project",
        filters={"department": department, "status": "Published"},
        fields=["name", "project_title", "description", "deadline", "status", "teacher"]
    )

    return projects

@frappe.whitelist()
def project_submissions_report_card():
    """
    Returns data for the dashboard card linking to the report
    """
    return {
        "value": "View",  # Card label, not numeric
        "fieldtype": "Data",
        "route": ["query-report", "Filtered Project Submissions"]  # Link to your report
    }



# @frappe.whitelist(allow_guest=True)
# def get_home_page(login_manager=None):
#     """
#     Redirect students to their website portal after login.
#     """
#     user = frappe.session.user
#     roles = frappe.get_roles(user)

#     if "Student" in roles:
#         # Website redirect — not Desk page
#         frappe.local.response["home_page"] = "/student-projects"
