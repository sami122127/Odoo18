from odoo import models, fields

class SchoolManagementSystem(models.Model):
    _name = 'school.management.system'
    _description = 'School Management System'

    name = fields.Char(string='School Name', required=True)
    address = fields.Text(string='Address')