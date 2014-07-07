__author__ = 'cysnake4713'

from openerp.osv import osv, fields


class ParnterInherit(osv.Model):
    _inherit = "res.partner"

    _columns = {
        'importance': fields.char('Importance', 64),
    }