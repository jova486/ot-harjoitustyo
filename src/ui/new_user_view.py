from tkinter import ttk, constants, messagebox

class NewUserView:
    """
    Uuden käyttäjän luomisesta vastaava näkymä luokka

    """
    def __init__(self, root, handle_show_teacher_main_view,sevice):
        
        self._root = root
        self.handle_show_teacher_main_vie = handle_show_teacher_main_view
        self._frame = None
        self._initialize()
        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self._initialize()
        self._sevice= sevice

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()


    def _new_user(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        if self._sevice.add_user(username,password): 
            self.handle_show_teacher_main_vie()
        else:
            messagebox.showerror("Tunnus on jo käytössä.", "Error")

        
        
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame = ttk.Frame(master=self._root)
        
        username_label = ttk.Label(master=self._frame, text='Tunnus')
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text='Salasana')
        self._password_entry = ttk.Entry(master=self._frame)


        create_user_button = ttk.Button(
            master=self._frame,
            text="Luo tunnus",
            command=self._new_user
        )

        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(row=0, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        password_label.grid(padx=5, pady=5)
        
        self._password_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        
        create_user_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        