from tkinter import ttk, constants, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import numpy as np


class ExerciseView:
    def __init__(self, root, _to_main_view, sevice):
        self._root = root
        self._to_main_view = _to_main_view
        self._sevice = sevice
        self._frame = None
        self._word_label = None
        self._translate_entry = None
        self.wordlist = sevice.get_wordlist()
        self.wordlist_stat = dict(
            (w, 0) for w in self._sevice.get_word_translations_list())
        self._word_list_index = 0
        self.fig = Figure(figsize=(5, 5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self._root)

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self.canvas.get_tk_widget().destroy()
        self._frame.destroy()

    def plot(self):

        stat = self._sevice.get_statistics()
        keys = stat.keys()
        values = stat.values()
        plot1 = self.fig.add_subplot(111)
        plot1.set_xlabel('Aika')
        plot1.set_title('Oikeat vastaukset %')
        width = .2
        plot1.bar(keys, values, width)
        self.canvas.get_tk_widget().pack(fill=constants.X)

    def _end(self):
        wright = sum(value == 1 for value in self.wordlist_stat.values())
        self._sevice.save_statistics(wright/len(self.wordlist_stat))
        self._word_list_index += 1

        messagebox.showinfo(title="Selvisit loppuun!",
                            message="Hienoa! "+"Kaikki oikein!")
        self.plot()

    def _next(self, next):
        if next == 0:
            self._word_list_index += 1
        word = self._translate_entry.get()
        self._word_label.config(text=self.wordlist[self._word_list_index][0])
        self._translate_entry.delete(0, len(word))
        self._translate_entry.insert(0, "")

    def _check(self):
        if len(self.wordlist) <= self._word_list_index:
            return
        word = self._translate_entry.get()
        if word == self.wordlist[self._word_list_index][1]:
            self.wordlist_stat[word] += 1
            messagebox.showinfo(
                title="Oikein!", message=self.wordlist[self._word_list_index][0] + " = " + word)
            if self._word_list_index == len(self.wordlist) - 1:
                self._end()

            else:
                self._next(0)

        else:
            self.wordlist_stat[self.wordlist[self._word_list_index][1]] += 1
            num_hints = self.wordlist_stat[self.wordlist[self._word_list_index][1]]
            if num_hints == len(self.wordlist[self._word_list_index][1]):
                messagebox.showinfo(
                    title="Sana on", message=self.wordlist[self._word_list_index][0] + " = " + self.wordlist[self._word_list_index][1])
                if self._word_list_index == len(self.wordlist) - 1:
                    self._end()
                else:
                    self._next(0)

            else:
                randnums = np.random.choice(
                    len(self.wordlist[self._word_list_index][1]), num_hints, replace=False)
                hint = []
                for i, character in enumerate(self.wordlist[self._word_list_index][1]):
                    if i in randnums:
                        hint += character
                    else:
                        hint += "_"
                messagebox.showinfo(title="Vihje!", message=hint)
                self._next(1)

    def _initialize(self):
        self._word_list_index = 0
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
