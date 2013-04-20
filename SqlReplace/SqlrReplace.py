#coding=utf-8

import sublime, sublime_plugin
import re


class SqlReplaceBase(sublime_plugin.TextCommand):
	"""
	"""
	def run(self, edit):
		self.view.set_syntax_file("Packages/SQL/SQL.tmLanguage")
		total_region=sublime.Region(0,self.view.size())
		new_content=self.replace_(self.view.substr(total_region))
		self.view.replace(edit,total_region,new_content)
		sublime.set_clipboard(new_content)
	
class SqlReplaceCommand(SqlReplaceBase):
	"""
		sql前面 加""+ 方便放在代码中
	"""
	def replace_(self,content):
		return "\n".join(map(lambda line: '" '+line+' "+' ,content.split("\n")))[:-1]+";"
	

class SqlReplaceReverseCommand(SqlReplaceBase):
	"""
		对上面操作取反 
	"""
	def replace_(self,content):
		return "\n".join(map(
			lambda line: re.sub(r'(^[ \t]*?"|([\\n "+]*[ \t]*$))','',line) ,content.split("\n")))


