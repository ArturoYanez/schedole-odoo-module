/** @odoo-module **/
import { CalendarController } from "@web/views/calendar/calendar_controller";

export class CustomCalendarController extends CalendarController {
    setup() {
        super.setup();
        // Configurar opciones de FullCalendar
        this.props.config.hiddenDays = [0, 6]; // Ocultar domingo(0) y sábado(6)
        this.props.config.slotMinTime = "08:00:00";
        this.props.config.slotMaxTime = "20:00:00";
    }
}

registry.category("views").add("calendar_op_session_custom", {
    ...calendarView,
    Controller: CustomCalendarController,
});