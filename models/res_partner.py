from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_teacher = fields.Boolean(string='Is Teacher')
    is_freelancer = fields.Boolean(string='Is Freelancer')