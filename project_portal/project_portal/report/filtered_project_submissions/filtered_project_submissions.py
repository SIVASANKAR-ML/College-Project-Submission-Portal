# Copyright (c) 2025, siva and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters: dict | None = None):
    """Return columns and data for the report."""
    if filters is None:
        filters = {}

    # -------------------------
    # Define columns
    # -------------------------
    columns = [
        {"label": _("ID"), "fieldname": "name", "fieldtype": "Link", "options": "Project Submission"},
        {"label": _("Student Name"), "fieldname": "student_name", "fieldtype": "Data"},
        {"label": _("Project"), "fieldname": "project", "fieldtype": "Link", "options": "College Project"},
        {"label": _("Department"), "fieldname": "department", "fieldtype": "Link", "options": "College Department"},
        {"label": _("Submission File"), "fieldname": "file_upload", "fieldtype": "Data"},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data"}
    ]

    # -------------------------
    # Build conditions based on filters
    # -------------------------
    conditions = []
    if filters.get("department"):
        conditions.append(f"department='{filters['department']}'")
    if filters.get("status"):
        conditions.append(f"status='{filters['status']}'")
    if filters.get("student"):
        conditions.append(f"student='{filters['student']}'")

    where_clause = " and ".join(conditions) if conditions else "1=1"

    # -------------------------
    # Fetch data from Project Submission
    # -------------------------
    data = frappe.db.sql(f"""
        SELECT
            name,
            student_name,
            project,
            department,
            file_upload,
            status
        FROM `tabProject Submission`
        WHERE {where_clause}
        ORDER BY name DESC
    """, as_dict=1)

    return columns, data
