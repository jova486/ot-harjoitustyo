from tkinter import Text, ttk, constants, messagebox


class ExerciseView:
    def __init__(self, root, _to_main_view, sevice):
        self._root = root
        self._to_main_view = _to_main_view
        self._frame = None
        self._frame = None
        self._word_label = None
        self._translate_entry = None
        self.wordlist = sevice.get_active_wordlist()
        self._word_list_index = 0
        self._sevice = sevice
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _check(self):
        word = self._translate_entry.get()
        if word == self.wordlist[self._word_list_index][1]:
            messagebox.showinfo(
                title="Oikein!", message=self.wordlist[self._word_list_index][0] + " = " + word)
            if self._word_list_index >= len(self.wordlist) - 1:

                messagebox.showinfo(title="Selvisit loppuun!",
                                    message="Hienoa! "+"Kaikki oikein!")
            else:
                self._word_list_index += 1
                self._word_label.config(
                    text=self.wordlist[self._word_list_index][0])
                self._translate_entry.delete(0, len(word))
                self._translate_entry.insert(0, "")
        else:
            messagebox.showerror(title="Väärin!", message="yritä uudelleen")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._translate_entry = ttk.Entry(master=self._frame)

        self._word_label = ttk.Label(
            master=self._frame, text=self.wordlist[self._word_list_index][0])

        check_button = ttk.Button(
            master=self._frame, text="Tarkista", command=self._check)

        back = ttk.Button(master=self._frame, text="Takaisin",
                          command=self._to_main_view)

        self._word_label.grid(row=0, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        self._translate_entry.grid(
            row=1, column=0, sticky=(constants.E, constants.W), padx=5, pady=5
        )

        check_button.grid(
            row=2, column=0, sticky=(constants.E, constants.W), padx=5, pady=5
        )

        back.grid(row=3, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)
