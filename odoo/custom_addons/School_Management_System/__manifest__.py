
{
    "name": "School Management System",
    "summary": "Manage schools, students, and their information",
    "version": "18.0.1.0.0",

    "description": """
        School Management System
        ========================
        Manage school and student records including:
        - School Name
        - School Address
        - Student Name
        - Student ID
        - Date of Birth
        - Gender
        - Email
        - Phone
        - Address
    """,

    "category": "Education",
    "license": "AGPL-3",
    "author": "Sami Tech",
    "website": "https://www.odoo.com",

    "depends": [
        "base",
    ],

    "data": [
        "security/ir.model.access.csv",
        "wizard/wizard.xml",
        "views/student.xml",
        "views/school.xml",
        "views/teacher.xml",
        "views/menus.xml",
       
    ],

    "images": [
         "static/description/icon.png",
    ],

    "installable": True,
    "application": True,
    "auto_install": False,
}
