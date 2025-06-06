from odoo import models, fields, api

class OpSession(models.Model):
    # Uso interno
    _name = 'schedule.schedule'
    _inherit = 'op.session' # Para seguimiento de cambios

    name = fields.Char(compute='_compute_name', store=True)

    # Sobrescritura de campos
    batch_id = fields.Many2one(
        'op.batch',
        string='Grupo Academico ',
        help='Cohorte de estudiantes',
        required=True,
    )
    classroom_id = fields.Many2one(
        'op.classroom',
        string='Aula aisgnada',
        help='Aula fisica donde se impartiran las clases'
    )

    # Metodo para nombrado automatizado
    @api.depends('batch_id')
    def _compute_name(self):
        for record in self:
            if record.batch_id:
                record.name = f'Horario - {record.batch_id.name}'
            else:
                record.name = 'Horario sin Grupo'
