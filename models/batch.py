from odoo import models, fields

class OpBatch(models.Model):
    # Uso interno
    # Herencia de OpenEduCat
    _inherit = 'op.batch'

    # Campos extras
    timetables_ids = fields.One2Many('op.session', 'batch_id', string='Horarios')

