# -*- coding: utf-8 -*-

from odoo import fields, models


# class SikilatDriver(models.Model):
#     _inherit = 'res.partner'

#     is_driver = fields.Boolean("Is Driver")
#     driver_license_type = fields.Selection(string='Driver License Type', selection=[('SIM A', 'SIM A'), 
#                                                                                     ('SIM B1', 'SIM B1'),
#                                                                                     ('SIM B2', 'SIM B2'),
#                                                                                     ('SIM C', 'SIM C'),
#                                                                                     ('SIM D', 'SIM D')])
#     driver_license_expiry_date = fields.Date("Driver License Expiry Date")
#     # vehicle_id = fields.Many2one(comodel_name='sikilat.vehicle', string='Vehicle')
    

class SikilatDriver(models.Model):
    _name = 'sikilat.driver'
    _description = 'sikilat driver data'

    name = fields.Char('name')
    driver_license_type = fields.Selection(string='Driver License Type', selection=[('SIM A', 'SIM A'), 
                                                                                    ('SIM B1', 'SIM B1'),
                                                                                    ('SIM B2', 'SIM B2'),
                                                                                    ('SIM C', 'SIM C'),
                                                                                    ('SIM D', 'SIM D')])
    driver_license_expiry_date = fields.Date("Driver License Expiry Date")
    partner_id = fields.Many2one('res.partner', string='partner')
    