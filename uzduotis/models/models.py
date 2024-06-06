from odoo import models, fields

class Dokumentai(models.Model):
    _name = 'dokumentai'
    _description = 'Dokumentų informacija'

    pavadinimas = fields.Char(required=True)
    aprasymas = fields.Text(string='Aprašymas')
    imone = fields.Char(string='Įmonė')
    sukure = fields.Many2one('res.users', string='Įrašo autorius', default=lambda self: self.env.user)
    palaikymas = fields.Many2many('res.users', string='Prižiūri')
