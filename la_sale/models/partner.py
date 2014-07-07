__author__ = 'cysnake4713'

from openerp.osv import osv, fields
from openerp import SUPERUSER_ID


class ParnterInherit(osv.Model):
    _inherit = "res.partner"

    def _get_related_projects(self, cr, uid, ids, field_name, arg, context):
        result = dict.fromkeys(ids, False)
        project_obj = self.pool.get('la.project.project')
        for partner in self.browse(cr, uid, ids, context=context):
            project_ids = project_obj.search(cr, SUPERUSER_ID, ['|', ('customer_id', '=', partner.id), ('customer_contact_ids', '=', partner.id)],
                                             context=context)
            related_projects_number = ','.join([p.number for p in project_obj.browse(cr, SUPERUSER_ID, project_ids, context)])
            result[partner.id] = {
                'related_projects': project_ids,
                'related_projects_number': related_projects_number,
            }
        return result

    _columns = {
        'importance': fields.char('Importance', 64),
        'related_projects': fields.function(_get_related_projects, type='many2many', obj='la.project.project', string='Related Projects',
                                            multi='project'),
        'related_projects_number': fields.function(_get_related_projects, type='char', string='Related Projects Number',
                                                   multi='project'),
    }