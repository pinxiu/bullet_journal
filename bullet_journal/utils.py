from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals

from datetime import date

def today():
	return date.today().strftime("%Y_%m_%d")
