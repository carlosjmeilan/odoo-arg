
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class correo_crm(models.Model):

     _inherit = 'crm.lead'
     correo_enviado = fields.Boolean(string='email enviado')

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


          email_to = values ['email_from']

          body = '<![CDATA[
	             <p>Dear ${(object.name)},<br/><br/>
	             Good job, you've just created your first e-mail template!<br/></p>
                 Regards,<br/>
                ${(object.company_id.name)}
	             ]]>'

          mail_values = {
             'subject' : 'gracias por comunicarse con nosotros',
             'body_html': boby,
             'email_to': email_to,
             'email_from':'admin@gestiongma.com'
              }

          self.env['mail.mail'].sudo().create(mail_values).send()


          return record
