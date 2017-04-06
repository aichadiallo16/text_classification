#! /usr/bin/env python3

import nltk
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine

def openPdf(name):
	f = open(name, 'rb')
	parser = PDFParser(f)
	doc = PDFDocument()
	parser.set_document(doc)
	doc.set_parser(parser)
	doc.initialize('')
	rsrcmgr = PDFResourceManager()
	laparams = LAParams()
	device = PDFPageAggregator(rsrcmgr, laparams=laparams)
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	# Process each page contained in the document.
	for page in doc.get_pages():
		interpreter.process_page(page)
		layout = device.get_result()
		for lt_obj in layout:
			if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
				#print(lt_obj.get_text())
				return lt_obj.get_text()


#extraction du texte à partir du pdf
raw = openPdf('file.pdf')
#decoupe en phrases

tokenizerp = nltk.data.load('tokenizers/punkt/PY3/french.pickle')
tokens = tokenizerp.tokenize(raw)
for line in tokens:
	
	print(line)
print('================================')

#decoupe en mots et élimination des stopwords
from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()

from nltk.corpus import stopwords

french_stopwords = set(stopwords.words('french'))

for line in tokens:
	tokens = tokenizer.tokenize(line)
	tokenf = [token for token in tokens if token.lower() not in french_stopwords]

	print (tokenf)









