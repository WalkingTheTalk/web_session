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

import os
import random
import time
import openerp
from openerp import SUPERUSER_ID
import openerp.http
import werkzeug

from openerp import sql_db
from openerp.modules.registry import RegistryManager
from openerp import tools
from pickle import dump, load, HIGHEST_PROTOCOL
from openerp.addons.web.http import Controller, route, request

def _new_session_gc(session_store):
    for fname in os.listdir(session_store.path):
        path = os.path.join(session_store.path, fname)
        f = open(path, 'rb')
        try:
            if f:
                session_data = load(f)
            else:
                session_data = {}
        except:
            session_data = {}
        f.close()
        minutes = 60
        hours = 24*7
        if session_data.get('db',None) != None:
            db = sql_db.db_connect(session_data['db'])
            cr = db.cursor()
            pool = RegistryManager.get(cr.dbname)
            param = pool['ir.config_parameter'].get_param(cr, SUPERUSER_ID, 'web_session.length')
            cr.close()
            if param and len(param.split(':')) > 1 and int(param.split(':')[1]) != 0:
                minutes = int(param.split(':')[1])
            if param and len(param.split(':')) != 0:
                hours = int(param.split(':')[0])
                if hours == 0:
                    hours = 1
        session_length = time.time() - 60*minutes*hours
        last_access_time = os.path.getatime(path)
        try:
            if last_access_time < session_length:
                os.unlink(path)
        except OSError:
            pass

openerp.http.session_gc = _new_session_gc

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: