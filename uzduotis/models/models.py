from odoo import models, fields

class Dokumentai(models.Model):
    _name = 'dokumentai'
    _description = 'Dokumentų informacija'

    pavadinimas = fields.Char(required=True)
    aprasymas = fields.Text()
    imone = fields.Char()
    sukure = fields.Many2one('res.users', string='Įrašo autorius', default=lambda self: self.env.user)
    palaikymas = fields.Many2many('res.users', string='Prižiūri')
