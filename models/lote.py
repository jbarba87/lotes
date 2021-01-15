from odoo import models, fields, api
from datetime import datetime

class lote(models.Model):
  _name = 'lote.lote'

  name = fields.Char(string="Nombre")
  estado = fields.Selection([
    ('abierto', 'abierto'),
    ('cerrado', 'cerrado'),
    ('enviado', 'enviado'),

    ], default='abierto', string="Estado")
  
  #fecha_inicio = fields.Date(string="Fecha de apertura") Fecha de inicio no es necesaria ya que hay "create_date"

  fecha_cierre = fields.Date(string="Fecha de cierre")

  fecha_envio = fields.Date(string="Fecha de envio")

  comunidades = fields.Many2many('coop.asociacion', string="Comunidades")

  observaciones = fields.Text(string="Observaciones")

  def cerrar(self):
    # Si fecha de cierre esta vacio colocar fecha actual
    if self.fecha_cierre is not set:
      self.fecha_cierre = datetime.today().strftime('%Y-%m-%d')
    self.estado = "cerrado"
    print("Cerrado")
  def enviar(self):
    # Si fecha de cierre esta vacio colocar fecha actual
    if self.fecha_envio is not set:
      self.fecha_envio = datetime.today().strftime('%Y-%m-%d')
    self.estado = "enviado"
    print("Enviado")