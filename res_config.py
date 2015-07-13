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

from openerp.osv import osv, fields
from openerp import SUPERUSER_ID

class base_config_settings(osv.TransientModel):
    _inherit = 'base.config.settings'

    _columns = {
        'session_length': fields.float('Session Length', help='Session length of all users - a period of time the user will stay logged in the system without any activity; format: HH:MM.')
    }

    def get_default_session_length(self, cr, uid, ids, context=None):
        param_obj = self.pool.get('ir.config_parameter')
        length = param_obj.get_param(cr, SUPERUSER_ID, 'web_session.length', default='', context=context)
        session_length = False
        if length and ':' in length:
            time_list = length.split(':')
            if len(time_list) == 2:
                hours = int(time_list[0])
                minutes = int(time_list[1])/60.0
                session_length = hours + minutes
        return {'session_length': session_length or False}

    def set_session_length(self, cr, uid, ids, context=None):
        for record in self.browse(cr, SUPERUSER_ID, ids, context=context):
            if record.session_length and record.session_length > 0.0:
                minutes = record.session_length*60
                hours, minutes = divmod(minutes, 60)
                session_length = "%02d:%02d"%(hours,minutes)
                param_obj = self.pool.get('ir.config_parameter')
                param_obj.set_param(cr, SUPERUSER_ID, 'web_session.length', session_length, context=context)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: