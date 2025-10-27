# 🏫 College Project Submission Portal

A **Frappe-based web app** for managing project submissions in colleges.  
Teachers can publish projects, students can submit work, and approvals flow through **Teacher → Project Head → HOD**, with automatic email updates at every stage.

---

## 🚀 Features

### 👩‍🏫 Teachers
- Create projects with title, department, and deadlines.  
- Get email alerts for new submissions.  
- Approve/reject projects from the dashboard.  
- View reports and print acknowledgments.  

### 🎓 Students
- View department-specific projects.  
- Submit work with attachments.  
- Track project status and download acknowledgments.  

### 🧑‍💼 Project Head & HOD
- Multi-level approval workflow.  
- Department dashboards and status tracking.  

### 📊 Reports
- Filter by department, status, or student.  
- Quick summary of pending and approved projects.  
- Print or export reports.

---

## 🛠️ Installation

Install using [Frappe Bench](https://github.com/frappe/bench):

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/SIVASANKAR-ML/College-Project-Submission-Portal.git --branch main
bench install-app project_portal

