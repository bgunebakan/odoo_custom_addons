# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import datetime

from odoo import models, fields, api, _


class ProcurementTender(models.Model):
    _name = 'procurement.tender'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Tender Record'
    # _rec_name = 'tender_name no'

    name = fields.Char(string="Name")

    # no = fields.Char(string="No")
    no = fields.Char(string='No', required=True, copy=False, readonly=False,
                     index=True, default=lambda self: _('New'))

    type_id = fields.Many2one(
        'procurement.tendertype', string='Type', readonly=False,
        index=True, tracking=1, required=True)

    status_id = fields.Many2one(
        'procurement.tenderstatus', string='Status', readonly=False,
        index=True, tracking=1, required=True)

    apply_date = fields.Date(string='Apply Date', readonly=False,
                             help="Date on which tender is applied.")

    fiscal_year = fields.Selection([(str(num), str(num)) for num in
                                    range((datetime.datetime.now().year - 5), ((datetime.datetime.now().year) + 1))],
                                   default=str(datetime.datetime.now().year)
                                   )
    responsible_staff = fields.Char(string="Responsible Staff")

    employee_id = fields.Many2one(
        'hr.employee', string='Personnel in charge', readonly=False,
        index=True, tracking=1)

    supplier_id = fields.Many2one(
        'res.partner', string='Supplier', readonly=False,
        index=True, tracking=1)

    auction_no = fields.Char(string="Auction No")

    auction_datetime = fields.Datetime(string='Auction Date', readonly=False,
                                       help="Date of Auction")

    auction_price = fields.Float(string="Auction Price")

    currency_id = fields.Many2one(
        'res.currency', string='Currency', readonly=False,
        index=True, tracking=1)

    auction_location = fields.Char(string="Auction Location")

    supplier_type_id = fields.Many2one(
        'procurement.suppliertype', string='Suplier Type', readonly=False,
        index=True, tracking=1)

    contract_date = fields.Date(string='Contract Date', readonly=False,
                                help="Date of Contract")

    file_lines = fields.One2many('procurement.tender.files', 'tender_id', string="Tender Files")
    offer_lines = fields.One2many('procurement.tender.offers', 'tender_id', string="Tender Offers")
    item_lines = fields.One2many('procurement.tender.items', 'tender_id', string="Tender Items")

    notes = fields.Text(string="Notes")

    @api.model
    def create(self, vals):
        record = super(ProcurementTender, self).create(vals)

        if vals.get('no', _('New')) == _('New'):
            # vals['no'] = self.env['ir.sequence'].next_by_code('procurement.tender.sequence') or _('New')

            sequence = self.env['ir.sequence'].next_by_code(
                'procurement.tender.sequence') or _('New')
            sequence = sequence. \
                replace('TYPE_CODE', record.type_id.code)
            record.write({
                'no': sequence,
            })

            # print(self.type_id.code)
            # vals['no'] = str(self.type_id.code)
        # result = super(ProcurementTender, self).create(vals)
        return record


class ProcurementTenderType(models.Model):
    _name = 'procurement.tendertype'
    _description = 'Tender Type'

    name = fields.Char(string="Name")

    code = fields.Char(string="Code")

    total = fields.Integer(string='Total', readonly=True)


class ProcurementTenderStatus(models.Model):
    _name = 'procurement.tenderstatus'
    _description = 'Tender Status'

    name = fields.Char(string="Name", translate=True)


class ProcurementSupplierType(models.Model):
    _name = 'procurement.suppliertype'
    _description = 'Supplier Type'

    name = fields.Char(string="Name", translate=True)


class ProcurementTenderFiles(models.Model):
    _name = 'procurement.tender.files'
    _description = 'Tender Files'

    name = fields.Char(string="Name")
    file = fields.Binary("File")
    file_name = fields.Char('File Name')
    tender_id = fields.Many2one('procurement.tender', string="Tender ID")
    type = fields.Selection([
        ('technical_specification', 'Technical Specification'),
        ('agreement ', 'Agreement '),
        ('invoice ', 'Invoice '),
        ('tender_approval', 'Tender Approval '),
        ('other', 'Other')], string='File Type', default='other', required=False,
        help='Select suitable file type before upload')


class ProcurementTenderOffers(models.Model):
    _name = 'procurement.tender.offers'
    _description = 'Tender Offers'

    tender_id = fields.Many2one('procurement.tender', string="Tender ID")

    supplier_id = fields.Many2one(
        'res.partner', string='Supplier', readonly=False,
        index=True, tracking=1)

    price = fields.Float(string="Price")

    currency_id = fields.Many2one(
        'res.currency', string='Currency', readonly=False,
        index=True, tracking=1)

    vat = fields.Selection([
        ('included', 'VAT Included'),
        ('excluded', 'VAT Excluded')], string='VAT', default='excluded', required=False,
        help='Select suitable VAT type')

    proforma_file = fields.Binary("Proforma Invoice")
    proforma_file_name = fields.Char('Proforma Invoice Name')


class ProcurementTenderItems(models.Model):
    _name = 'procurement.tender.items'
    _description = 'Tender Items'

    tender_id = fields.Many2one('procurement.tender', string="Tender ID")

    product_id = fields.Many2one('product.product', string='Product', domain=[('purchase_ok', '=', True)],
                                 change_default=True)

    product_qty = fields.Float(string='Quantity', digits='Product Unit of Measure', required=True)
