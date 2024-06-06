from odoo import models, fields

class DokumentaiWizard(models.TransientModel):
    _name = 'dokumentai.wizard'
    _description = 'Dokumentai Wizard'

    start_date = fields.Date(string="Nuo")
    end_date = fields.Date(string="Iki")
    user_id = fields.Many2one('res.users', string="Darbuotojas")

    def action_wizard(self):
        domain = []
        if not self.user_id:
            if self.start_date and not self.end_date:
                domain.append(('create_date', '>=', self.start_date))
            if self.end_date and not self.start_date:
                domain.append(('create_date', '<=', self.end_date))
            if self.start_date and self.end_date:
                domain += ['&',
                             ('create_date', '>=', self.start_date),
                             ('create_date', '<=', self.end_date)]
        else:
            if not self.start_date and not self.end_date:
                domain.append(('sukure', '=', self.user_id.id))
            if self.start_date and not self.end_date:
                domain += ['&',
                             ('sukure', '=', self.user_id.id),
                             ('create_date', '>=', self.start_date)]
            if self.end_date and not self.start_date:
                domain += ['&',
                             ('sukure', '=', self.user_id.id),
                             ('create_date', '<=', self.end_date)]
            if self.start_date and self.end_date:
                domain += ['&',
                             ('sukure', '=', self.user_id.id),
                             '&',
                               ('create_date', '>=', self.start_date),
                               ('create_date', '<=', self.end_date)]

        return {
            'type': 'ir.actions.act_window',
            'name': 'Išfiltruoti Dokumentai',
            'view_mode': 'tree,form',
            'res_model': 'dokumentai',
            'domain': domain,
        }