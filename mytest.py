# coding: utf-8
class Date :
	word = 'date : '

	def __init__(self, date):
		self.date = self.word + date

	@classmethod      ####
	def now(cls):
		return cls("today")

	def show(self):
		print(self.date)

class KoreanDate(Date):
	word = '날짜 : '

a = KoreanDate.now()
a.show()
