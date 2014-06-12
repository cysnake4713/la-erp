from openerp.osv import osv
from openerp.tools.safe_eval import safe_eval

__author__ = 'cysnake4713'


class ResPartnerInherit(osv.osv):
    _inherit = "res.partner"
    _defaults = {
        'country_id': lambda self, cr, uid, ctx: self.pool.get('ir.model.data').get_object_reference(cr, 1, 'base', 'cn')[1],
    }
