# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LibraryBook(models.Model):
	_name = "library.book"
	
	name   		= fields.Char(string="Nombre")
	active 		= fields.Boolean("Es Activo")
	image  		= fields.Binary()
	pages 		= fields.Integer(string="# Pàginas")
	isbn   		= fields.Char(string="ISBN", size = 13)
	description = fields.Html(string="Descripción")
	category_id = fields.Many2one("library.category", string="Categoría ")
	


	
