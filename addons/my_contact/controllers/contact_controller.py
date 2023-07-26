from odoo import http
from odoo.http import request
from odoo.addons.my_contact.models.mycontact import NewContact
import json

class ContactApi(http.Controller):

    @http.route('/mycontactAPI', auth='public')
    def bar_handler(self):
        return json.dumps({
            "content": "Welcome to my contact API!"
        })

    @http.route('/contacts', auth='user', type='json', methods=['POST'])
    def create_contact(self, **post):
        contact = NewContact.create(post)
        return {'id': contact.id}

    @http.route('/contacts/<int:contact_id>', auth='user', type='json', methods=['GET'])
    def read_contact(self, contact_id, **kw):
        contact = NewContact.browse(contact_id)
        return {
            'id': contact.id,
            'first_name': contact.first_name,
            'last_name': contact.last_name,
            'date_of_birth': contact.date_of_birth,
            'mobile': contact.mobile,
            'nickname': contact.nickname,
            'email': contact.email,
            'image': contact.image,
        }

    @http.route('/contacts/<int:contact_id>', auth='user', type='json', methods=['PUT'])
    def update_contact(self, contact_id, **post):
        contact = NewContact.browse(contact_id)
        contact.write(post)
        return {'message': 'Contact updated successfully'}

    @http.route('/contacts/<int:contact_id>', auth='user', type='json', methods=['DELETE'])
    def delete_contact(self, contact_id, **kw):
        contact = NewContact.browse(contact_id)
        contact.unlink()
        return {'message': 'Contact deleted successfully'}
