from odoo import models,fields


class MyModuleModel(models.Model):
    _name = 'my_module.model'
    _description = 'my module'

    name = fields.Char(string="Name",required=True,default=lambda self: self.env.user.name)
    email = fields.Char(string="Email",required=True,default=lambda self: self.env.user.email)