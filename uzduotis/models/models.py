from odoo import models, fields

class Dokumentai(models.Model):
    _name = 'dokumentai'
    _description = 'Dokumentu informacija'

    pavadinimas = fields.Char(required=True)
    aprasymas = fields.Text()
    imone = fields.Char()



# class uzduotis(models.Model):
#     _name = 'uzduotis.uzduotis'
#     _description = 'uzduotis.uzduotis'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

