import sublime, sublime_plugin
import socket

class ExtemporeConnection:
	hostname = 'localhost'
	port = 7099
	s = None

class ExtemporeConnectCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		try:
			ExtemporeConnection.s = socket.socket(AF_INET, SOCK_STREAM)
			ExtemporeConnection.s.settimeout(5)
			ExtemporeConnection.s.connect((ExtemporeConnection.hostname, ExtemporeConnection.port))
			data = ExtemporeConnection.s.recv(1024)
			sublime.status_message(data)
		except socket.error, e:
			return None

class ExtemporeSendCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for sel in self.view.sel():
			theCode = self.view.substr(sel)

			try:
				ExtemporeConnection.s.send(theCode)
				data = ExtemporeConnection.s.recv(1024)
				sublime.status_message(data)
			except socket.error, e:
				sublime.status_message(e)

		self.view.sel().clear()
