# -*- coding: utf-8 -*-

from odoo import api,fields,models


class ToDO(models.Model):
    _name = "todo.model"
    _description = "todo.task to represent tasks in the to-do list"

    #fields of my model
    name=fields.Char(string="Task Name ", required=True, tracking=True)
    partner_id = fields.Many2one('res.partner', string='Assign To', required=True, tracking=True)
    description = fields.Text(string='Description', tracking=True)
    date =fields.Datetime(string="Due Date", tracking=True)
    status=fields.Selection([
        ('new', 'New'),
        ('inprogress', 'In Progress'),
        ('completed', 'Completed')
    ],  tracking=True)

