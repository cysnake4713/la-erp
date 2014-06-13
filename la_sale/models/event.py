# coding=utf-8
from openerp.osv import osv, fields
from openerp.tools.translate import _


class PartnerEvent(osv.Model):
    _name = 'la.res.partner.event'
    _rec_name = 'note'
    _columns = {
        'type': fields.many2one('la.res.partner.event.type', 'Event Type', required=True),
        'note': fields.text(u'备注'),
        'partner_ids': fields.many2many('res.partner', 'rel_partner_event', 'event_id', 'partner_id', 'Partner'),
        'event_date': fields.date('Event Date'),
    }

    #TODO:
    _defaults = {
        'event_date': lambda *args: fields.date.today(),
    }


class PartnerEventType(osv.Model):
    _name = 'la.res.partner.event.type'
    _columns = {
        'name': fields.char('Name', 64, required=True),
    }

    _sql_constraints = [('partner_event_type_name_unique', 'unique(name)', _('name must be unique !'))]


class PartnerInherit(osv.Model):
    _inherit = 'res.partner'
    _columns = {
        'event_ids': fields.many2many('la.res.partner.event', 'rel_partner_event', 'partner_id', 'event_id', 'Event'),
    }