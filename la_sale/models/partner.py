__author__ = 'cysnake4713'

from openerp.osv import osv, fields
from openerp import SUPERUSER_ID


class PartnerInherit(osv.Model):
    _inherit = "res.partner"

    def _get_related_projects(self, cr, uid, ids, field_name, arg, context):
        result = dict.fromkeys(ids, False)
        project_obj = self.pool.get('la.project.project')
        for partner in self.browse(cr, uid, ids, context=context):
            project_ids = project_obj.search(cr, SUPERUSER_ID, ['|', ('customer_id', '=', partner.id),
                                                                ('customer_contact_ids', '=', partner.id)],
                                             context=context)
            related_projects_number = ','.join(
                [p.number for p in project_obj.browse(cr, SUPERUSER_ID, project_ids, context) if p.number])
            result[partner.id] = {
                'related_projects': project_ids,
                'related_projects_number': related_projects_number,
            }
        return result

    _columns = {
        'importance': fields.char('Importance', 64),
        'related_projects': fields.function(_get_related_projects, type='many2many', obj='la.project.project',
                                            string='Related Projects',
                                            multi='project'),
        'related_projects_number': fields.function(_get_related_projects, type='char', string='Related Projects Number',
                                                   multi='project'),
        # TODO:
        'customer_type': fields.selection(
            selection=[('friendly_co', 'Friend Co'), ('project_partner', 'Project Partner'),
                       ('pertential', 'Pertential'), ('else', 'Else')], string='Customer Type'),
    }

    def name_get(self, cr, user, ids, context=None):
        """Returns the preferred display value (text representation) for the records with the
           given ``ids``. By default this will be the value of the ``name`` column, unless
           the model implements a custom behavior.
           Can sometimes be seen as the inverse function of :meth:`~.name_search`, but it is not
           guaranteed to be.

           :rtype: list(tuple)
           :return: list of pairs ``(id,text_repr)`` for all records with the given ``ids``.
        """
        if not ids:
            return []
        if isinstance(ids, (int, long)):
            ids = [ids]

        if self._rec_name in self._all_columns:
            rec_name_column = self._all_columns[self._rec_name].column
            return [(r['id'], rec_name_column.as_display_name(cr, user, self, r[self._rec_name], context=context))
                    for r in self.read(cr, user, ids, [self._rec_name],
                                       load='_classic_write', context=context)]
        return [(id, "%s,%s" % (self._name, id)) for id in ids]

    def _fields_sync(self, cr, uid, partner, update_values, context=None):
        super(PartnerInherit, self)._fields_sync(cr, uid, partner, update_values, context)
        # if update partner parent
        if update_values.get('parent_id') and partner.is_company is False:
            if partner.parent_id:
                partner.write({'customer_type': partner.parent_id.customer_type})
        # if update a company
        if partner.child_ids:
            partner.child_ids.write({'customer_type': partner.customer_type})