import sublime, sublime_plugin
from socket import *


class ExtemporeConnection:
	hostname = 'localhost'
	port = 7099
	s = None

class ExtemporeConnectCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		ExtemporeConnection.s = socket(AF_INET, SOCK_STREAM)
		ExtemporeConnection.s.connect((ExtemporeConnection.hostname, ExtemporeConnection.port))

class ExtemporeSendCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#for sel in self.view.sel():
		#	theString = self.view.substr(sel)
		ExtemporeConnection.s.send('(define a (lambda (x) (+ x x)))')
		data = ExtemporeConnection.s.recv(1024)

			#print repr(data)
		sublime.error_message(data)

		self.view.sel().clear()
