from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    pre_invoice_number = fields.Char(string="Pre-Factura No.", readonly=True, copy=False)

    @api.model
    def create(self, vals):
        if vals.get('move_type') in ['out_invoice', 'in_invoice'] and not vals.get('pre_invoice_number'):
            vals['pre_invoice_number'] = self.env['ir.sequence'].next_by_code('pre.invoice')
        return super(AccountMove, self).create(vals)

    def action_post(self):
        for move in self:
            if move.pre_invoice_number:
                move.pre_invoice_number = False  # Comenta esta línea si quieres conservar el número
        return super(AccountMove, self).action_post()
