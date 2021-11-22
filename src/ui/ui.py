from ui.login_view import LoginView
from ui.new_user_view import NewUserView
from ui.teacher_main_view import TeacherMainView

from app_logic.wordList_service import (
    word_list_Service as service
)


class UI:
    """Luokka joka vastaa käyttöliittynän logiikasta"""
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._service = service

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None


    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(self._root, self._show_teacher_main_view,self._show_new_user_view, self._service)

        self._current_view.pack()
    
    def _show_new_user_view(self):
        self._hide_current_view()

        self._current_view = NewUserView(self._root, self._show_teacher_main_view, self._service)

        self._current_view.pack()

    def _show_teacher_main_view(self):
        self._hide_current_view()

        self._current_view = TeacherMainView(self._root, self._show_login_view,self._service)

        self._current_view.pack()

    