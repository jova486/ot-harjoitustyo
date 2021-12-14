from tkinter import ttk, constants, StringVar, messagebox


class StudentMainView:
    def __init__(self, root, _to_main_view, _to_exercise_view, sevice):
        self._root = root
        self._to_main_view = _to_main_view
        self._to_exercise_view = _to_exercise_view
        self._frame = None
        self._sevice = sevice
        self.word_list_cb = None
        self.language_cb = None
        self._selected_list = None
        self._selected_language = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _open(self):
        """handle list"""
        self._sevice.open_active_wordlist(
            self._selected_list.get(), self._selected_language.get())
        self._to_exercise_view()

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

    def _close(self):
        self._root.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._selected_list = StringVar()
        self._selected_language = StringVar()
        lists = self._sevice.get_wordlist_info()
        names = []
        languages = []
        if len(lists) > 0:
            languages.append("Kaikki kielet")
            for row in lists:
                names.append(row[0])
                if row[1] not in languages:
                    languages.append(row[1])
            open = ttk.Button(master=self._frame,
                              text="Avaa", command=self._open)
            open.grid(row=2, column=0, sticky=(
                constants.E, constants.W), padx=5, pady=5)
            close = ttk.Button(master=self._frame,
                               text="Lopeta", command=self._close)
            close.grid(row=3, column=0, sticky=(
                constants.E, constants.W), padx=5, pady=5)
        else:
            names.append("Ei vielä tehtäviä")
            languages.append("-----")
            close = ttk.Button(master=self._frame,
                               text="Lopeta", command=self._close)
            close.grid(row=3, column=0, sticky=(
                constants.E, constants.W), padx=5, pady=5)

        self.word_list_cb = ttk.Combobox(
            master=self._frame, textvariable=self._selected_list, state='readonly'
        )
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
            row=0, column=0, sticky=(constants.E, constants.W), padx=5, pady=5
        )
        self.language_cb.grid(
            row=1, column=0, sticky=(constants.E, constants.W), padx=5, pady=5
        )
