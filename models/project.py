# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo  import fields, models,api

class Project_Master(models.Model):
    _name = 'project.master'

    name = fields.Char(string='Project Name',required=True)
    project_description = fields.Text(string='Project Description')
    associated_tasks = fields.One2many('task.master','associated_project','Task List')








