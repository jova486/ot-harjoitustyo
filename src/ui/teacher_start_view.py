from tkinter import ttk, constants, StringVar


class TeacherStartView:
    def __init__(self, root, handle_show_teacher_main_view, sevice):
        self._root = root
        self.handle_show_teacher_main_view = handle_show_teacher_main_view
        self._frame = None
        self._sevice = sevice
        self.word_list_cb = None
        self.language_cb = None

        self._initialize_teacher_start_view()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _update_selected_list(self, language):
        if language == "Kaikki kielet":
            self.word_list_cb["values"] = self._sevice.get_wordlists_names()
            self.word_list_cb.current(0)

        else:
            self.word_list_cb["values"] = self._sevice.get_wordlists_by_language(
                language)
            self.word_list_cb.current(0)

    def _language_cb_modified(self, event):
        self._update_selected_list(self._selected_language.get())

    def _new(self):
        self._sevice.reset_active_wordlist()
        self.handle_show_teacher_main_view()

    def _open(self):
        """handle list"""
        self._sevice.open_active_wordlist(self._selected_list.get())
        self.handle_show_teacher_main_view()

    def _close(self):
        self._root.destroy()

    def _initialize_teacher_start_view(self):
        self._frame = ttk.Frame(master=self._root)
        new = ttk.Button(master=self._frame,
                         text="Uusi lista", command=self._new)
        self._selected_list = StringVar()
        self._selected_language = StringVar()
        lists = self._sevice.get_wordlist_info()
        names = []
        languages = []
        if len(lists) > 0:
            languages.append("Kaikki kielet")
            for row in lists:
                names.append(row[0])
                languages.append(row[1])
            open = ttk.Button(master=self._frame,
                              text="Muokkaa", command=self._open)
            open.grid(row=3, column=0, sticky=(
                constants.E, constants.W), padx=5, pady=5)
            close = ttk.Button(master=self._frame,
                               text="Lopeta", command=self._close)
            close.grid(row=4, column=0, sticky=(
                constants.E, constants.W), padx=5, pady=5)
        else:
            names.append("Ei vielä tehtäviä")
            languages.append("-")
            close = ttk.Button(master=self._frame,
                               text="Lopeta", command=self._close)
            close.grid(row=3, column=0, sticky=(
                constants.E, constants.W), padx=5, pady=5)

        self.word_list_cb = ttk.Combobox(
            master=self._frame, textvariable=self._selected_list, state='readonly'
        )
        new.grid(row=0, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self.word_list_cb["values"] = names
        self.word_list_cb.current(0)

        self.language_cb = ttk.Combobox(
            master=self._frame, textvariable=self._selected_language, state='readonly'
        )
        self.language_cb["values"] = languages
        self.language_cb.current(0)
        self.language_cb.bind('<<ComboboxSelected>>',
                              self._language_cb_modified)

        self.word_list_cb.grid(
            row=1, column=0, sticky=(constants.E, constants.W), padx=5, pady=5
        )
        self.language_cb.grid(
            row=2, column=0, sticky=(constants.E, constants.W), padx=5, pady=5
        )
