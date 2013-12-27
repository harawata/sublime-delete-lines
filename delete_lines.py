import sublime, sublime_plugin

class DeleteLinesCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      if not region.empty():
        region = sublime.Region(region.begin(), region.end() - 1)
      lines = self.view.full_line(region)
      self.view.erase(edit, lines)
