from  odoo import models, fields

class sendStudentEmail(models.TransientModel):
    _name = "send.student.email"
    _description = "Send Student Email"


    email_form = fields.Char(string="Email form")
    email_to = fields.Char(string="Email to")
    email_subject = fields.Char(string ="Email subject")
    email_body = fields.Text(string="Email body")
    
