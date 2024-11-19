# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo  import fields, models,api

class Task_Master(models.Model):
    _name = 'task.master'

    name = fields.Char(string='Task Name',required=True)
    task_description = fields.Text(string='Task Description')
    associated_project = fields.Many2one(comodel_name='project.master',string='Project list')
    timesheet_line_ids = fields.One2many('timesheet.line','task_id',string="Timesheet Line")
    task_status = fields.Selection(
        selection=[
            ('notstarted', "Not started"),
            ('progress', "Progress"),
            ('done', "Done")
        ],
        string="Status",default='notstarted',required=True)


class Timesheet_line(models.Model):
    _name = 'timesheet.line'

    date = fields.Date(string='Date')
    description = fields.Text(string='Work Description')
    time = fields.Datetime(string='Time')
    task_id= fields.Many2one('task.master', string = "Task")








