# -*- encoding: utf-8 -*-
# __author__ = cysnake4713@gmail.com
# #############################################################################
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Project Module For Leiao Company',
    'version': '0.1',
    'author': 'cysnake4713',
    'maintainer': 'cysnake4713@gmail.com',
    'website': 'http://www.cysnake.com',
    'description': u"""
Project Module For Leiao Company
""",
    'depends': ['base'],
    'category': 'Project Management',
    'demo_xml': [],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',

        'views/project_view.xml',
        'views/project_menu.xml',
        'views/project_setting_view.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
}