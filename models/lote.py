from odoo import models, fields, api

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

  comunidades = fields.Many2many('coop2.asociacion', string="Comunidades")

  observaciones = fields.Text(string="Observaciones")

  def cerrar(self):
    self.estado = "cerrado"
    print("Cerrado")
  def enviar(self):
    self.estado = "enviado"
    print("Enviado")