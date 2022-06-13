import xml.sax as sax
from sys import argv

class ZefanjaReader(sax.ContentHandler):
	books = [
		("1 Mo","Genesis"),
		("2 Mo","Exodus"),
		("3 Mo","Leviticus"),
		("4 Mo","Numeri"),
		("5 Mo","Deuteronomium"),
		("Jos","Joshua"),
		("Ri","Richter"),
		("Ruth","Ruth"),
		("1 Sam","1 Samuel"),
		("2 Sam","2 Samuel"),
		("1 Kng","1 Könige"),
		("2 Kng","2 Könige"),
		("1 Chr","1 Chroniken"),
		("2 Chr","2 Chroniken"),
		("Esra","Esra"),
		("Neh","Nehemia"),
		("Est","Esther"),
		("Hiob","Hiob"),
		("Ps","Psalme"),
		("Spr","Sprüche"),
		("Pred","Prediger"),
		("Hld","Hohelieder"),
		("Jes","Jesaja"),
		("Jer","Jeremiah"),
		("Kla","Klagelieder"),
		("Hes","Hesekiel"),
		("Dan","Daniel"),
		("Hos","Hosea"),
		("Joel","Joel"),
		("Amos","Amos"),
		("Obd","Obadja"),
		("Jona","Jona"),
		("Mi","Micha"),
		("Nah","Nahum"),
		("Hab","Habakuk"),
		("Zef","Zefanja"),
		("Hag","Haggai"),
		("Sach","Sacharja"),
		("Mal","Maleachi"),
		("Mt","Matthäus"),
		("Mk","Markus"),
		("Lk","Lukas"),
		("Joh","Johannes"),
		("Apg","Apostelgeschichte"),
		("Rom","Römer"),
		("1 Kor","1 Korinther"),
		("2 Kor","2 Korinther"),
		("Gal","Galater"),
		("Eph","Epheser"),
		("Phi","Philipper"),
		("Kol","Kolosser"),
		("1 Thess","1 Thessalonicher"),
		("2 Thess","2 Thessalonicher"),
		("1 Tim","1 Timotheus"),
		("2 Tim","2 Timotheus"),
		("Tit","Titus"),
		("Phlm","Philemon"),
		("Hebr","Hebräer"),
		("Jak","Jakobus"),
		("1 Pt","1 Petrus"),
		("2 Pt","2 Petrus"),
		("1 Jo","1 Johannes"),
		("2 Jo","2 Johannes"),
		("3 Jo","3 Johannes"),
		("Jud","Judas"),
		("Offb","Offenbarung")
	]
	def __init__(self):
		self.current_book = 0
		self.current_bname = ""
		self.current_bsname = ""
		self.current_chapter = 1
		self.current_line = ""
	def startElement(self,name,attr):
		if name=="BIBLEBOOK":
			self.current_book = int(attr["bnumber"])
			self.current_bname = attr["bname"]
			self.current_bsname = attr["bsname"]
		elif name=="CHAPTER":
			self.current_chapter = int(attr["cnumber"])
		elif name=="VERS":
			self.current_line = (self.current_bname+"\t"+self.current_bsname+"\t"+str(self.current_book)+"\t"+str(self.current_chapter)+"\t"+attr["vnumber"]+"\t")
		else:
			pass
	def endElement(self,name):
		if name=="VERS":
			print(self.current_line)
		else:
			pass
	def characters(self,content):
		self.current_line += content



if __name__ == "__main__":
	parser = sax.make_parser()
	handler = ZefanjaReader()
	parser.setContentHandler(handler)
	if(len(argv)<2):
		quit("Parse what?")
	try:
		parser.parse(argv[1])
	except ValueError:
		raise OSError(404,"File not Found")
	pass
