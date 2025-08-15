from odoo import models, fields

class BookTracker(models.Model):
    _name = 'book.tracker'
    _description = 'Book Tracker'

    name = fields.Char(string='Title')
    author = fields.Char(string='Author')
    is_read = fields.Boolean(string='Read')  # renamed from 'read' to 'is_read'
