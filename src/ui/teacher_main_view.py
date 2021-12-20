from tkinter import ttk, constants, messagebox


class TeacherMainView:
    def __init__(self, root, handle_show_teacher_start_view, sevice):
        self._root = root
        self._to_main_view = handle_show_teacher_start_view
        self._frame = None
        self._listname_entry = None
        self._word_entry = None
        self._translate_entry = None
        self._word_list_index = 0
        self._sevice = sevice
        self.wordlist = sevice.get_wordlist()
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def clear(self):

        name = self._listname_entry_entry.get()
        language = self._language_entry_entry.get()
        word = self._word_entry.get()
        translation = self._translate_entry.get()
        self._listname_entry_entry.delete(0, len(name))
        self._language_entry_entry.delete(0, len(language))
        self._word_entry.delete(0, len(word))
        self._translate_entry.delete(0, len(translation))
        self._word_list_index = 0
        self._sevice.reset_active_wordlist()
        self.wordlist = self._sevice.get_wordlist()

    def _save(self):
        word = self._word_entry.get()
        translation = self._translate_entry.get()
        if (len(word) > 0) and (len(translation) > 0):
            self._sevice.save_to_wordlist(
                word, translation, self._word_list_index)

            self._word_entry.delete(0, len(word))
            self._translate_entry.delete(0, len(translation))
            self._word_list_index += 1
        else:
            messagebox.showerror(
                title="Huom!", message="Sana tai käännös puuttuu")

    def _save_list(self):
        name = self._listname_entry_entry.get()
        language = self._language_entry_entry.get()

        if (len(name) > 0) and (len(language) > 0):
            if self._sevice.check_word_list_name(name):
                messagebox.showerror(
                    title="Virhe", message="sanalistan nimi on jo käytössä")
            else:
                if self._sevice.save_wordlist(name, language) == True:
                    messagebox.showinfo(title="Tallennettu",
                                        message="Sanalista "+name + " on tallennettu")
                    self.clear()

                else:
                    messagebox.showerror(
                        "Lisää sanoja", "Sanalista ei voi olla tyhä")

        else:
            messagebox.showerror(
                "Virhe", "Anna sanalistalle sekä nimi että kieli")

    def _back(self):
        if self._word_list_index == 0:
            return

        self._word_list_index -= 1
        word = self._word_entry.get()
        translation = self._translate_entry.get()

        self._word_entry.delete(0, len(word))
        self._translate_entry.delete(0, len(translation))

        self._word_entry.insert(0, self.wordlist[self._word_list_index][0])
        self._translate_entry.insert(
            0, self.wordlist[self._word_list_index][1])

    def _forward(self):
        if self._word_list_index >= len(self.wordlist) - 1:
            self._word_list_index = len(self.wordlist)
            word = self._word_entry.get()
            translation = self._translate_entry.get()
            self._word_entry.delete(0, len(word))
            self._translate_entry.delete(0, len(translation))
        else:
            self._word_list_index += 1
            word = self._word_entry.get()
            translation = self._translate_entry.get()
            self._word_entry.delete(0, len(word))
            self._translate_entry.delete(0, len(translation))
            self._word_entry.insert(0, self.wordlist[self._word_list_index][0])
            self._translate_entry.insert(
                0, self.wordlist[self._word_list_index][1])

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        listname_label = ttk.Label(
            master=self._frame, text="Sanalistan nimi")
        self._listname_entry_entry = ttk.Entry(master=self._frame)

        language_label = ttk.Label(
            master=self._frame, text="Sanalistan kieli")
        self._language_entry_entry = ttk.Entry(master=self._frame)

        word_label = ttk.Label(master=self._frame, text="Sana")
        self._word_entry = ttk.Entry(master=self._frame)

        translate_label = ttk.Label(master=self._frame, text="Käännös")
        self._translate_entry = ttk.Entry(master=self._frame)

        back_arrow = ttk.Button(
            master=self._frame, text="<=", command=self._back)

        forward_arrow = ttk.Button(
            master=self._frame, text="=>", command=self._forward)

        save_word = ttk.Button(
            master=self._frame, text="Tallenna sana ja käännös", command=self._save)

        save_list = ttk.Button(
            master=self._frame, text="Tallenna sanalista", command=self._save_list
        )

        back = ttk.Button(master=self._frame, text="Alkuun",
                          command=self._to_main_view)

        listname_label.grid(padx=5, pady=5)
        self._listname_entry_entry.grid(
            row=0, column=1, sticky=(constants.E, constants.W), padx=5, pady=5
        )

        language_label.grid(padx=5, pady=5)
        self._language_entry_entry.grid(
            row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5
        )

        word_label.grid(padx=5, pady=5)
        self._word_entry.grid(
            row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5
        )

        translate_label.grid(padx=5, pady=5)
        self._translate_entry.grid(
            row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5
        )

        back_arrow.grid(
            row=4, column=0, sticky=(constants.E, constants.W), padx=5, pady=5
        )
        forward_arrow.grid(
            row=4, column=1, sticky=(constants.E, constants.W), padx=5, pady=5
        )

        save_word.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        save_list.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        back.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        if len(self.wordlist) > 0:
            self._word_list_index = 0
            self._listname_entry_entry.insert(
                0, self._sevice.get_wordlist_name())
            self._language_entry_entry.insert(
                0, self._sevice.get_wordlist_language())

            self._word_entry.insert(0, self.wordlist[self._word_list_index][0])
            self._translate_entry.insert(
                0, self.wordlist[self._word_list_index][1])
