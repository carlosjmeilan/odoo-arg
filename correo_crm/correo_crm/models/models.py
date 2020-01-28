
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class correo_crm(models.Model):

     _inherit = 'crm.lead'
     correo_enviado = fields.Boolean(string='flag to email')

     def automata(self):
          mail_values = {
              'subject' : 'CVS',
              'body_html' : 'CVS',
              'email_to':'carlosjmeilan@gmail.com',
              'email_from':'admin@gestiongma.com'
          }
          self.env['mail.mail'].sudo().create(mail_values).send()


     @api.multi
     def create(self, values):
          record = super(correo_crm, self).create(values)
          record['correo_enviado'] = True

          mail_values = {
              'subject' : 'CVS',
              'body_html' : 'CVS',
              'email_to':'carlosjmeilan@yahoo.com.ar',
              'email_from':'admin@gestiongma.com'
          }
          self.env['mail.mail'].sudo().create(mail_values).send()
          return record


#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
