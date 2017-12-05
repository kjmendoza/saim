# -*- coding: utf-8 -*-
from odoo import api, fields, models
class bd_aplicacion(models.Model):
    """Modelo para realizar relación de One2many con el modelo de aplicaciones"""
    _name = 'bd.aplicacion'
    _rec_name = 'nombre_bd'
    bd_id = fields.Many2one('aplicaciones', 'Aplicaciones')
    nombre_bd = fields.Char('Nombre')
    ip_bd = fields.Char('Ip')
    descripcion_d = fields.Text('Descripción', size=100)

class data_s_aplicacion(models.Model):
    """Modelo Relacionado para llevar la data de DATA SOURCE a el model de aplicaciones"""
    _name = 'data.s.aplicacion'
    _rec_name = 'data_s'
    data_s_id = fields.Many2one('aplicaciones')
    data_s = fields.Char('Data Source', size=100)

class data_min_aplicacion(models.Model):
    """Modelo Relacionado para llevar la data de DATA MIN a el model de aplicaciones"""
    _name = 'data.min.aplicacion'
    _rec_name = 'data_min'
    data_min_id = fields.Many2one('aplicaciones')
    data_min = fields.Integer('MIN', size=2)

class data_max_aplicacion(models.Model):
        """Modelo Relacionado para llevar la data de DATA MAX a el model de aplicaciones"""
        _name = 'data.max.aplicacion'
        _rec_name = 'data_max'
        data_max_id = fields.Many2one('aplicaciones')
        data_max = fields.Integer('MAX', size=3)

class conf_aplicacion(models.Model):
        """Modelo Relacionado para llevar la data de Configuración a el model de aplicaciones"""
        _name = 'conf.aplicacion'
        _rec_name = 'configuracion'
        conf_id = fields.Many2one('aplicaciones')
        configuracion = fields.Char('Configuración', size=100)
