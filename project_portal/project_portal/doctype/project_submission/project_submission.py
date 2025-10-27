import frappe
from frappe.model.document import Document

class ProjectSubmission(Document):
    def validate(self):
        # Optionally validate before submission
        pass

    # This function is used to notify the assigned teacher when a student submits a project.

    def on_submit(self):
        self.notify_teacher_on_submission()


    # This function is used to notify the student about the final status of their project submission when the document is updated.
    
    def on_update(self):
        
        self.send_final_status_to_student()




    # This function sends an email notification to the assigned teacher when a student submits a project.

    def notify_teacher_on_submission(self):
        if not self.teacher:
            frappe.throw("Assigned Teacher is required before submission.")

        args = {
            "teacher": self.teacher,
            "student_name": self.student_name,
            "project": self.project,
            "department": self.department
        }

        frappe.sendmail(
            recipients=[self.teacher],
            subject=f"New Project Submission: {self.project}",
            template="project_submission_teacher",
            args=args
        )

    # This function sends an email notification to the student about the final status of their project submission.

    def send_final_status_to_student(self):
        args = {
            "project": self.project,
            "status": self.workflow_state,
            "teacher": self.teacher,
        }
        frappe.sendmail(
            recipients=[self.student],
            subject=f"Your project '{self.project}' has been {self.workflow_state.lower()}",
            template="student_final_status",
            args=args
        )
