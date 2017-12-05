# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Solución ERP de código abierto
#
#    Este programa es software libre: se puede redistribuir y / o modificar
#    bajo los términos de la GNU Affero General Public License
#
#    Debería haber recibido una copia de la Licencia Pública General GNU Affero
#    Junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generado por el plugin Odoo V10 para Dia!
{
    'name': 'SAIM',
    'version': '1.1',
    'author': 'Pasantes Movilnet 2017: Castillo Jonnathan, Olivares Jesús, Mendoza Keivin, Olivares Oliver',
    'website': 'Sin Pagina Web',
    'images': ['aplicaciones/static/description/SAIM.png'],
    'category': 'Buscador',
    'sequence': 15,
    'summary': 'Desconocida',
    'description': """ Modulo de Aplicaciones de Movilnet """,
    'depends': ['base'],
    'data': [

        'security/ir.model.access.csv',
        'views/aplicaciones_view.xml',
        'views/incidencia_view.xml',
        'views/bd_view.xml',
        'views/equipos_view.xml',
        'views/login_inherit.xml',
        'views/login_layout.xml',
        'views/web_layout_inherit.xml',
        'data/equipo.xml',
        'data/descripcion_bd.xml',
        'data/datos_configuracion_bd.xml'
    ],
    'demo': [ ],
    'css': ['static/src/css/aplicaciones.css'],
    'update_xml': [ ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
