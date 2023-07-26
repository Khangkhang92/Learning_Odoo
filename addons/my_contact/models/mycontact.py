from odoo import models, fields

class NewContact(models.Model):
    _name = 'my_contact_module.contact'
    _description = 'Contact Management'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    mobile = fields.Char(string='Mobile', required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    nickname = fields.Char('Nickname')
    email = fields.Char('Email')
    image = fields.Binary("Image", attachment=True, help="Image") 