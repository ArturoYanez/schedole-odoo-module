from odoo import models, fields, api

class ScheduleSession(models.Model):
    _inherit = 'op.session'

    classroom_code = fields.Char(string='Código de aula')
    
    # Campo display_name calculado
    display_name = fields.Char(
        string='Nombre a Mostrar',
        compute='_compute_display_name',
        store=True
    )
    
    @api.depends('faculty_id', 'subject_id', 'start_datetime', 'end_datetime')
    def _compute_display_name(self):
        tz = pytz.timezone(self.env.user.tz or 'UTC')
        for session in self:
            parts = []
            if session.faculty_id and session.faculty_id.name:
                parts.append(session.faculty_id.name)
            if session.subject_id and session.subject_id.name:
                parts.append(session.subject_id.name)
            if session.start_datetime and session.end_datetime:
                start = session.start_datetime.astimezone(tz).strftime('%H:%M')
                end = session.end_datetime.astimezone(tz).strftime('%H:%M')
                parts.append(f"{start}-{end}")
            session.display_name = " - ".join(parts) if parts else f"Sesión #{session.id}"