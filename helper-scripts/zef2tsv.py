import xml.sax as sax
from sys import argv

class ZefanjaReader(sax.ContentHandler):
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
