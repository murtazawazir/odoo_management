from odoo import fields, models, api


class Restaurant(models.Model):
    _name = 'rest.staff'
    _description = 'This Model is About Restaurant'
    _rec_name = 'name'
    _order = 'age'

    name = fields.Char(string='Name')
    mobile = fields.Char(string='Mobile')
    email = fields.Char(string='Email')
    age  = fields.Integer(string='Age')
    date  = fields.Date(string='Date')
    country_id = fields.Many2one('res.country',string='Country')
    country_ids = fields.Many2many('res.country',string='Countries')
    country_code = fields.Char(string='Country Code',related='country_id.code')

    staff_line_ids = fields.One2many('rest.staff.line','staff_id')

class RestStaffLine(models.Model):
    _name = 'rest.staff.line'

    staff_id = fields.Many2one('rest.staff')
