# coding=utf-8
from openerp.osv import osv
from openerp.osv import fields

__author__ = 'cysnake4713'


class LaProject(osv.osv):
    _name = "la.project.project"
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _columns = {
        'name': fields.char(u'项目名称', 128),
        'type': fields.char(u'项目类型', 128),
        'manager': fields.char(u'项目负责人', 128),
        'director': fields.char(u'主管总师', 128),
        'percent': fields.char(u'项目进度', 128),
        'income_ids': fields.many2many('la.project.income', 'la_project_income_rel', 'project_id', 'income_id', string='Incomes'),
        'state_id': fields.many2one('la.project.state', string=u'状态')
    }
    _defaults = {
        # 'state_id': lambda *a: 'begin',
    }


class LaProjectState(osv.osv):
    _name = 'la.project.state'
    _order = 'index asc'
    _columns = {
        'index': fields.integer(string='Index'),
        'name': fields.char('Name', 128),
    }


class LaProjectIncome(osv.osv):
    _name = "la.project.income"
    _columns = {
        'price': fields.char(u'金额', 128),
        'get_time': fields.char(u'时间', 128),
    }