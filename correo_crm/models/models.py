
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class correo_crm(models.Model):

     _inherit = 'crm.lead'
     correo_enviado = fields.Boolean(string='email enviado')

     @api.multi
     def create(self, values,):
          record = super(correo_crm, self).create(values)
          record['correo_enviado'] = True


          email_to = values ['email_from']
          name = values ['contact_name']
          company_id = self.env['res.company'].search([('id','=', 1)])
          company = company_id ['name']
          email_from = company_id['email']

          mail_values = {
             'subject' : 'Gracias por comunicarse con nosotros',
             'body_html': '<p>Estimado ' + name + ', ' + 'gracias por comunicarse con nosotros </p> </br> </br>' + 'El equipo de ventas de  </br>' +  company,
             'email_to': email_to,
             'email_from':email_from
          }

          self.env['mail.mail'].sudo().create(mail_values).send()

#          template = self.env.ref('auth_signup.mail_template_user_signup_account_created')
#          template_id = template.id
#          self.env['mail.template'].browse(template_id).send_mail(self.id)


          return record