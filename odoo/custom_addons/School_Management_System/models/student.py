from odoo import models, fields,api 
from odoo.http  import request
from odoo.exceptions import ValidationError


class StudentManagement(models.Model):
    _name = "student.management"
    _description = "Student information"

    name = fields.Char(string="Name", required=True)
    student_id = fields.Char(string="Student ID", required=True)
    image = fields.Binary(string="Image")
    student_image = fields.Image("Student Image")
    dob = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age")
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female")],
        string="Gender"
    )
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    address = fields.Text(string="Address")
    guardian_name = fields.Char(string="Guardian Name")
    guardian_phone = fields.Char(string="Guardian Phone")
    admission_date = fields.Date(string="Admission Date")

    def print_something(self):
        print("The button got clicked")

    def show_rainbow(self):
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'This is a rainbow effect!',
                'img_url':'/web/static/src/img/smile.png',
                'type': 'rainbow_man',
            }
        }

    def send_email(self):
        action_ref = self.env.ref(
            "School_Management_System.send_student_action"
        )
        return action_ref.read()[0]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            student_id = vals.get("student_id")

            if student_id and self.search_count([
                ("student_id", "=", student_id)
            ]):
                raise ValidationError(
                    "Student ID already exists. Please use a different ID."
                )

        return super().create(vals_list)


   