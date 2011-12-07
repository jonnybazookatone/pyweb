#!/usr/bin/python

Usage = """Website class to allow automation of webpage making. Simple html based."""

import subprocess
import urllib2 as urllib

__author__ = "Jonny Elliott"
__copyright__ = "Copyright 2011"
__credits__ =  ""
__license__ = "GPL"
__version__ = "0.0"
__maintainer__ = "Jonny Elliott"
__email__ = "jonnyelliott@mpe.mpg.de"
__status__ = "Prototype"

class webpage(object):

	def __init__(self, title=""):
		self._title = title
		self._html = ""
		self._header = ""
		self._body = ""

        def setTitle(self, title):
                self._title = title

	def addBody(self, body, link=False):
		if link:
			_body = "<a href=%s>%s</a>" % (body, body)
		else:
			_body = "<p>%s</p>" % (body)

		if self._body == "":
			self._body = [_body]
		else:
			self._body.append(_body)
	
	def buildPage(self, outname):
		# open file
		webout = open(outname, "w")
		
		# Write the standard html format
		webout.write("<html>")
		webout.write("	<title> %s </title>" % self._title)
		webout.write("	<body")
		for body in self._body:
			webout.write("	%s" % body)
		webout.write("	</body>")
		webout.write("</html>")
		
		# close file
		webout.close()

class CopiedWebPage(webpage):
	
	# Initiatilsation will inherit properties of webpage
	def __init__(self):
		self._content = []
		self._filename = ""

	# Following style of C++
	def getContent(self):
		return self._content
	def setFileName(self, filename):
		self._filename = filename
	def getFileName(self):
		return self._filename

	# Download the webpage using the wget protocol and Popen
	def getWebPage(self, url=""):
	
		try:
			tmp = open(self.getFileName(), "r")
			returnFlag = False
			tmp.close()
		except:	
			req = urllib.Request(url)
			try:
				download = urllib.urlopen(req)

				webwrite = open(self.getFileName(), "w")
				webwrite.write(download.read())
				webwrite.close()
				returnFlag = True

			# Handle errors
			except urllib.HTTPError, e:
				print "HTTP Error:",e.code , url
				returnFlag = False

			except urllib.URLError, e:
				print "URL Error:",e.reason , url
				returnFlag = False

		return returnFlag

	# Parse the webpage into body/title etc based on the webpage class
	def parseWebPage(self):
		
		# Open web page
		rrmhawkifile = open(self.getFileName(), "r")
		rrmhawki = rrmhawkifile.readlines()
		rrmhawkifile.close()
		#
		# Parse file (TBC)
		#
		self._content = rrmhawki
		
	
if __name__ == "__main__":

	print Usage
