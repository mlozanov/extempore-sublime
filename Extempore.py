import sublime, sublime_plugin
import socket

class ExtemporeConnection:
	hostname = 'localhost'
	port = 7099
	s = None

class ExtemporeConnectCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		try:
			ExtemporeConnection.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			ExtemporeConnection.s.settimeout(5)
			ExtemporeConnection.s.connect((ExtemporeConnection.hostname, ExtemporeConnection.port))
			data = ExtemporeConnection.s.recv(1024)
			sublime.status_message(data)
		except socket.error, e:
			return None

class ExtemporeDisconnectCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		try:
			ExtemporeConnection.s.close()
		except socket.error, e:
			print repr(e)

class ExtemporeEvaluateCommand(sublime_plugin.TextCommand):
	def __init__(self, view):
		sublime_plugin.TextCommand.__init__(self, view)

	def send(self, sock, string):

		count = sock.send(string + '\r\n')
		return sock.recv(512)
		
	def run(self, edit):			
		sels = self.view.sel()
		sock = ExtemporeConnection.s

		if not sock:
			print 'trying to connect'
			self.view.run_command('extempore_connect')
			sock = ExtemporeConnection.s

		if sock:
			for sel in sels:
				string = self.view.substr(sel)
				if len(string) > 0:
					try:
						response = self.send(sock,string)
						sublime.status_message(response)
						self.view.sel().clear()
					except Exception, e:
						sublime.status_message('no response')
		else:
			sublime.error_message('not sock')

