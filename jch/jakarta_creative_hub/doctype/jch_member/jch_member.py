# -*- coding: utf-8 -*-
# Copyright (c) 2018, MGBoy and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import utils

class JCHMember(Document):
	utils.now()
	utils.today()
	def autoname(doc):
		query = frappe.db.sql("""SELECT MAX(SUBSTRING(name,10,5)) as maxID FROM `tabJCH Member`""")
		query1 = str(query)
		if query1 == "((None,),)":
			query2 = '{:05d}'.format(1)
			doc.name = (doc.series + doc.kode_domisili_ktp + doc.kota_kabupaten + str(query2))
		else:
			query3 = query1[4:9]
			query4 = int(query3) + 1
			query5 = '{:05d}'.format(query4)
			doc.name = (doc.series + doc.kode_domisili_ktp + doc.kota_kabupaten + str(query5))
