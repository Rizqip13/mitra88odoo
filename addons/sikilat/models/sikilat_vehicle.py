# -*- coding: utf-8 -*-

from odoo import fields, models


class SikilatVehicle(models.Model):
    _name = 'sikilat.vehicle'
    _description = 'Master table of sikilat delivery vehicle'

    description = fields.Text("Vehicle Description")
    number_plate = fields.Char(string="Vehicle Number Plate")
    is_active = fields.Boolean("Active", default=True)
