# -*- coding: utf-8 -*-

from odoo import models, fields


class delivery(models.Model):
    _name = 'sikilat.delivery'
    _description = 'sikilat.delivery'

    customer = fields.Char("Receiver")
    state = fields.Selection(string='Status', selection=[('Draft', 'Draft'), ('Confirm', 'Confirm'), ('Done', 'Done')])
    vehicle_id = fields.Many2one(comodel_name='sikilat.vehicle', string='Vehicle')
    driver_id = fields.Many2one(comodel_name='sikilat.driver', string='driver_id')
    driver_name = fields.Char(related='driver_id.name', string='Driver Name')
    # driver_id = fields.Many2one(comodel_name='sikilat.driver', string='Driver')

# class SikilatDelivery(models.Model):
#     _name = 'sikilat.delivery'
#     _inherit = 'delivery.carrier'

#     delivery_type = fields.Selection(selection_add=[('sikilat_delivery', 'Sikilat Delivery')], ondelete={'sikilat_delivery': 'set default'})
#     driver_id = fields.Many2one(comodel_name='sikilat.driver', string='Driver')


#     """
#      Add your methods:
#        <my_provider>_rate_shipment
#        <my_provider>_send_shipping
#        <my_provider>_get_tracking_link
#        <my_provider>_cancel_shipment
#        _<my_provider>_get_default_custom_package_code
#        """       

#     def sikilat_delivery_rate_shipment(self, order):
#         carrier = self._match_address(order.partner_shipping_id)
#         if not carrier:
#             return {'success': False,
#                     'price': 0.0,
#                     'error_message': 'Error: this delivery method is not available for this address.',
#                     'warning_message': False}
#         price = 200.0
#         company = self.company_id or order.company_id or self.env.company
#         print(f"===============================\n===============================\n{company=}")
#         return {
#             'success': True,
#             'price': price
#         }

#     def sikilat_delivery_send_shipping(self, pickings):
#         res = []
#         fixed_price = 200.0
#         for picking in pickings:
#             res += [{'exact_price': fixed_price,
#                      'tracking_number': False}]
#         return res

#     def sikilat_delivery_get_tracking_link(self, picking):
#         return False

#     def sikilat_delivery_cancel_shipment():
#         raise NotImplementedError()

#     def _sikilat_delivery_get_default_package_code():
#         pass
