# -*- coding: cp1251 -*-

from simpletk import *

class TIntEdit(TEdit):
	def __init__(self, parent, **kw):
		TEdit.__init__(self, parent, **kw)
		self.__value = 0
		self.onValidate = self.__validate

	def __setValue(self, value):
		self.text = str(value)

	def __validate(self):
		try:
			self.__value = int(self.text)
			return True
		except:
			return False

	value = property(lambda x: x.__value, __setValue)

class THexIntEdit(TEdit):
	def __init__(self, parent, **kw):
		TEdit.__init__(self, parent, **kw)
		self.__value = '0'
		self.onValidate = self.__validate

	def __setValue(self, value):
		self.text = str(value)

	def __validate(self):
		text = self.text.lower()
		for s in text:
			if not (s in '1234567890abcdef'):
				return False

		self.__value = text
		return True

	value = property(lambda x: x.__value, __setValue)