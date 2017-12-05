# -*- coding: utf-8 -*-
from odoo import api, fields, models
class equipos(models.Model):
    """modelo de relación equipos S.O"""
    _name = 'equipos'
    _description="Equipos"
    _rec_name = 'equipo'
    equipo_id = fields.Many2one('aplicaciones')
    equipo = fields.Char(help="Ingrese el Nombre del Servidor Ej: CCS 24-7")
    ip_equipo = fields.Char('Dirección Ip', help="Ej: 192.168.1.2")
    ubicacion = fields.Char('Ubicación del Servidor', help="Ej: El Recreo")
    puerto_d = fields.Selection([('7777','7777')])
    puerto_h = fields.Selection([('7780','7780')])
    puerto_o = fields.Selection([('22-SSH/SFTP','22-SSH/SFTP'),
                                 ('23-SSH/SFTP','23-SSH/SFTP'),
                                 ('25-SSH/SFTP','25-SSH/SFTP'),
                                 ('22-SSH/SFTP/HTTPS 4443','22-SSH/SFTP/HTTPS 4443'),
                                 ('22-SSH/SFTP/HTTPS 443/5432','22-SSH/SFTP/HTTPS 443/5432')])
