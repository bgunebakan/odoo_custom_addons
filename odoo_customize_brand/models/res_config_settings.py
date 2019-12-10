# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    app_system_name = fields.Char('System Name', help="Setup System Name,which replace Odoo")
    app_show_lang = fields.Boolean('Show Quick Language Switcher',
                                   help="When enable,User can quick switch language in user menu")
    app_show_debug = fields.Boolean('Show Quick Debug', help="When enable,everyone login can see the debug menu")
    app_show_documentation = fields.Boolean('Show Documentation', help="When enable,User can visit user manual")
    app_show_documentation_dev = fields.Boolean('Show Developer Documentation',
                                                help="When enable,User can visit development documentation")
    app_show_support = fields.Boolean('Show Support', help="When enable,User can vist your support site")
    app_show_account = fields.Boolean('Show My Account', help="When enable,User can login to your website")
    app_show_enterprise = fields.Boolean('Show Enterprise Tag', help="Uncheck to hide the Enterprise tag")
    app_show_share = fields.Boolean('Show Share Dashboard', help="Uncheck to hide the Odoo Share Dashboard")
    app_show_poweredby = fields.Boolean('Show Powered by Odoo', help="Uncheck to hide the Powered by text")
    group_show_author_in_apps = fields.Boolean(string="Show Author in Apps Dashboard", implied_group='odoo_customize_brand.group_show_author_in_apps',
                                               help="Uncheck to Hide Author and Website in Apps Dashboard")

    app_documentation_url = fields.Char('Documentation Url')
    app_documentation_dev_url = fields.Char('Developer Documentation Url')
    app_support_url = fields.Char('Support Url')
    app_account_title = fields.Char('My Odoo.com Account Title')
    app_account_url = fields.Char('My Odoo.com Account Url')
    app_enterprise_url = fields.Char('Customize Module Url(eg. Enterprise)')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        ir_config = self.env['ir.config_parameter'].sudo()
        app_system_name = ir_config.get_param('app_system_name', default='odooApp')

        app_show_lang = True if ir_config.get_param('app_show_lang') == "True" else False
        app_show_debug = True if ir_config.get_param('app_show_debug') == "True" else False
        app_show_documentation = True if ir_config.get_param('app_show_documentation') == "True" else False
        app_show_documentation_dev = True if ir_config.get_param('app_show_documentation_dev') == "True" else False
        app_show_support = True if ir_config.get_param('app_show_support') == "True" else False
        app_show_account = True if ir_config.get_param('app_show_account') == "True" else False
        app_show_enterprise = True if ir_config.get_param('app_show_enterprise') == "True" else False
        app_show_share = True if ir_config.get_param('app_show_share') == "True" else False
        app_show_poweredby = True if ir_config.get_param('app_show_poweredby') == "True" else False

        app_documentation_url = ir_config.get_param('app_documentation_url',
                                                    default='https://creworker.com')
        app_documentation_dev_url = ir_config.get_param('app_documentation_dev_url',
                                                        default='https://creworker.com')
        app_support_url = ir_config.get_param('app_support_url', default='https://creworker.com')
        app_account_title = ir_config.get_param('app_account_title', default='My Online Account')
        app_account_url = ir_config.get_param('app_account_url', default='https://creworker.com')
        app_enterprise_url = ir_config.get_param('app_enterprise_url', default='https://creworker.com')
        res.update(
            app_system_name=app_system_name,
            app_show_lang=app_show_lang,
            app_show_debug=app_show_debug,
            app_show_documentation=app_show_documentation,
            app_show_documentation_dev=app_show_documentation_dev,
            app_show_support=app_show_support,
            app_show_account=app_show_account,
            app_show_enterprise=app_show_enterprise,
            app_show_share=app_show_share,
            app_show_poweredby=app_show_poweredby,

            app_documentation_url=app_documentation_url,
            app_documentation_dev_url=app_documentation_dev_url,
            app_support_url=app_support_url,
            app_account_title=app_account_title,
            app_account_url=app_account_url,
            app_enterprise_url=app_enterprise_url
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        ir_config = self.env['ir.config_parameter'].sudo()
        ir_config.set_param("app_system_name", self.app_system_name or "")
        ir_config.set_param("app_show_lang", self.app_show_lang or "False")
        ir_config.set_param("app_show_debug", self.app_show_debug or "False")
        ir_config.set_param("app_show_documentation", self.app_show_documentation or "False")
        ir_config.set_param("app_show_documentation_dev", self.app_show_documentation_dev or "False")
        ir_config.set_param("app_show_support", self.app_show_support or "False")
        ir_config.set_param("app_show_account", self.app_show_account or "False")
        ir_config.set_param("app_show_enterprise", self.app_show_enterprise or "False")
        ir_config.set_param("app_show_share", self.app_show_share or "False")
        ir_config.set_param("app_show_poweredby", self.app_show_poweredby or "False")

        ir_config.set_param("app_documentation_url",
                            self.app_documentation_url or "https://creworker.com")
        ir_config.set_param("app_documentation_dev_url",
                            self.app_documentation_dev_url or "https://creworker.com")
        ir_config.set_param("app_support_url", self.app_support_url or "https://creworker.com")
        ir_config.set_param("app_account_title", self.app_account_title or "My Online Account")
        ir_config.set_param("app_account_url", self.app_account_url or "https://creworker.com")
        ir_config.set_param("app_enterprise_url", self.app_enterprise_url or "https://creworker.com")

    def set_module_url(self):
        sql = "UPDATE ir_module_module SET website = '%s' WHERE license like '%s' and website <> ''" % (self.app_enterprise_url, 'OEEL%')
        try:
            self._cr.execute(sql)
            self._cr.commit()
        except Exception as e:
            pass

    def remove_sales(self):
        to_removes = [

            ['sale.order.line', ],
            ['sale.order', ],
            ['sale.commission.line', ],
            # ['sale.order.template.option', ],
            # ['sale.order.template.line', ],
            # ['sale.order.template', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()

            seqs = self.env['ir.sequence'].search([('code', 'like', 'sale%')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
        except Exception as e:
            raise Warning(e)
        return True

    def remove_product(self):
        to_removes = [

            ['product.product', ],
            ['product.template', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()

            seqs = self.env['ir.sequence'].search([('code', '=', 'product.product')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_product_attribute(self):
        to_removes = [

            ['product.attribute.value', ],
            ['product.attribute', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_pos(self):
        to_removes = [

            ['pos.payment', ],
            ['pos.order.line', ],
            ['pos.order', ],
            ['pos.session', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()

            seqs = self.env['ir.sequence'].search([('code', 'like', 'pos.%')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })

            statement = self.env['account.bank.statement'].search([])
            for s in statement:
                s._end_balance()

        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_purchase(self):
        to_removes = [

            ['purchase.order.line', ],
            ['purchase.order', ],
            ['purchase.requisition.line', ],
            ['purchase.requisition', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()

            seqs = self.env['ir.sequence'].search([('code', 'like', 'purchase.%')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
            self._cr.execute(sql)
            self._cr.commit()
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_expense(self):
        to_removes = [

            ['hr.expense.sheet', ],
            ['hr.expense', ],
            ['hr.payslip', ],
            ['hr.payslip.run', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()

            seqs = self.env['ir.sequence'].search([
                ('code', 'like', 'hr.expense.%')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
            self._cr.execute(sql)
            self._cr.commit()
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_mrp(self):
        to_removes = [

            ['mrp.workcenter.productivity', ],
            ['mrp.workorder', ],
            ['mrp.production.workcenter.line', ],
            ['change.production.qty', ],
            ['mrp.production', ],
            ['mrp.production.product.line', ],
            ['mrp.unbuild', ],
            ['change.production.qty', ],
            ['sale.forecast.indirect', ],
            ['sale.forecast', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()

            seqs = self.env['ir.sequence'].search([('code', 'like', 'mrp.%')])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_mrp_bom(self):
        to_removes = [

            ['mrp.bom.line', ],
            ['mrp.bom', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_inventory(self):
        to_removes = [

            ['stock.quant', ],
            ['stock.move.line', ],
            ['stock.package.level', ],
            ['stock.quantity.history', ],
            ['stock.quant.package', ],
            ['stock.move', ],
            # ['stock.pack.operation', ],
            ['stock.picking', ],
            ['stock.scrap', ],
            ['stock.picking.batch', ],
            ['stock.inventory.line', ],
            ['stock.inventory', ],
            ['stock.valuation.layer', ],
            ['stock.production.lot', ],
            # ['stock.fixed.putaway.strat', ],
            ['procurement.group', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()

            seqs = self.env['ir.sequence'].search([
                '|', ('code', 'like', 'stock.%'),
                '|', ('code', 'like', 'picking.%'),
                '|', ('prefix', '=', 'WH/IN/'),
                '|', ('prefix', '=', 'WH/INT/'),
                '|', ('prefix', '=', 'WH/OUT/'),
                '|', ('prefix', '=', 'WH/PACK/'),
                ('prefix', '=', 'WH/PICK/')
            ])
            for seq in seqs:
                seq.write({
                    'number_next': 1,
                })
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_account(self):
        to_removes = [

            ['account.voucher.line', ],
            ['account.voucher', ],
            ['account.bank.statement.line', ],
            ['account.payment', ],
            ['account.analytic.line', ],
            ['account.analytic.account', ],
            ['account.invoice.line', ],
            ['account.invoice.refund', ],
            ['account.invoice', ],
            ['account.partial.reconcile', ],
            ['account.move.line', ],
            ['hr.expense.sheet', ],
            ['account.move', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()


                    seqs = self.env['ir.sequence'].search([
                        '|', ('code', 'like', 'account.%'),
                        '|', ('prefix', 'like', 'BNK1/'),
                        '|', ('prefix', 'like', 'CSH1/'),
                        '|', ('prefix', 'like', 'INV/'),
                        '|', ('prefix', 'like', 'EXCH/'),
                        '|', ('prefix', 'like', 'MISC/'),
                        '|', ('prefix', 'like', '账单/'),
                        ('prefix', 'like', '杂项/')
                    ])
                    for seq in seqs:
                        seq.write({
                            'number_next': 1,
                        })
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_account_chart(self):
        to_removes = [

            ['res.partner.bank', ],
            ['res.bank', ],
            ['account.move.line'],
            ['account.invoice'],
            ['account.payment'],
            ['account.bank.statement', ],
            ['account.tax.account.tag', ],
            ['account.tax', ],
            ['account.tax', ],
            ['account.account.account.tag', ],
            ['wizard_multi_charts_accounts'],
            ['account.account', ],
            ['account.journal', ],
        ]
        # todo: remove_hr account

        try:
            # reset default tax
            field1 = self.env['ir.model.fields']._get('product.template', "taxes_id").id
            field2 = self.env['ir.model.fields']._get('product.template', "supplier_taxes_id").id

            sql = ("delete from ir_default where field_id = %s or field_id = %s") % (field1, field2)
            self._cr.execute(sql)
            self._cr.commit()
        except Exception as e:
            pass  # raise Warning(e)
        try:
            rec = self.env['res.partner'].search([])
            for r in rec:
                r.write({
                    'property_account_receivable_id': None,
                    'property_account_payable_id': None,
                })
        except Exception as e:
            pass  # raise Warning(e)
        try:
            rec = self.env['product.category'].search([])
            for r in rec:
                r.write({
                    'property_account_income_categ_id': None,
                    'property_account_expense_categ_id': None,
                    'property_account_creditor_price_difference_categ': None,
                    'property_stock_account_input_categ_id': None,
                    'property_stock_account_output_categ_id': None,
                    'property_stock_valuation_account_id': None,
                })
        except Exception as e:
            pass  # raise Warning(e)
        try:
            rec = self.env['stock.location'].search([])
            for r in rec:
                r.write({
                    'valuation_in_account_id': None,
                    'valuation_out_account_id': None,
                })
        except Exception as e:
            pass  # raise Warning(e)

        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()


            sql = "update res_company set chart_template_id=null;"
            self._cr.execute(sql)
            self._cr.commit()
            # 更新序号
        except Exception as e:
            pass

        return True

    def remove_project(self):
        to_removes = [

            ['account.analytic.line', ],
            ['project.task', ],
            ['project.forecast', ],
            ['project.project', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()
            # 更新序号
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_website(self):
        to_removes = [

            ['blog.tag.category', ],
            ['blog.tag', ],
            ['blog.post', ],
            ['blog.blog', ],
            ['website.published.multi.mixin', ],
            ['website.published.mixin', ],
            ['website.multi.mixin', ],
            ['website.redirect', ],
            ['website.seo.metadata', ],
            ['website.page', ],
            ['website.menu', ],
            ['website', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj and obj._table:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_message(self):
        to_removes = [

            ['mail.message', ],
            ['mail.followers', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj and obj._table:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()
        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_workflow(self):
        to_removes = [

            ['wkf.workitem', ],
            ['wkf.instance', ],
        ]
        try:
            for line in to_removes:
                obj_name = line[0]
                obj = self.pool.get(obj_name)
                if obj and obj._table:
                    sql = "delete from %s" % obj._table
                    self._cr.execute(sql)
                    self._cr.commit()

        except Exception as e:
            pass  # raise Warning(e)
        return True

    def remove_all_biz(self):
        try:
            self.remove_account()
            self.remove_inventory()
            self.remove_mrp()
            self.remove_purchase()
            self.remove_sales()
            self.remove_project()
            self.remove_pos()
            self.remove_expense()
            self.remove_message()
        except Exception as e:
            pass  # raise Warning(e)
        return True
