from odoo import models, fields

class ServiceCategory(models.Model):
    _name = 'service.category'
    _description = 'Service Category'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')
    service_ids = fields.One2many(
        'service.service',
        'category_id',
        string='Services'
    )
