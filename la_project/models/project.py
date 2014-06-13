# coding=utf-8
from openerp.osv import osv
from openerp.osv import fields
from openerp.tools.translate import _

__author__ = 'cysnake4713'


class LaProject(osv.Model):
    _name = "la.project.project"
    # _inherit = ['mail.thread', 'ir.needaction_mixin']

    def _get_receive_funds(self, cr, uid, ids, field_name, args, context=None):
        result = dict.fromkeys(ids, {'receive_funds': 0.0, 'receive_percent': 0.0})
        # for obj in self.browse(cr, uid, ids, context=context):
        # if self.is_project_member(cr, context.get('uid', 1), obj.id, context=context):
        # result[obj.id] = True
        # else:
        # result[obj.id] = False
        return result

    _columns = {
        # base
        'type_id': fields.many2one('la.project.type', 'Project Type'),
        'customer_id': fields.many2one('res.partner', 'Project Customer'),
        'name': fields.char('Project Name', 128, required=True),
        'temp_department_id': fields.many2many('la.project.temp.department', 'rel_project_temp_department', 'project_id', 'department_id',
                                               'Temp Design Department'),
        'number': fields.char('Project Number', 64),
        'sign_date': fields.date('Project Sign_date'),
        'scale': fields.char('Project Scale', 128),
        'location': fields.char('Project Location'),
        # quality
        'level': fields.selection([('segment', 'Segment'), ('headquarter', 'Headquarter')], 'Project Level'),
        'temp_chief_ids': fields.many2many('la.project.temp.member', 'rel_temp_chief_member', 'temp_chief_id', 'member_id', 'Temp Project Chief'),
        'temp_user_ids': fields.many2many('la.project.temp.member', 'rel_temp_user_member', 'temp_user_id', 'member_id', 'Temp Project Manager'),
        'is_documented': fields.boolean('Is Documented'),
        'design_plan': fields.char('Design Plan', 256),
        'design_input': fields.char('Design Input', 256),
        'design_approve': fields.char('Design Approve', 256),
        'design_confirm': fields.char('Design confirm', 256),
        'quality_comment': fields.text('Quality Comment'),
        # Progress
        # TODO:
        'state': fields.selection([('begin', 'Begin')], 'Project State'),
        'progress_percent': fields.char('Progress Percent', 16),
        'this_month_report': fields.char('This Month Report', 128),
        'next_month_report': fields.char('Next Month Report', 128),
        'progress_comment': fields.text('Progress Comment'),

        # Incomes
        'total_funds': fields.float('Total Funds', digits=(8, 2)),
        'income_ids': fields.one2many('la.project.income', 'project_id', string='Project Incomes'),
        'receive_funds': fields.function(_get_receive_funds, type='float', multi='receive', string='Receive Funds'),
        'receive_percent': fields.function(_get_receive_funds, type='float', multi='receive', string='Receive Percent'),
        'funds_comment': fields.text('Funds Comment'),
        'headquarter_deduct': fields.char('HeadQuarter Deduct', 64),

        'comment': fields.text('Project Comment'),
    }
    _defaults = {
        # 'state_id': lambda *a: 'begin',
    }

    _sql_constraints = [('project_number_unique', 'unique(number)', _('number must be unique !'))]

    def name_search(self, cr, user, name='', args=None, operator='ilike', context=None, limit=100):
        if not args:
            args = []
        if not context:
            context = {}
        ids = []
        if name:
            ids = self.search(cr, user, [('number', '=', name)] + args, limit=limit, context=context)
        if not ids:
            ids = self.search(cr, user, [('name', operator, name)] + args, limit=limit, context=context)
        return self.name_get(cr, user, ids, context=context)


class LaProjectType(osv.Model):
    _name = 'la.project.type'
    _columns = {
        'name': fields.char('Name', 128, required=True),
    }
    _sql_constraints = [('project_type_unique', 'unique(name)', _('name must be unique !'))]


class LaTempDepartment(osv.Model):
    _name = 'la.project.temp.department'
    _columns = {
        'name': fields.char('Name', 64, required=True),
    }
    _sql_constraints = [('project_temp_department_unique', 'unique(name)', _('name must be unique !'))]


class LaTempMember(osv.Model):
    _name = 'la.project.temp.member'
    _columns = {
        'name': fields.char('Name', 64, required=True),
    }
    _sql_constraints = [('project_temp_member_unique', 'unique(name)', _('name must be unique !'))]


class LaProjectIncome(osv.Model):
    _name = "la.project.income"
    _rec_name = 'paid_date'
    _columns = {
        'price': fields.float('Price', (8, 2)),
        'paid_date': fields.date('Paid Date'),
        'project_id': fields.many2one('la.project.project', 'Project', required=True),
    }


    # class PartnerEvent(osv.osv):
    # _name = "res.partner.event"
    # _inherit = ['mail.thread', 'ir.needaction_mixin']
    # _rec_name = 'note'
    # _columns = {
    # 'type': fields.char(u'类型', 128),
    # 'note': fields.text(u'备注'),
    # 'partner_ids': fields.many2many('res.partner', 'rel_partner_event', 'event_id', 'partner_id', u'客户'),
    # }


    # class PartnerInherit(osv.osv):
    # _inherit = "res.partner"
    # _columns = {
    # 'event_ids': fields.many2many('res.partner.event', 'rel_partner_event', 'partner_id', 'event_id', u'事件'),
    # }