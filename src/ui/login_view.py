from tkinter import ttk, constants, messagebox


class LoginView:

    def __init__(
        self, root, handle_show_teacher_start_view, handle_show_new_user_view, handle_show_student_main_view, sevice
    ):

        self._root = root
        self.handle_show_teacher_start_view = handle_show_teacher_start_view
        self.handle_show_new_user_view = handle_show_new_user_view
        self.handle_show_student_main_view = handle_show_student_main_view
        self._frame = None
        self._username_entry_login = None
        self._password_entry_login = None
        self._sevice = sevice
        self._initialize_login()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _to_new_user(self):
        self.handle_show_new_user_view()

    def _login(self):
        username = self._username_entry_login.get()
        password = self._password_entry_login.get()
        if self._sevice.check_user(username, password):
            if self._sevice.get_teacher() == 1:
                self.handle_show_teacher_start_view()
            else:
                self.handle_show_student_main_view()

        else:
            messagebox.showerror(
                "Virhe", "Käyttäjänimi tai salasana ei täsmää\n yritä uudelleen"
            )

    def _initialize_login(self):
        self._frame = ttk.Frame(master=self._root)

        username_label_login = ttk.Label(
            master=self._frame, text="Käyttäjätunnus")
        self._username_entry_login = ttk.Entry(master=self._frame)

        password_label_login = ttk.Label(master=self._frame, text="Salasana")
        self._password_entry_login = ttk.Entry(master=self._frame)

        login_button = ttk.Button(
            master=self._frame, text="Kirjaudu", command=self._login
        )

        create_user_button = ttk.Button(
            master=self._frame, text="Luo tunnus", command=self._to_new_user
        )

        username_label_login.grid(padx=5, pady=5)
        self._username_entry_login.grid(
            row=0, column=1, sticky=(constants.E, constants.W), padx=5, pady=5
        )
        password_label_login.grid(padx=5, pady=5)

        self._password_entry_login.grid(
            row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5
        )

        login_button.grid(
            columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5
        )
        create_user_button.grid(
            columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5
        )
