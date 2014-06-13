# -*- encoding: utf-8 -*-
# __author__ = cysnake4713@gmail.com
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
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
    'name': 'Localization Module For Chinese',
    'version': '0.1',
    'author': 'cysnake4713',
    'maintainer': 'cysnake4713@gmail.com',
    'website': 'http://www.cysnake.com',
    'description': u"""
Localization Module For Chinese
""",
    'depends': [],
    'category': 'Localization',
    'demo_xml': [],
    'data': [
        'views/base_override.xml',
        'data/base_data.xml',
    ],
    'qweb': [
        'static/src/xml/base_web.xml',
    ],
    'installable': True,
}