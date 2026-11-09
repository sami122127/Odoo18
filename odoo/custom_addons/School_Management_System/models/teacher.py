from odoo import models, fields


class TeacherManagement(models.Model):
    _name = "teacher.management"
    _description = "Teacher Information"
    _rec_name = "name"
    _order = "name"

    name = fields.Char(
        string="Teacher Name",
        required=True
    )

    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    subject = fields.Char(string="Subject")
    active = fields.Boolean(
        string="Active",
        default=True
    )