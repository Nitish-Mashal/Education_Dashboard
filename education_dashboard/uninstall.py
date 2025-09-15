import frappe

def after_uninstall():
    # Delete all Workspaces you added
    workspaces_to_remove = [
        "Education Dashboard",
        "Student Info",
        "Instructor Info",
        "Attendance Student",
        "Student Course",
        "Student Fees",
        "Program Enrollment Student",
        "Academic",
    ]

    for ws in workspaces_to_remove:
        if frappe.db.exists("Workspace", ws):
            frappe.delete_doc("Workspace", ws, force=1, ignore_permissions=True)

    # Delete all Dashboard Charts from Education module
    charts = frappe.get_all("Dashboard Chart", filters={"module": "Education"}, pluck="name")
    for chart in charts:
        frappe.delete_doc("Dashboard Chart", chart, force=1, ignore_permissions=True)

    # (Optional) Delete Number Cards if you add them later
    cards = frappe.get_all("Number Card", filters={"module": "Education"}, pluck="name")
    for card in cards:
        frappe.delete_doc("Number Card", card, force=1, ignore_permissions=True)
