# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 ITS-1 (<http://www.its1.lv/>)
#                       E-mail: <info@its1.lv>
#                       Address: <Vienibas gatve 109 LV-1058 Riga Latvia>
#                       Phone: +371 66116534
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Web - Session',
    'version': '1.0',
    'description': 
    """
Web session length configuration.
====================================================
Session length is a period of time the user will stay logged in the system without any activity.

You can configure Session Length in Settings -> Configuration -> General Settings. The format needs to be HH:MM.

After pressing "Apply" the session length parameter value is saved in Settings -> Technical -> Parameters -> System Parameters with the key named "web_session.length".

Users last activity datetime can be visible in Users list view (Settings -> Users -> Users) column "Latest action".
    """,
    'category': 'Tools',
    'author': 'ITS-1',
    'website': 'http://www.its1.lv',
    'depends': ['web', 'base_setup'],
    'data': [
        'views/webclient_templates.xml',
        'res_users_view.xml',
        'res_config_view.xml',
        'data/data.xml'
    ],
    'js': [
        'static/src/js/openerpframework.js'
    ],
    'installable': True,
    'auto_install': False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: