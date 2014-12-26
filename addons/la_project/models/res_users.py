from openerp import SUPERUSER_ID

from openerp.osv import osv


class ResUsers(osv.Model):
    _inherit = "res.users"

    def _get_group(self, cr, uid, context=None):
        result = super(ResUsers, self)._get_group(cr, uid, context=context)
        data_obj = self.pool.get('ir.model.data')
        dummy, group_id = data_obj.get_object_reference(cr, SUPERUSER_ID, 'la_project', 'project_user')
        result.append(group_id)
        return result

    _defaults = {
        'groups_id': _get_group,
    }