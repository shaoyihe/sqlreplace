#coding=utf-8

import sublime, sublime_plugin
import re

class SqlReplaceCommand(sublime_plugin.TextCommand):
	"""
		sql前面 加""+ 方便放在代码中
	"""
	def replace_(self,content):
		# tet=max(map(lambda line : len(line), content.split("\n")))
		result=""
		com_=re.compile("^(.+)$",re.M)
		for cur in com_.finditer(content):
			result+='" '+cur.group(1)+' \\n"+\n'
		return result[:-2]+";"
	def run(self, edit):
		execute(self,edit)
		# self.view.insert(edit, 0, self.view.settings().get('syntax'))
		
class SqlReplaceReverseCommand(sublime_plugin.TextCommand):
	"""
		对上面操作取反
	"""
	def replace_(self,content):
		# tet=max(map(lambda line : len(line), content.split("\n")))
		result=""
		com_=re.compile(r'(^ *")*(.+)(\\n *?"[ ;+]*)+?$',re.M)
		for cur in com_.finditer(content):
			result+=cur.group(2)+"\n"
		return result
	def run(self, edit):
		execute(self,edit)


def execute(self, edit):
	self.view.set_syntax_file("Packages/SQL/SQL.tmLanguage")
	total_region=sublime.Region(0,self.view.size())
	new_content=self.replace_(self.view.substr(total_region))
	self.view.replace(edit,total_region,new_content)
	sublime.set_clipboard(new_content)