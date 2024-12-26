from odoo import models, fields

class Service(models.Model):
    _name = 'service.service'
    _description = 'Service'

    name = fields.Char(string='Service Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price', required=True)
    category_id = fields.Many2one(
        'service.category',
        string='Category',
        ondelete='cascade'
    )
