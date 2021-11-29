from tkinter import ttk, constants, messagebox


class LoginView:

    def __init__(
        self, root, handle_show_teacher_main_view, handle_show_new_user_view, handle_show_student_main_view, sevice
    ):

        self._root = root
        self.handle_show_teacher_main_vie = handle_show_teacher_main_view
        self.handle_show_new_user_view = handle_show_new_user_view
        self.handle_show_student_main_view = handle_show_student_main_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._sevice = sevice
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _new_user(self):
        self.handle_show_new_user_view()

    def _login(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        if self._sevice.check_user(username, password):
            if self._sevice.get_teacher() == 1:
                self.handle_show_teacher_main_vie()
            else:
                self.handle_show_student_main_view()

        else:
            messagebox.showerror(
                "Virhe", "Käyttäjänimi tai salasana ei täsmää\n yritä uudelleen"
            )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        username_label = ttk.Label(master=self._frame, text="Tunnus")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Salasana")
        self._password_entry = ttk.Entry(master=self._frame)

        login_button = ttk.Button(
            master=self._frame, text="Kirjaudu", command=self._login
        )

        create_user_button = ttk.Button(
            master=self._frame, text="Luo tunnus", command=self._new_user
        )

        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(
            row=0, column=1, sticky=(constants.E, constants.W), padx=5, pady=5
        )
        password_label.grid(padx=5, pady=5)

        self._password_entry.grid(
            row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5
        )

        login_button.grid(
            columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5
        )
        create_user_button.grid(
            columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5
        )
