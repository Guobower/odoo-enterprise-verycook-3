# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
    'name': 'POB Extension: Multi Shop',
	'sequence': 1,
	'summary':'MultiShop Extension for POB',
    'version': '2.1',
    'category': 'A Module of WEBKUL Software Pvt Ltd.',
    'description': """	
    Odoo Prestashop Bridge This Brilliant Module will Connect Odoo with Prestashop and synchronise all shopes from prestashop to Odoo.
	
	>>> In order to use this module you have to install our Previous module named as Prestashop Bridge. <<<
	
	This module works very well with latest version of prestashop 1.7.x.x and latest version of Odoo 11.
    """,
    'author': 'Webkul Software Pvt Ltd.',
    'depends': ['pob'],
    'website': 'http://www.webkul.com',
    'data': ['security/ir.model.access.csv','views/pob_multishop_view.xml'],
    'installable': True,
    'active': False,
    #'certificate': '0084849360985',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
