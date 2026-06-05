# PlacementMCKV

PlacementMCKV is a role-based Placement Management System built using Django and MySQL. The platform helps manage campus recruitment activities by connecting students, recruiters, and administrators through a centralized portal.

Students can create profiles, upload resumes, browse jobs, and track applications. Recruiters can manage companies, post jobs, review applicants, and update application statuses. Administrators can monitor overall placement activity through dedicated dashboards.

---

## Features

### Student

- Student registration and login
- Profile management
- Resume upload
- GitHub and LinkedIn profile links
- Browse available jobs
- Apply for jobs
- Track application status

### Recruiter

- Recruiter registration and login
- Create and manage companies
- Create and manage job postings
- Review applicants
- View student profiles and resumes
- Update application status

### Admin

- System monitoring dashboard
- Placement statistics overview
- Manage platform data through Django Admin

---

## Tech Stack

| Technology | Usage |
|------------|-------|
| Python 3.11 | Backend Language |
| Django 5 | Web Framework |
| MySQL | Database |
| Bootstrap 5 | Frontend Styling |
| Django Templates | UI Rendering |

---

## User Roles

### Student Workflow

```text
Register
↓
Create Profile
↓
Upload Resume
↓
Browse Jobs
↓
Apply
↓
Track Status
```

### Recruiter Workflow

```text
Register
↓
Create Company
↓
Post Job
↓
Review Applicants
↓
Shortlist / Interview / Select / Reject
```

### Admin Workflow

```text
Monitor Students
Monitor Recruiters
Monitor Jobs
Monitor Applications
```

---

## Project Structure

```text
placement_management/
├── accounts/
├── applications/
├── companies/
├── config/
├── dashboard/
├── jobs/
├── recruiters/
├── students/
├── templates/
├── static/
├── media/
├── .env
├── .env.example
├── manage.py
├── requirements.txt
└── README.md
```

---

## Current Features

- Custom User Model
- Role-Based Authentication
- Student Registration
- Recruiter Registration
- Student Dashboard
- Recruiter Dashboard
- Admin Dashboard
- Company Management (CRUD)
- Job Management (CRUD)
- Job Application Tracking
- Resume Upload and Download
- Candidate Review Workflow
- MySQL Database Integration

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/placement_management.git
cd placement_management
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file using `.env.example` and update the database credentials.

### Run Migrations

```bash
python manage.py migrate
```

### Create Admin User

```bash
python manage.py createsuperuser
```

### Start Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

## Future Improvements

- Job Search and Filters
- Email Notifications
- Placement Analytics Charts
- Interview Scheduling
- Cloud Deployment

---

## Author

**Sahil Sah**

GitHub: https://github.com/sahil3028