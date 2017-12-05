# -*- coding: utf-8 -*-
from odoo import api, fields, models
class aplicaciones(models.Model):
    _name = 'aplicaciones'
    _rec_name ='nombre'
    foto_aplic = fields.Binary('Logo', help='coloque el logo que identifique la aplicación')

    nombre = fields.Char('Nombre del Aplicativo', size= 30, help='Ingrese el Nombre del Aplicativo ej: Movimiento de Personal Movilnet')

    descripcion = fields.Text('Descripción del Aplicativo', size=300)

    falla = fields.Text('Posible Fallas',size=300)

    descripcion_f = fields.Text('Afectación del Negocio', size=300)

    descripcion_i = fields.Text('Afectación de la Ingenería', size=300)

    arquitectura = fields.Binary('Arquitectura', help='Indique la arquitectura de la aplicación')

    bds_id = fields.One2many('bd.aplicacion', 'bd_id')

    descripcion_arq = fields.Html('Descripción')

    incidente_id = fields.One2many('incidencia.aplicacion', 'incidentes_id', string="Incidencia")

    equipos_id = fields.One2many('equipos', 'equipo_id')

    data_source_id = fields.One2many('data.s.aplicacion', 'data_s_id')

    data_mini_id = fields.One2many('data.min.aplicacion', 'data_min_id')

    data_maxi_id = fields.One2many('data.max.aplicacion', 'data_max_id')

    config_id = fields.One2many('conf.aplicacion', 'conf_id')
