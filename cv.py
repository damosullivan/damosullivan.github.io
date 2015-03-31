class Education(object):
	def bsc_computer_science(self):
		self.college = "University College Cork, Co. Cork, Ireland"
		self.years = range(2009, 2014)
		self.result = 1.1

	def leaving_certificate(self):
		self.result = 410


class TechnicalProficiency(object):
	def languages(self, new_language_to_learn=None):
		self.languages_used = [
			"Python",
			"Java",
			"php",
			"Haskell",
			"Perl",
			"JavaScript",
			"Bash",
			"HTML + CSS",
		]
		if new_language_to_learn:
			self.languages_used.append(new_language_to_learn)

	def operating_systems(self):
		self.operating_systems_used = [
			"Windows",
			"Mac OSX",
			"Linux",
		]

	def applications(self):
		self.applications_used = [
			"Microsoft Office (full suite)",
			"Google services",
			"Eclipse",
			"Terminal",
			"git (github)",
			"VIM",
			"Adobe Premier",
			"Photoshop",
			"many more".
		]
