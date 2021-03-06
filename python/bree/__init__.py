# bree
# determines whether I am bree on any given date
from calendar import isleap

__all__ = ("is_bree",)

def is_bree(d):
	"""Returns whether I am bree on the given date"""
	return d.weekday() == 4 and\
	  d.day - 7 > 0 and\
	  d.day - 14 <= 0 and\
	  (d.month != 3 or not isleap(d.year)) and\
	  (d.month != 7 or d.year != 2023)