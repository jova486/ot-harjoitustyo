from tkinter import ttk, constants


class TeacherMainView:
    def __init__(self, root, _to_main_view,sevice):
        self._root = root
        self._to_main_view = _to_main_view
        self._frame = None
        self._frame = None
        self._listname_entry = None
        self._word_entry = None
        self._translate_entry = None
        self.wordlist = []
        self._word_list_index = 0
        self._initialize()
        self._save()
        self._back()
        self._forward()
        self._sevice= sevice
       

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    
    def _save(self):
        word = self._word_entry.get()
        translation = self._translate_entry.get()
        self.wordlist.append(((word,translation)))
        self._word_entry.delete(0, len(word))
        self._translate_entry.delete(0, len(translation))
        self._word_list_index +=1
        print(self.wordlist)

    def _back(self):
        if self._word_list_index == 0:
            return
        else:
            self._word_list_index -= 1
            word = self._word_entry.get()
            translation = self._translate_entry.get()
            
            self._word_entry.delete(0, len(word))
            self._translate_entry.delete(0, len(translation))

            self._word_entry.insert(0,self.wordlist[self._word_list_index][0])
            self._translate_entry.insert(0,self.wordlist[self._word_list_index][1])

    def _forward(self):
        if self._word_list_index == len(self.wordlist)-1:
            return
        else:
            self._word_list_index += 1
            
            word = self._word_entry.get()
            translation = self._translate_entry.get()
            
            self._word_entry.delete(0, len(word))
            self._translate_entry.delete(0, len(translation))

            self._word_entry.insert(0,self.wordlist[self._word_list_index][0])
            self._translate_entry.insert(0,self.wordlist[self._word_list_index][1])
        


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        #label = ttk.Label(master=self._frame, text="Uusi sanalista!")

        listname_label = ttk.Label(master=self._frame, text='Uuden sanalistan nimi')
        self._listname_entry_entry = ttk.Entry(master=self._frame)

        word_label = ttk.Label(master=self._frame, text='Sana')
        self._word_entry = ttk.Entry(master=self._frame)

        translate_label = ttk.Label(master=self._frame, text='Käännös')
        self._translate_entry = ttk.Entry(master=self._frame)
        
        
        back_arrow = ttk.Button(
            master=self._frame,
            text="<=",
            command=self._back
        )

        forward_arrow = ttk.Button(
            master=self._frame,
            text="=>",
            command=self._forward
        )

        new_list = ttk.Button(
            master=self._frame,
            text="Tallenna",
            command=self._save
        )

        back = ttk.Button(
            master=self._frame,
            text="Peru",
            command=self._to_main_view
        )

        listname_label.grid(padx=5, pady=5)
        self._listname_entry_entry.grid(row=0, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        word_label.grid(padx=5, pady=5)
        self._word_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        translate_label.grid(padx=5, pady=5)
        self._translate_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        
        back_arrow.grid(row=3, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)
        forward_arrow.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        new_list.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        back.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        