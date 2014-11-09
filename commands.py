import sublime
import sublime_plugin

class DelayedSaveAll(sublime_plugin.TextCommand):
  def __init__(self, view):
    super().__init__(view)
    self.timeout = 300

  def run(self, edit):
    self.views = []
    for view in self.view.window().views():
      self.views.append(view)

    self._set_timeout()

  def _set_timeout(self):
    if len(self.views) == 0:
      return

    view = self.views.pop(0)
    view.run_command('save')
    sublime.set_timeout(self._set_timeout, self.timeout)