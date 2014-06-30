# coding=utf-8
from openerp.osv import osv
from openerp.osv import fields
from openerp.tools.translate import _

__author__ = 'cysnake4713'


class LaProject(osv.Model):
    _name = "la.project.project"
    # _inherit = ['mail.thread', 'ir.needaction_mixin']

    # noinspection PyUnusedLocal
    def _get_receive_funds(self, cr, uid, ids, field_name, args, context=None):
        result = dict.fromkeys(ids, {'receive_funds': 0.0, 'receive_percent': 0.0})
        for obj in self.browse(cr, uid, ids, context=context):
            prices = sum([i.price for i in obj.income_ids])
            receive_percent = prices / obj.total_funds * 100 if obj.total_funds else 0
            result[obj.id].update({'receive_funds': prices, 'receive_percent': receive_percent})
        return result

    # noinspection PyUnusedLocal
    def _function_chief_ids(self, cr, uid, ids, name, args, context=None):
        result = dict.fromkeys(ids, False)
        for obj in self.browse(cr, uid, ids, context=context):
            result[obj.id] = ','.join([d.name for d in obj.temp_department_ids])
        return result

    _columns = {
        # base
        'type_ids': fields.many2many('la.project.type', 'rel_project_type', 'project_id', 'type_id', 'Project Types'),
        'customer_id': fields.many2one('res.partner', 'Project Customer', domain=[('customer', '=', True)]),
        'customer_state': fields.related('customer_id', 'state_id', type='many2one', relation='res.country.state', string='Customer State'),
        'customer_city': fields.related('customer_id', 'city', type='char', string='Customer City'),
        'customer_contact_ids': fields.many2many('res.partner', 'rel_project_contact_partner', 'project_id', 'partner_id',
                                                 string='Customer Contacts', domain=[('customer', '=', True)]),
        'name': fields.char('Project Name', 128, required=True),
        'temp_department_ids': fields.many2many('la.project.temp.department', 'rel_project_temp_department', 'project_id', 'department_id',
                                                'Temp Design Department'),
        'number': fields.char('Project Number', 128),
        'sign_date': fields.date('Project Sign_date'),
        'scale': fields.char('Project Scale', 128),
        'location': fields.char('Project Location'),
        # quality
        'level': fields.selection([('segment', 'Segment'), ('headquarter', 'Headquarter')], 'Project Level'),
        'temp_chief_ids': fields.many2many('la.project.temp.member', 'rel_temp_chief_member', 'temp_chief_id', 'member_id', 'Temp Project Chief',
                                           store=True),
        'function_chief_ids': fields.function(_function_chief_ids, type='char', string='For Search Chiefs', store=True),
        'temp_user_ids': fields.many2many('la.project.temp.member', 'rel_temp_user_member', 'temp_user_id', 'member_id', 'Temp Project Manager'),
        'is_documented': fields.boolean('Is Documented'),
        'design_plan': fields.char('Design Plan', 256),
        'design_input': fields.char('Design Input', 256),
        'design_approve': fields.char('Design Approve', 256),
        'design_confirm': fields.char('Design confirm', 256),
        'quality_comment': fields.text('Quality Comment'),
        # Progress
        'state': fields.selection([('plan', 'Initial Plan'),
                                   ('research', 'Research & Input'),
                                   ('init', 'Initial program'),
                                   ('deep', 'Deep Program'),
                                   ('output', 'Project Output'),
                                   ('complete', 'Complete')], 'Project State'),
        'progress_percent': fields.char('Progress Percent', 16),
        'this_month_report': fields.char('This Month Report', 128),
        'next_month_report': fields.char('Next Month Report', 128),
        'progress_comment': fields.text('Progress Comment'),

        # Incomes
        'total_funds': fields.float('Total Funds', digits=(10, 4)),
        'income_ids': fields.one2many('la.project.income', 'project_id', string='Project Incomes'),
        'receive_funds': fields.function(_get_receive_funds, type='float', digits=(10, 4), multi='receive', string='Receive Funds (wan)'),
        'receive_percent': fields.function(_get_receive_funds, type='float', digits=(10, 2), multi='receive', string='Receive Percent (%)'),
        'funds_comment': fields.text('Funds Comment'),
        'headquarter_deduct': fields.char('HeadQuarter Deduct', 64),

        'comment': fields.text('Project Comment'),
        'is_pause': fields.boolean('Is Project Pause'),
        'importance': fields.char('Importance', 64),
    }
    _defaults = {
        # 'state': lambda *a: 'plan',
        'sign_date': lambda *args: fields.date.today(),
    }

    # _sql_constraints = [('project_number_unique', 'unique(number)', _('number must be unique !'))]

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
        'price': fields.float('Price', digits=(10, 4), required=True),
        'paid_date': fields.date('Paid Date'),
        'project_id': fields.many2one('la.project.project', 'Project', required=True),
    }

    _defaults = {
        'paid_date': lambda *args: fields.date.today(),
    }