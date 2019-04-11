class MapInfo:
	def __init__(self):
		self.info = {
			"-E0" : ("-E1", "", ""),
			"-E1" : ("-E4", "-E3", ""),
			"-E10" : ("E9", "E11", ""),
			"-E11" : ("E10", "E9", ""),
			"-E12" : ("-E11", "", ""),
			"-E13" : ("-E12", "-E17", ""),
			"-E14" : ("-E13", "E15", "E25"),
			"-E15" : ("E25", "E14", "-E13"),
			"-E16" : ("E19", "-E27", ""),
			"-E17" : ("-E18", "-E16", ""),
			"-E18" : ("-E20", "-E19", ""),
			"-E19" : ("-E27", "E16", ""),
			"-E2" : ("E3", "-E25", ""),
			"-E21" : ("-E22", "", ""),
			"-E22" : ("-E0", "-E2", ""),
			"-E23" : ("-E5", "E7", ""),
			"-E24" : ("-E7", "-E8", ""),
			"-E25" : ("E14", "-E13", "E15"),
			"-E26" : ("E6", "-E23", ""),
			"-E28" : ("E20", "-E21", ""),
			"-E3" : ("-E25", "E2", ""),
			"E20" : ("-E19", "E18", ""),
			"-E4" : ("-E5", "-E6", ""),
			"-E5" : ("E7", "E23", ""),
			"-E6" : ("-E23", "E26", ""),
			"-E7" : ("E23", "E5", ""),
			"-E8" : ("-E9", "", ""),
			"-E9" : ("E11", "E10", ""),
			"E0" : ("-E2", "E22", ""),
			"E1" : ("E0", "", ""),
			"E10" : ("-E14", "-E26", "-E24"),
			"E11" : ("E12", "", ""),
			"E12" : ("-E17", "E13", ""),
			"E13" : ("E15", "E25", "E14"),
			"E14" : ("-E26", "-E24", "-E10"),
			"E15" : ("E25", "E14", "-E13"),
			"E16" : ("E17", "-E18", ""),
			"E17" : ("E13", "-E12", ""),
			"E18" : ("-E16", "E17", ""),
			"E19" : ("E18", "-E20", ""),
			"E2" : ("E22", "-E0", ""),
			#"E20" : ("E22", "-E0", ""),
			"E21" : ("E28", "E20", ""),
			"E22" : ("E21", "", ""),
			"E23" : ("E26", "E6", ""),
			"E24" : ("-E10", "-E14", "-E26"),
			"E25" : ("E2", "E3", ""),
			"E26" : ("-E24", "-E10", "-E14"),
			"E28" : ("-E15", "E27", ""),
			"E3" : ("E1", "-E4", ""),
			"-E20" : ("-E21", "E28", ""),
			"E4" : ("-E3", "E1", ""),
			"E5" : ("-E6", "E4", ""),
			"E6" : ("E4", "-E5", ""),
			"E7" : ("-E8", "E24", ""),
			"E8" : ("E24", "-E7", ""),
			"E9" : ("E8", "", ""),
			"E27" : ("E16", "E19", ""),
			"-E27" : ("-E28", "-E15", "")
			
		
		
		}

		
		
	def set_Pnd_At(self, id, value):
		self.Ponderation[id] = value
