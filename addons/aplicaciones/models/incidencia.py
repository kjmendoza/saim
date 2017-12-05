# -*- coding: utf-8 -*-

from odoo import api, fields, models
class incidencia_aplicacion(models.Model):
    """modelo para relación One2many"""
    _name = 'incidencia.aplicacion'
    incidentes_id = fields.Many2one('aplicaciones', 'Aplicaciones')
    descripcion_inc = fields.Char('Descripción', size=100)
    fecha_inc = fields.Date('Fecha')
    usuario_inc = fields.Char('Usuario')
    gerencia_inc = fields.Char('Gerencia')
    archivo_inc = fields.Binary('Ticket')
    archivo_name = fields.Char('Nombre del Ticket', size= 500)
