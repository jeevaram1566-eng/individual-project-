import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error


# ============================================================
# DATABASE SETTINGS
# ============================================================

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "jeevzz@56"
DB_NAME = "book_store_management"


# ============================================================
# APPLICATION LOGIN
# ============================================================

APP_USERNAME = "jeevzz"
APP_PASSWORD = ("jeeva123")


# ============================================================
# DATABASE CONNECTION
# ============================================================

def connect_db(show_error=True):

    try:

        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        if connection.is_connected():
            return connection

    except Error as e:

        if show_error:

            messagebox.showerror(
                "Database Connection Error",
                f"Could not connect to MySQL.\n\n{e}"
            )

    return None


# ============================================================
# MAIN APPLICATION
# ============================================================

class BookstoreApp:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Bookstore Management System"
        )

        self.root.geometry(
            "1350x780"
        )

        self.root.minsize(
            1000,
            650
        )

        self.current_table = None
        self.columns = []
        self.primary_key = None
        self.tree = None
        self.search_entry = None

        self.employee_mapping = {}
        self.employee_display_columns = []

        self.setup_style()

        self.show_login()

    # ========================================================
    # STYLE
    # ========================================================

    def setup_style(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except Exception:
            pass

        style.configure(
            "Treeview",
            background="white",
            foreground="#222222",
            rowheight=34,
            fieldbackground="white",
            font=("Arial", 10)
        )

        style.configure(
            "Treeview.Heading",
            background="#17365D",
            foreground="white",
            font=("Arial", 10, "bold"),
            padding=8
        )

        style.map(
            "Treeview",
            background=[
                ("selected", "#2F75B5")
            ],
            foreground=[
                ("selected", "white")
            ]
        )

    # ========================================================
    # LOGIN PAGE
    # ========================================================

    def show_login(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.configure(
            bg="#17365D"
        )

        container = tk.Frame(
            self.root,
            bg="#17365D"
        )

        container.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        login_box = tk.Frame(
            container,
            bg="white",
            width=450,
            height=540
        )

        login_box.pack()

        login_box.pack_propagate(False)

        tk.Label(
            login_box,
            text="📚",
            bg="white",
            font=("Arial", 50)
        ).pack(
            pady=(25, 0)
        )

        tk.Label(
            login_box,
            text="BOOKSTORE",
            bg="white",
            fg="#17365D",
            font=("Arial", 25, "bold")
        ).pack()

        tk.Label(
            login_box,
            text="Management System",
            bg="white",
            fg="#777777",
            font=("Arial", 11)
        ).pack(
            pady=(0, 25)
        )

        tk.Label(
            login_box,
            text="Username",
            bg="white",
            fg="#333333",
            font=("Arial", 10, "bold")
        ).pack(
            anchor="w",
            padx=50
        )

        self.username_entry = tk.Entry(
            login_box,
            font=("Arial", 12),
            bd=1,
            relief="solid"
        )

        self.username_entry.pack(
            fill="x",
            padx=50,
            pady=(5, 15),
            ipady=8
        )

        tk.Label(
            login_box,
            text="Password",
            bg="white",
            fg="#333333",
            font=("Arial", 10, "bold")
        ).pack(
            anchor="w",
            padx=50
        )

        password_frame = tk.Frame(
            login_box,
            bg="white"
        )

        password_frame.pack(
            fill="x",
            padx=50,
            pady=(5, 10)
        )

        self.password_entry = tk.Entry(
            password_frame,
            font=("Arial", 12),
            bd=1,
            relief="solid",
            show="*"
        )

        self.password_entry.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=8
        )

        self.show_password = False

        tk.Button(
            password_frame,
            text="👁",
            command=self.toggle_password,
            bg="white",
            relief="flat",
            bd=0,
            font=("Arial", 12),
            cursor="hand2"
        ).pack(
            side="right",
            padx=5
        )

        tk.Label(
            login_box,
            text="Enter your credentials to continue",
            bg="white",
            fg="#888888",
            font=("Arial", 9)
        ).pack(
            pady=(0, 15)
        )

        tk.Button(
            login_box,
            text="LOGIN",
            command=self.login,
            bg="#17365D",
            fg="white",
            activebackground="#2F75B5",
            activeforeground="white",
            relief="flat",
            bd=0,
            font=("Arial", 11, "bold"),
            cursor="hand2"
        ).pack(
            fill="x",
            padx=50,
            ipady=10
        )

        tk.Button(
            login_box,
            text="Exit",
            command=self.root.destroy,
            bg="white",
            fg="#C00000",
            activebackground="white",
            relief="flat",
            bd=0,
            font=("Arial", 10),
            cursor="hand2"
        ).pack(
            pady=15
        )

        self.root.bind(
            "<Return>",
            lambda event: self.login()
        )

        self.username_entry.focus()

    # ========================================================
    # TOGGLE PASSWORD
    # ========================================================

    def toggle_password(self):

        if self.show_password:

            self.password_entry.config(
                show="*"
            )

            self.show_password = False

        else:

            self.password_entry.config(
                show=""
            )

            self.show_password = True

    # ========================================================
    # LOGIN
    # ========================================================

    def login(self):

        username = self.username_entry.get().strip()
        password = self.password_entry.get()

        if not username or not password:

            messagebox.showwarning(
                "Login Required",
                "Please enter username and password."
            )

            return

        if (
            username == APP_USERNAME
            and password == APP_PASSWORD
        ):

            self.root.unbind("<Return>")

            self.open_application()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid username or password."
            )

            self.password_entry.delete(
                0,
                tk.END
            )

            self.password_entry.focus()

    # ========================================================
    # OPEN APPLICATION
    # ========================================================

    def open_application(self):

        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.configure(
            bg="#F4F6F8"
        )

        self.create_sidebar()

        self.create_main_area()

        self.show_dashboard()

    # ========================================================
    # SIDEBAR
    # ========================================================

    def create_sidebar(self):

        self.sidebar = tk.Frame(
            self.root,
            bg="#17365D",
            width=240
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)

        tk.Label(
            self.sidebar,
            text="📚",
            bg="#17365D",
            fg="white",
            font=("Arial", 35)
        ).pack(
            pady=(25, 0)
        )

        tk.Label(
            self.sidebar,
            text="BOOKSTORE",
            bg="#17365D",
            fg="white",
            font=("Arial", 20, "bold")
        ).pack(
            pady=(0, 30)
        )

        self.menu_button(
            "🏠  Dashboard",
            self.show_dashboard
        )

        self.menu_button(
            "📚  Books",
            lambda: self.show_table("books")
        )

        self.menu_button(
            "🗂  Categories",
            lambda: self.show_table("categories")
        )

        self.menu_button(
            "👤  Customers",
            lambda: self.show_table("customers")
        )

        self.menu_button(
            "🛒  Orders",
            lambda: self.show_table("orders")
        )

        self.menu_button(
            "📦  Order Details",
            lambda: self.show_table("order_details")
        )

        self.menu_button(
            "👨‍💼  Employees",
            self.show_employees
        )

        self.menu_button(
            "📊  Sales Insights",
            self.show_sales_insights
        )

        tk.Frame(
            self.sidebar,
            bg="#17365D",
            height=15
        ).pack()

        self.menu_button(
            "🚪  Logout",
            self.logout
        )

        self.menu_button(
            "❌  Exit",
            self.root.destroy
        )

    # ========================================================
    # MENU BUTTON
    # ========================================================

    def menu_button(
        self,
        text,
        command
    ):

        button = tk.Button(
            self.sidebar,
            text=text,
            command=command,
            bg="#17365D",
            fg="white",
            activebackground="#2F75B5",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            bd=0,
            anchor="w",
            padx=20,
            pady=11,
            cursor="hand2"
        )

        button.pack(
            fill="x",
            padx=10,
            pady=1
        )

    # ========================================================
    # LOGOUT
    # ========================================================

    def logout(self):

        answer = messagebox.askyesno(
            "Logout",
            "Are you sure you want to logout?"
        )

        if answer:

            self.current_table = None
            self.columns = []
            self.primary_key = None
            self.tree = None

            self.show_login()

    # ========================================================
    # MAIN AREA
    # ========================================================

    def create_main_area(self):

        self.main = tk.Frame(
            self.root,
            bg="#F4F6F8"
        )

        self.main.pack(
            side="right",
            fill="both",
            expand=True
        )

    # ========================================================
    # CLEAR MAIN
    # ========================================================

    def clear_main(self):

        for widget in self.main.winfo_children():
            widget.destroy()

        self.tree = None
        self.search_entry = None

    # ========================================================
    # DATABASE HELPERS
    # ========================================================

    def get_columns(self, table):

        db = connect_db()

        if db is None:
            return []

        cursor = None

        try:

            cursor = db.cursor(
                dictionary=True
            )

            cursor.execute(
                f"SHOW COLUMNS FROM `{table}`"
            )

            return cursor.fetchall()

        except Error as e:

            messagebox.showerror(
                "Database Error",
                f"Could not read table `{table}`.\n\n{e}"
            )

            return []

        finally:

            try:

                if cursor:
                    cursor.close()

                db.close()

            except Exception:
                pass

    def get_count(self, table):

        db = connect_db(
            show_error=False
        )

        if db is None:
            return 0

        cursor = None

        try:

            cursor = db.cursor()

            cursor.execute(
                f"SELECT COUNT(*) FROM `{table}`"
            )

            row = cursor.fetchone()

            if row:
                return int(row[0])

            return 0

        except Error:
            return 0

        finally:

            try:

                if cursor:
                    cursor.close()

                db.close()

            except Exception:
                pass

    def query_one(
        self,
        sql,
        params=()
    ):

        db = connect_db(
            show_error=False
        )

        if db is None:
            return None

        cursor = None

        try:

            cursor = db.cursor()

            cursor.execute(
                sql,
                params
            )

            return cursor.fetchone()

        except Error:
            return None

        finally:

            try:

                if cursor:
                    cursor.close()

                db.close()

            except Exception:
                pass

    def query_all(
        self,
        sql,
        params=()
    ):

        db = connect_db(
            show_error=False
        )

        if db is None:
            return []

        cursor = None

        try:

            cursor = db.cursor()

            cursor.execute(
                sql,
                params
            )

            return cursor.fetchall()

        except Error:
            return []

        finally:

            try:

                if cursor:
                    cursor.close()

                db.close()

            except Exception:
                pass

    # ========================================================
    # DASHBOARD
    # ========================================================

    def show_dashboard(self):

        self.clear_main()

        self.current_table = None
        self.columns = []
        self.primary_key = None

        header = tk.Frame(
            self.main,
            bg="#F4F6F8"
        )

        header.pack(
            fill="x",
            padx=30,
            pady=25
        )

        tk.Label(
            header,
            text="Bookstore Dashboard",
            bg="#F4F6F8",
            fg="#17365D",
            font=("Arial", 27, "bold")
        ).pack(
            anchor="w"
        )

        tk.Label(
            header,
            text="Manage your bookstore database and sales",
            bg="#F4F6F8",
            fg="#666666",
            font=("Arial", 11)
        ).pack(
            anchor="w",
            pady=5
        )

        cards = tk.Frame(
            self.main,
            bg="#F4F6F8"
        )

        cards.pack(
            fill="x",
            padx=30
        )

        card_data = [
            (
                "Books",
                self.get_count("books"),
                "📚"
            ),
            (
                "Categories",
                self.get_count("categories"),
                "🗂"
            ),
            (
                "Customers",
                self.get_count("customers"),
                "👤"
            ),
            (
                "Orders",
                self.get_count("orders"),
                "🛒"
            ),
            (
                "Employees",
                self.get_count("employees"),
                "👨‍💼"
            )
        ]

        for i, (
            title,
            value,
            icon
        ) in enumerate(card_data):

            card = tk.Frame(
                cards,
                bg="white",
                highlightbackground="#D9DEE5",
                highlightthickness=1
            )

            card.grid(
                row=0,
                column=i,
                sticky="nsew",
                padx=6
            )

            cards.columnconfigure(
                i,
                weight=1
            )

            tk.Label(
                card,
                text=icon,
                bg="white",
                font=("Arial", 26)
            ).pack(
                pady=(18, 3)
            )

            tk.Label(
                card,
                text=str(value),
                bg="white",
                fg="#17365D",
                font=("Arial", 25, "bold")
            ).pack()

            tk.Label(
                card,
                text=title,
                bg="white",
                fg="#666666",
                font=("Arial", 10, "bold")
            ).pack(
                pady=(0, 18)
            )

        self.dashboard_sales_area()

    # ========================================================
    # DASHBOARD SALES
    # ========================================================

    def dashboard_sales_area(self):

        box = tk.Frame(
            self.main,
            bg="white",
            highlightbackground="#D9DEE5",
            highlightthickness=1
        )

        box.pack(
            fill="x",
            padx=36,
            pady=25
        )

        tk.Label(
            box,
            text="Sales Overview",
            bg="white",
            fg="#17365D",
            font=("Arial", 17, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(18, 12)
        )

        sales = self.query_one(
            "SELECT "
            "COALESCE(SUM(quantity * price), 0), "
            "COALESCE(SUM(quantity), 0) "
            "FROM order_details"
        )

        total_sales = (
            float(sales[0])
            if sales
            else 0
        )

        books_sold = (
            int(sales[1])
            if sales
            else 0
        )

        orders = self.get_count(
            "orders"
        )

        customers = self.get_count(
            "customers"
        )

        row = tk.Frame(
            box,
            bg="white"
        )

        row.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        stats = [
            (
                "Total Sales",
                f"₹{total_sales:,.2f}"
            ),
            (
                "Total Orders",
                str(orders)
            ),
            (
                "Books Sold",
                str(books_sold)
            ),
            (
                "Customers",
                str(customers)
            )
        ]

        for i, (
            name,
            value
        ) in enumerate(stats):

            row.columnconfigure(
                i,
                weight=1
            )

            frame = tk.Frame(
                row,
                bg="#F4F6F8"
            )

            frame.grid(
                row=0,
                column=i,
                sticky="nsew",
                padx=5
            )

            tk.Label(
                frame,
                text=value,
                bg="#F4F6F8",
                fg="#17365D",
                font=("Arial", 19, "bold")
            ).pack(
                pady=(13, 3)
            )

            tk.Label(
                frame,
                text=name,
                bg="#F4F6F8",
                fg="#666666",
                font=("Arial", 9, "bold")
            ).pack(
                pady=(0, 13)
            )

        tk.Button(
            box,
            text="Open Sales Insights",
            command=self.show_sales_insights,
            bg="#17365D",
            fg="white",
            activebackground="#2F75B5",
            relief="flat",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=20,
            pady=8
        ).pack(
            pady=(0, 18)
        )

    # ========================================================
    # GENERIC TABLE PAGE
    # ========================================================

    def show_table(
        self,
        table
    ):

        self.current_table = table

        self.columns = self.get_columns(
            table
        )

        if not self.columns:
            return

        self.primary_key = None

        for column in self.columns:

            if column.get("Key") == "PRI":

                self.primary_key = column[
                    "Field"
                ]

                break

        self.clear_main()

        title_map = {
            "books": "Books",
            "categories": "Categories",
            "customers": "Customers",
            "orders": "Orders",
            "order_details": "Order Details"
        }

        title = title_map.get(
            table,
            table.replace(
                "_",
                " "
            ).title()
        )

        header = tk.Frame(
            self.main,
            bg="#F4F6F8"
        )

        header.pack(
            fill="x",
            padx=30,
            pady=(25, 15)
        )

        tk.Label(
            header,
            text=title,
            bg="#F4F6F8",
            fg="#17365D",
            font=("Arial", 25, "bold")
        ).pack(
            side="left"
        )

        button_frame = tk.Frame(
            header,
            bg="#F4F6F8"
        )

        button_frame.pack(
            side="right"
        )

        tk.Button(
            button_frame,
            text="＋ Add",
            command=self.add_record,
            bg="#28A745",
            fg="white",
            activebackground="#218838",
            relief="flat",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=15,
            pady=7
        ).pack(
            side="left",
            padx=4
        )

        tk.Button(
            button_frame,
            text="✎ Edit",
            command=self.edit_record,
            bg="#2F75B5",
            fg="white",
            activebackground="#1F5C92",
            relief="flat",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=15,
            pady=7
        ).pack(
            side="left",
            padx=4
        )

        tk.Button(
            button_frame,
            text="🗑 Delete",
            command=self.delete_record,
            bg="#C00000",
            fg="white",
            activebackground="#990000",
            relief="flat",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=15,
            pady=7
        ).pack(
            side="left",
            padx=4
        )

        search_frame = tk.Frame(
            self.main,
            bg="#F4F6F8"
        )

        search_frame.pack(
            fill="x",
            padx=30,
            pady=(0, 12)
        )

        self.search_entry = tk.Entry(
            search_frame,
            font=("Arial", 11),
            relief="solid",
            bd=1
        )

        self.search_entry.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=7
        )

        tk.Button(
            search_frame,
            text="🔍 Search",
            command=self.search,
            bg="#17365D",
            fg="white",
            activebackground="#2F75B5",
            relief="flat",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=18,
            pady=8
        ).pack(
            side="left",
            padx=(8, 4)
        )

        tk.Button(
            search_frame,
            text="Refresh",
            command=self.load_records,
            bg="#777777",
            fg="white",
            activebackground="#555555",
            relief="flat",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=18,
            pady=8
        ).pack(
            side="left"
        )

        table_frame = tk.Frame(
            self.main,
            bg="white"
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 25)
        )

        column_names = [
            c["Field"]
            for c in self.columns
        ]

        self.tree = ttk.Treeview(
            table_frame,
            columns=column_names,
            show="headings"
        )

        y_scroll = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        x_scroll = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.tree.xview
        )

        self.tree.configure(
            yscrollcommand=y_scroll.set,
            xscrollcommand=x_scroll.set
        )

        for name in column_names:

            self.tree.heading(
                name,
                text=name.replace(
                    "_",
                    " "
                ).title()
            )

            self.tree.column(
                name,
                width=150,
                minwidth=90,
                anchor="center"
            )

        self.tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        y_scroll.pack(
            side="right",
            fill="y"
        )

        x_scroll.pack(
            side="bottom",
            fill="x"
        )

        self.tree.bind(
            "<Double-1>",
            lambda event: self.edit_record()
        )

        self.load_records()

    # ========================================================
    # LOAD RECORDS
    # ========================================================

    def load_records(
        self,
        search_text=""
    ):

        if (
            not self.current_table
            or self.tree is None
        ):
            return

        for item in self.tree.get_children():

            self.tree.delete(
                item
            )

        db = connect_db(
            show_error=False
        )

        if db is None:
            return

        cursor = None

        try:

            cursor = db.cursor()

            names = [
                c["Field"]
                for c in self.columns
            ]

            select_sql = ", ".join(
                f"`{name}`"
                for name in names
            )

            if search_text:

                conditions = " OR ".join(
                    f"CAST(`{name}` AS CHAR) LIKE %s"
                    for name in names
                )

                sql = (
                    f"SELECT {select_sql} "
                    f"FROM `{self.current_table}` "
                    f"WHERE {conditions}"
                )

                if self.current_table == "order_details":
                    sql += " ORDER BY `order_id` ASC, `order_detail_id` ASC"

                params = [
                    f"%{search_text}%"
                ] * len(names)

                cursor.execute(
                    sql,
                    params
                )

            else:

                if self.current_table == "order_details":

                    order_sql = (
                        f"SELECT {select_sql} "
                        f"FROM `{self.current_table}` "
                        f"ORDER BY `order_id` ASC, `order_detail_id` ASC"
                    )

                else:

                    order_sql = (
                        f"SELECT {select_sql} "
                        f"FROM `{self.current_table}`"
                    )

                cursor.execute(order_sql)

            rows = cursor.fetchall()

            for row in rows:

                self.tree.insert(
                    "",
                    "end",
                    values=row
                )

        except Error as e:

            messagebox.showerror(
                "Database Error",
                f"Could not load records.\n\n{e}"
            )

        finally:

            try:

                if cursor:
                    cursor.close()

                db.close()

            except Exception:
                pass

    # ========================================================
    # SEARCH
    # ========================================================

    def search(self):

        if self.search_entry is not None:

            self.load_records(
                self.search_entry.get().strip()
            )

    # ========================================================
    # ADD RECORD
    # ========================================================

    def add_record(self):

        if not self.current_table:
            return

        self.open_form()

    # ========================================================
    # EDIT RECORD
    # ========================================================

    def edit_record(self):

        if self.tree is None:
            return

        selected = self.tree.selection()

        if not selected:

            messagebox.showwarning(
                "No Selection",
                "Please select a record first."
            )

            return

        values = self.tree.item(
            selected[0],
            "values"
        )

        self.open_form(
            values
        )

    # ========================================================
    # GENERIC ADD / EDIT FORM
    # ========================================================

    def open_form(
        self,
        old_values=None
    ):

        if (
            not self.current_table
            or not self.columns
        ):
            return

        window = tk.Toplevel(
            self.root
        )

        if old_values is not None:

            window.title(
                "Edit " +
                self.current_table
            )

        else:

            window.title(
                "Add " +
                self.current_table
            )

        window.geometry(
            "520x650"
        )

        window.transient(
            self.root
        )

        window.grab_set()

        canvas = tk.Canvas(
            window,
            bg="#F4F6F8",
            highlightthickness=0
        )

        scrollbar = ttk.Scrollbar(
            window,
            orient="vertical",
            command=canvas.yview
        )

        form = tk.Frame(
            canvas,
            bg="#F4F6F8"
        )

        form.bind(
            "<Configure>",
            lambda e:
            canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window(
            (0, 0),
            window=form,
            anchor="nw",
            width=500
        )

        canvas.configure(
            yscrollcommand=scrollbar.set
        )

        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        form_title = (
            "Edit Order Detail"
            if old_values is not None and self.current_table == "order_details"
            else "Add Order Detail"
            if old_values is None and self.current_table == "order_details"
            else "Edit Record"
            if old_values is not None
            else "Add Record"
        )

        tk.Label(
            form,
            text=form_title,
            bg="#F4F6F8",
            fg="#17365D",
            font=("Arial", 20, "bold")
        ).pack(
            pady=25
        )

        entries = {}

        for index, column in enumerate(
            self.columns
        ):

            name = column["Field"]

            field_frame = tk.Frame(
                form,
                bg="#F4F6F8"
            )

            field_frame.pack(
                fill="x",
                padx=40,
                pady=7
            )

            tk.Label(
                field_frame,
                text=name.replace(
                    "_",
                    " "
                ).title(),
                bg="#F4F6F8",
                fg="#333333",
                font=("Arial", 10, "bold")
            ).pack(
                anchor="w"
            )

            entry = tk.Entry(
                field_frame,
                font=("Arial", 11),
                relief="solid",
                bd=1
            )

            entry.pack(
                fill="x",
                pady=4,
                ipady=7
            )

            if (
                old_values is not None
                and index < len(old_values)
            ):

                entry.insert(
                    0,
                    str(
                        old_values[index]
                    )
                )

            is_auto_increment = (
                "auto_increment"
                in column.get(
                    "Extra",
                    ""
                ).lower()
            )

            is_primary_key = (
                column.get("Key") == "PRI"
            )

            if is_auto_increment or is_primary_key:

                entry.configure(
                    state="disabled"
                )

            entries[name] = entry

        def save():

            db = connect_db()

            if db is None:
                return

            cursor = None

            try:

                cursor = db.cursor()

                # INSERT

                if old_values is None:

                    # Extra validation for order_details so the user gets
                    # a clear message instead of an unclear MySQL error.
                    if self.current_table == "order_details":

                        required_order_detail_fields = [
                            "order_id",
                            "book_id",
                            "quantity",
                            "price"
                        ]

                        missing_fields = []

                        for field_name in required_order_detail_fields:
                            if field_name in entries:
                                if not entries[field_name].get().strip():
                                    missing_fields.append(field_name)

                        if missing_fields:
                            messagebox.showwarning(
                                "Required Fields",
                                "Please enter:\n\n"
                                + "\n".join(missing_fields)
                            )
                            return

                    names = []
                    values = []

                    for column in self.columns:

                        name = column["Field"]

                        if (
                            "auto_increment"
                            in column.get(
                                "Extra",
                                ""
                            ).lower()
                        ):
                            continue

                        value = entries[
                            name
                        ].get().strip()

                        if value == "":
                            value = None

                        names.append(
                            f"`{name}`"
                        )

                        values.append(
                            value
                        )

                    if not names:

                        messagebox.showerror(
                            "Error",
                            "No fields available."
                        )

                        return

                    placeholders = ", ".join(
                        ["%s"] *
                        len(values)
                    )

                    sql = (
                        f"INSERT INTO "
                        f"`{self.current_table}` "
                        f"({', '.join(names)}) "
                        f"VALUES "
                        f"({placeholders})"
                    )

                    cursor.execute(
                        sql,
                        values
                    )

                # UPDATE

                else:

                    if self.primary_key is None:

                        messagebox.showerror(
                            "Error",
                            "This table has no primary key."
                        )

                        return

                    update_parts = []
                    values = []

                    for column in self.columns:

                        name = column["Field"]

                        if (
                            name ==
                            self.primary_key
                        ):
                            continue

                        value = entries[
                            name
                        ].get().strip()

                        if value == "":
                            value = None

                        update_parts.append(
                            f"`{name}` = %s"
                        )

                        values.append(
                            value
                        )

                    pk_index = next(
                        (
                            i
                            for i, column
                            in enumerate(
                                self.columns
                            )
                            if column["Field"]
                            ==
                            self.primary_key
                        ),
                        None
                    )

                    if pk_index is None:

                        messagebox.showerror(
                            "Error",
                            "Primary key not found."
                        )

                        return

                    values.append(
                        old_values[
                            pk_index
                        ]
                    )

                    sql = (
                        f"UPDATE "
                        f"`{self.current_table}` "
                        f"SET "
                        f"{', '.join(update_parts)} "
                        f"WHERE "
                        f"`{self.primary_key}` = %s"
                    )

                    cursor.execute(
                        sql,
                        values
                    )

                db.commit()

                messagebox.showinfo(
                    "Success",
                    "Record saved successfully."
                )

                window.destroy()

                self.load_records()

            except Error as e:

                db.rollback()

                messagebox.showerror(
                    "Database Error",
                    str(e)
                )

            finally:

                try:

                    if cursor:
                        cursor.close()

                    db.close()

                except Exception:
                    pass

        tk.Button(
            form,
            text="💾  SAVE",
            command=save,
            bg="#28A745",
            fg="white",
            activebackground="#218838",
            relief="flat",
            font=("Arial", 11, "bold"),
            padx=45,
            pady=10,
            cursor="hand2"
        ).pack(
            pady=25
        )

    # ========================================================
    # DELETE RECORD
    # ========================================================

    def delete_record(self):

        if self.tree is None:
            return

        selected = self.tree.selection()

        if not selected:

            messagebox.showwarning(
                "No Selection",
                "Please select a record first."
            )

            return

        if self.primary_key is None:

            messagebox.showerror(
                "Error",
                "Primary key was not found."
            )

            return

        values = self.tree.item(
            selected[0],
            "values"
        )

        pk_index = next(
            (
                i
                for i, column
                in enumerate(
                    self.columns
                )
                if column["Field"]
                ==
                self.primary_key
            ),
            None
        )

        if pk_index is None:

            messagebox.showerror(
                "Error",
                "Primary key was not found."
            )

            return

        pk_value = values[
            pk_index
        ]

        confirm = messagebox.askyesno(
            "Delete Record",
            "Are you sure you want to delete "
            "this record?\n\n"
            f"{self.primary_key}: {pk_value}"
        )

        if not confirm:
            return

        db = connect_db()

        if db is None:
            return

        cursor = None

        try:

            cursor = db.cursor()

            cursor.execute(
                f"DELETE FROM "
                f"`{self.current_table}` "
                f"WHERE "
                f"`{self.primary_key}` = %s",
                (pk_value,)
            )

            db.commit()

            messagebox.showinfo(
                "Deleted",
                "Record deleted successfully."
            )

            self.load_records()

        except Error as e:

            db.rollback()

            messagebox.showerror(
                "Delete Error",
                "Could not delete record.\n\n"
                "If this record is used by another table, "
                "delete the related child records first.\n\n"
                f"{e}"
            )

        finally:

            try:

                if cursor:
                    cursor.close()

                db.close()

            except Exception:
                pass

    # ========================================================
    # EMPLOYEE COLUMN MAPPING
    # ========================================================

    def get_employee_mapping(
        self,
        columns
    ):

        actual = {
            c["Field"].lower(): c
            for c in columns
        }

        aliases = {

            "employee_id": [
                "employee_id",
                "emp_id",
                "id"
            ],

            "employee_name": [
                "employee_name",
                "emp_name",
                "name"
            ],

            "phone": [
                "phone",
                "phone_number",
                "mobile",
                "mobile_number",
                "contact_number"
            ],

            "email": [
                "email",
                "email_address"
            ],

            "address": [
                "address",
                "employee_address"
            ],

            "joining_date": [
                "joining_date",
                "join_date",
                "date_of_joining"
            ],

            "salary": [
                "salary",
                "employee_salary",
                "monthly_salary"
            ]
        }

        mapping = {}

        for logical_name, names in aliases.items():

            for name in names:

                if name.lower() in actual:

                    mapping[
                        logical_name
                    ] = actual[
                        name.lower()
                    ]["Field"]

                    break

        return mapping

    # ========================================================
    # EMPLOYEE PAGE
    # ========================================================

    def show_employees(self):

        columns = self.get_columns(
            "employees"
        )

        if not columns:
            return

        mapping = self.get_employee_mapping(
            columns
        )

        required = [
            "employee_id",
            "employee_name",
            "phone",
            "email",
            "address",
            "joining_date",
            "salary"
        ]

        missing = [
            name
            for name in required
            if name not in mapping
        ]

        if missing:

            messagebox.showerror(
                "Employee Table Error",
                "The employees table is missing these "
                "required fields:\n\n"
                +
                "\n".join(missing)
                +
                "\n\nSupported column names are handled automatically."
            )

            return

        self.employee_mapping = mapping

        self.current_table = "employees"

        self.columns = columns

        self.primary_key = next(
            (
                c["Field"]
                for c in columns
                if c.get("Key") == "PRI"
            ),
            mapping["employee_id"]
        )

        self.clear_main()

        header = tk.Frame(
            self.main,
            bg="#F4F6F8"
        )

        header.pack(
            fill="x",
            padx=30,
            pady=(25, 15)
        )

        tk.Label(
            header,
            text="Employee Details",
            bg="#F4F6F8",
            fg="#17365D",
            font=("Arial", 25, "bold")
        ).pack(
            side="left"
        )

        buttons = tk.Frame(
            header,
            bg="#F4F6F8"
        )

        buttons.pack(
            side="right"
        )

        tk.Button(
            buttons,
            text="＋ Add Employee",
            command=self.add_employee,
            bg="#28A745",
            fg="white",
            activebackground="#218838",
            relief="flat",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=15,
            pady=7
        ).pack(
            side="left",
            padx=4
        )

        tk.Button(
            buttons,
            text="✎ Edit",
            command=self.edit_employee,
            bg="#2F75B5",
            fg="white",
            activebackground="#1F5C92",
            relief="flat",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=15,
            pady=7
        ).pack(
            side="left",
            padx=4
        )

        tk.Button(
            buttons,
            text="🗑 Delete",
            command=self.delete_employee,
            bg="#C00000",
            fg="white",
            activebackground="#990000",
            relief="flat",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=15,
            pady=7
        ).pack(
            side="left",
            padx=4
        )

        search_frame = tk.Frame(
            self.main,
            bg="#F4F6F8"
        )

        search_frame.pack(
            fill="x",
            padx=30,
            pady=(0, 12)
        )

        self.search_entry = tk.Entry(
            search_frame,
            font=("Arial", 11),
            relief="solid",
            bd=1
        )

        self.search_entry.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=7
        )

        tk.Button(
            search_frame,
            text="🔍 Search",
            command=self.search_employee,
            bg="#17365D",
            fg="white",
            activebackground="#2F75B5",
            relief="flat",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=18,
            pady=8
        ).pack(
            side="left",
            padx=(8, 4)
        )

        tk.Button(
            search_frame,
            text="Refresh",
            command=self.load_employees,
            bg="#777777",
            fg="white",
            activebackground="#555555",
            relief="flat",
            font=("Arial", 10, "bold"),
            cursor="hand2",
            padx=18,
            pady=8
        ).pack(
            side="left"
        )

        table_frame = tk.Frame(
            self.main,
            bg="white"
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 25)
        )

        display_columns = [
            mapping[x]
            for x in required
        ]

        self.employee_display_columns = (
            display_columns
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=display_columns,
            show="headings"
        )

        y_scroll = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        x_scroll = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.tree.xview
        )

        self.tree.configure(
            yscrollcommand=y_scroll.set,
            xscrollcommand=x_scroll.set
        )

        headings = {

            mapping["employee_id"]:
                "Employee ID",

            mapping["employee_name"]:
                "Employee Name",

            mapping["phone"]:
                "Phone Number",

            mapping["email"]:
                "Email",

            mapping["address"]:
                "Address",

            mapping["joining_date"]:
                "Joining Date",

            mapping["salary"]:
                "Salary"
        }

        widths = {

            mapping["employee_id"]:
                110,

            mapping["employee_name"]:
                180,

            mapping["phone"]:
                140,

            mapping["email"]:
                200,

            mapping["address"]:
                220,

            mapping["joining_date"]:
                130,

            mapping["salary"]:
                120
        }

        for name in display_columns:

            self.tree.heading(
                name,
                text=headings[name]
            )

            self.tree.column(
                name,
                width=widths[name],
                minwidth=90,
                anchor="center"
            )

        self.tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        y_scroll.pack(
            side="right",
            fill="y"
        )

        x_scroll.pack(
            side="bottom",
            fill="x"
        )

        self.tree.bind(
            "<Double-1>",
            lambda event: self.edit_employee()
        )

        self.load_employees()

    # ========================================================
    # LOAD EMPLOYEES
    # ========================================================

    def load_employees(
        self,
        search_text=""
    ):

        if (
            self.tree is None
            or not self.employee_mapping
        ):
            return

        for item in self.tree.get_children():

            self.tree.delete(
                item
            )

        m = self.employee_mapping

        logical_names = [
            "employee_id",
            "employee_name",
            "phone",
            "email",
            "address",
            "joining_date",
            "salary"
        ]

        columns = [
            m[x]
            for x in logical_names
        ]

        db = connect_db(
            show_error=False
        )

        if db is None:
            return

        cursor = None

        try:

            cursor = db.cursor()

            select_sql = ", ".join(
                f"`{c}`"
                for c in columns
            )

            if search_text:

                conditions = " OR ".join(
                    f"CAST(`{c}` AS CHAR) LIKE %s"
                    for c in columns
                )

                sql = (
                    f"SELECT {select_sql} "
                    f"FROM `employees` "
                    f"WHERE {conditions}"
                )

                cursor.execute(
                    sql,
                    [
                        f"%{search_text}%"
                    ] * len(columns)
                )

            else:

                cursor.execute(
                    f"SELECT {select_sql} "
                    f"FROM `employees`"
                )

            rows = cursor.fetchall()

            for row in rows:

                self.tree.insert(
                    "",
                    "end",
                    values=row
                )

        except Error as e:

            messagebox.showerror(
                "Database Error",
                f"Could not load employees.\n\n{e}"
            )

        finally:

            try:

                if cursor:
                    cursor.close()

                db.close()

            except Exception:
                pass

    # ========================================================
    # EMPLOYEE SEARCH
    # ========================================================

    def search_employee(self):

        text = ""

        if self.search_entry:

            text = self.search_entry.get().strip()

        self.load_employees(
            text
        )

    # ========================================================
    # ADD EMPLOYEE
    # ========================================================

    def add_employee(self):

        self.open_employee_form()

    # ========================================================
    # EDIT EMPLOYEE
    # ========================================================

    def edit_employee(self):

        if self.tree is None:
            return

        selected = self.tree.selection()

        if not selected:

            messagebox.showwarning(
                "No Selection",
                "Please select an employee first."
            )

            return

        values = self.tree.item(
            selected[0],
            "values"
        )

        self.open_employee_form(
            values
        )

    # ========================================================
    # EMPLOYEE FORM
    # ========================================================

    def open_employee_form(
        self,
        old_values=None
    ):

        m = self.employee_mapping

        logical_fields = [

            (
                "employee_id",
                "Employee ID"
            ),

            (
                "employee_name",
                "Employee Name"
            ),

            (
                "phone",
                "Phone Number"
            ),

            (
                "email",
                "Email"
            ),

            (
                "address",
                "Address"
            ),

            (
                "joining_date",
                "Joining Date"
            ),

            (
                "salary",
                "Salary"
            )
        ]

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Edit Employee"
            if old_values is not None
            else "Add Employee"
        )

        window.geometry(
            "560x650"
        )

        window.transient(
            self.root
        )

        window.grab_set()

        form = tk.Frame(
            window,
            bg="#F4F6F8"
        )

        form.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            form,
            text=(
                "Edit Employee"
                if old_values is not None
                else "Add Employee"
            ),
            bg="#F4F6F8",
            fg="#17365D",
            font=("Arial", 20, "bold")
        ).pack(
            pady=20
        )

        entries = {}

        for index, (
            logical,
            label_text
        ) in enumerate(
            logical_fields
        ):

            frame = tk.Frame(
                form,
                bg="#F4F6F8"
            )

            frame.pack(
                fill="x",
                padx=40,
                pady=5
            )

            tk.Label(
                frame,
                text=label_text,
                bg="#F4F6F8",
                fg="#333333",
                font=("Arial", 10, "bold")
            ).pack(
                anchor="w"
            )

            entry = tk.Entry(
                frame,
                font=("Arial", 11),
                relief="solid",
                bd=1
            )

            entry.pack(
                fill="x",
                pady=3,
                ipady=6
            )

            if old_values is not None:

                entry.insert(
                    0,
                    str(
                        old_values[index]
                    )
                )

            actual_column = m[
                logical
            ]

            column_info = next(
                (
                    c
                    for c in self.columns
                    if c["Field"]
                    == actual_column
                ),
                {}
            )

            if (
                old_values is None
                and
                "auto_increment"
                in column_info.get(
                    "Extra",
                    ""
                ).lower()
            ):

                entry.configure(
                    state="disabled"
                )

            entries[
                logical
            ] = entry

        def save_employee():

            db = connect_db()

            if db is None:
                return

            cursor = None

            try:

                cursor = db.cursor()

                # INSERT

                if old_values is None:

                    names = []
                    values = []

                    for logical, _ in logical_fields:

                        actual = m[
                            logical
                        ]

                        info = next(
                            (
                                c
                                for c in self.columns
                                if c["Field"]
                                == actual
                            ),
                            {}
                        )

                        if (
                            "auto_increment"
                            in info.get(
                                "Extra",
                                ""
                            ).lower()
                        ):
                            continue

                        value = entries[
                            logical
                        ].get().strip()

                        if value == "":
                            value = None

                        names.append(
                            f"`{actual}`"
                        )

                        values.append(
                            value
                        )

                    placeholders = ", ".join(
                        ["%s"] *
                        len(values)
                    )

                    sql = (
                        f"INSERT INTO "
                        f"`employees` "
                        f"({', '.join(names)}) "
                        f"VALUES "
                        f"({placeholders})"
                    )

                    cursor.execute(
                        sql,
                        values
                    )

                # UPDATE

                else:

                    pk_column = self.primary_key

                    pk_index = (
                        self.employee_display_columns.index(
                            pk_column
                        )
                    )

                    original_pk = (
                        old_values[
                            pk_index
                        ]
                    )

                    updates = []
                    values = []

                    for logical, _ in logical_fields:

                        actual = m[
                            logical
                        ]

                        if actual == pk_column:
                            continue

                        value = entries[
                            logical
                        ].get().strip()

                        if value == "":
                            value = None

                        updates.append(
                            f"`{actual}` = %s"
                        )

                        values.append(
                            value
                        )

                    values.append(
                        original_pk
                    )

                    sql = (
                        f"UPDATE `employees` "
                        f"SET "
                        f"{', '.join(updates)} "
                        f"WHERE "
                        f"`{pk_column}` = %s"
                    )

                    cursor.execute(
                        sql,
                        values
                    )

                db.commit()

                messagebox.showinfo(
                    "Success",
                    "Employee saved successfully."
                )

                window.destroy()

                self.load_employees()

            except Error as e:

                db.rollback()

                messagebox.showerror(
                    "Database Error",
                    str(e)
                )

            finally:

                try:

                    if cursor:
                        cursor.close()

                    db.close()

                except Exception:
                    pass

        tk.Button(
            form,
            text="💾  SAVE EMPLOYEE",
            command=save_employee,
            bg="#28A745",
            fg="white",
            activebackground="#218838",
            relief="flat",
            font=("Arial", 11, "bold"),
            padx=30,
            pady=10,
            cursor="hand2"
        ).pack(
            pady=20
        )

    # ========================================================
    # DELETE EMPLOYEE
    # ========================================================

    def delete_employee(self):

        if self.tree is None:
            return

        selected = self.tree.selection()

        if not selected:

            messagebox.showwarning(
                "No Selection",
                "Please select an employee first."
            )

            return

        values = self.tree.item(
            selected[0],
            "values"
        )

        pk_column = self.primary_key

        pk_index = (
            self.employee_display_columns.index(
                pk_column
            )
        )

        pk_value = values[
            pk_index
        ]

        if not messagebox.askyesno(
            "Delete Employee",
            "Are you sure you want to delete "
            "this employee?\n\n"
            f"Employee ID: {pk_value}"
        ):
            return

        db = connect_db()

        if db is None:
            return

        cursor = None

        try:

            cursor = db.cursor()

            cursor.execute(
                f"DELETE FROM `employees` "
                f"WHERE `{pk_column}` = %s",
                (pk_value,)
            )

            db.commit()

            messagebox.showinfo(
                "Deleted",
                "Employee deleted successfully."
            )

            self.load_employees()

        except Error as e:

            db.rollback()

            messagebox.showerror(
                "Delete Error",
                f"Could not delete employee.\n\n{e}"
            )

        finally:

            try:

                if cursor:
                    cursor.close()

                db.close()

            except Exception:
                pass

    # ========================================================
    # SALES INSIGHTS
    # ========================================================

    def show_sales_insights(self):

        self.clear_main()

        self.current_table = None
        self.columns = []
        self.primary_key = None

        header = tk.Frame(
            self.main,
            bg="#F4F6F8"
        )

        header.pack(
            fill="x",
            padx=30,
            pady=(25, 10)
        )

        tk.Label(
            header,
            text="Sales Insights",
            bg="#F4F6F8",
            fg="#17365D",
            font=("Arial", 25, "bold")
        ).pack(
            anchor="w"
        )

        tk.Label(
            header,
            text="Understand sales, customers, books and category performance",
            bg="#F4F6F8",
            fg="#666666",
            font=("Arial", 11)
        ).pack(
            anchor="w",
            pady=5
        )

        sales = self.query_one(
            "SELECT "
            "COALESCE(SUM(quantity * price), 0), "
            "COUNT(DISTINCT order_id), "
            "COALESCE(SUM(quantity), 0) "
            "FROM order_details"
        )

        total_sales = (
            float(sales[0])
            if sales
            else 0
        )

        detail_orders = (
            int(sales[1])
            if sales
            else 0
        )

        books_sold = (
            int(sales[2])
            if sales
            else 0
        )

        total_orders = self.get_count(
            "orders"
        )

        customers = self.get_count(
            "customers"
        )

        cards = tk.Frame(
            self.main,
            bg="#F4F6F8"
        )

        cards.pack(
            fill="x",
            padx=30,
            pady=10
        )

        card_values = [

            (
                "Total Sales",
                f"₹{total_sales:,.2f}"
            ),

            (
                "Total Orders",
                str(total_orders)
            ),

            (
                "Books Sold",
                str(books_sold)
            ),

            (
                "Total Customers",
                str(customers)
            ),

            (
                "Orders in Details",
                str(detail_orders)
            )
        ]

        for i, (
            title,
            value
        ) in enumerate(
            card_values
        ):

            cards.columnconfigure(
                i,
                weight=1
            )

            card = tk.Frame(
                cards,
                bg="white",
                highlightbackground="#D9DEE5",
                highlightthickness=1
            )

            card.grid(
                row=0,
                column=i,
                sticky="nsew",
                padx=5
            )

            tk.Label(
                card,
                text=value,
                bg="white",
                fg="#17365D",
                font=("Arial", 18, "bold")
            ).pack(
                pady=(16, 4)
            )

            tk.Label(
                card,
                text=title,
                bg="white",
                fg="#666666",
                font=("Arial", 9, "bold")
            ).pack(
                pady=(0, 16)
            )

        body = tk.Frame(
            self.main,
            bg="#F4F6F8"
        )

        body.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=15
        )

        left = tk.Frame(
            body,
            bg="white",
            highlightbackground="#D9DEE5",
            highlightthickness=1
        )

        left.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 7)
        )

        right = tk.Frame(
            body,
            bg="white",
            highlightbackground="#D9DEE5",
            highlightthickness=1
        )

        right.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(7, 0)
        )

        tk.Label(
            left,
            text="Key Insights",
            bg="white",
            fg="#17365D",
            font=("Arial", 16, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=18
        )

        tk.Label(
            right,
            text="Top 5 Performance",
            bg="white",
            fg="#17365D",
            font=("Arial", 16, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=18
        )

        self.create_key_insight_labels(
            left
        )

        self.create_top_tables(
            right
        )

    # ========================================================
    # KEY SALES INSIGHTS
    # ========================================================

    def create_key_insight_labels(
        self,
        parent
    ):

        top_customer = self.query_one(
            "SELECT "
            "c.customer_name, "
            "COALESCE(SUM(od.quantity * od.price), 0) AS revenue "
            "FROM customers c "
            "JOIN orders o "
            "ON o.customer_id = c.customer_id "
            "JOIN order_details od "
            "ON od.order_id = o.order_id "
            "GROUP BY "
            "c.customer_id, "
            "c.customer_name "
            "ORDER BY revenue DESC "
            "LIMIT 1"
        )

        best_book = self.query_one(
            "SELECT "
            "b.title, "
            "b.author, "
            "COALESCE(SUM(od.quantity), 0) AS qty "
            "FROM books b "
            "JOIN order_details od "
            "ON od.book_id = b.book_id "
            "GROUP BY "
            "b.book_id, "
            "b.title, "
            "b.author "
            "ORDER BY qty DESC "
            "LIMIT 1"
        )

        popular_category = self.query_one(
            "SELECT "
            "c.category_name, "
            "COALESCE(SUM(od.quantity), 0) AS qty "
            "FROM categories c "
            "JOIN books b "
            "ON b.category_id = c.category_id "
            "JOIN order_details od "
            "ON od.book_id = b.book_id "
            "GROUP BY "
            "c.category_id, "
            "c.category_name "
            "ORDER BY qty DESC "
            "LIMIT 1"
        )

        highest_revenue_book = self.query_one(
            "SELECT "
            "b.title, "
            "b.author, "
            "COALESCE(SUM(od.quantity * od.price), 0) AS revenue "
            "FROM books b "
            "JOIN order_details od "
            "ON od.book_id = b.book_id "
            "GROUP BY "
            "b.book_id, "
            "b.title, "
            "b.author "
            "ORDER BY revenue DESC "
            "LIMIT 1"
        )

        repeat_customers = self.query_one(
            "SELECT COUNT(*) "
            "FROM ("
            "SELECT o.customer_id "
            "FROM orders o "
            "GROUP BY o.customer_id "
            "HAVING COUNT(*) > 1"
            ") AS repeat_list"
        )

        values = [

            (
                "Top Customer",

                (
                    f"{top_customer[0]}  |  "
                    f"₹{float(top_customer[1]):,.2f}"
                )
                if top_customer
                else
                "No sales data"
            ),

            (
                "Best-Selling Book",

                (
                    f"{best_book[0]}  |  "
                    f"{best_book[2]} copies"
                )
                if best_book
                else
                "No sales data"
            ),

            (
                "Popular Category",

                (
                    f"{popular_category[0]}  |  "
                    f"{popular_category[1]} books sold"
                )
                if popular_category
                else
                "No sales data"
            ),

            (
                "Highest Revenue Book",

                (
                    f"{highest_revenue_book[0]}  |  "
                    f"₹{float(highest_revenue_book[2]):,.2f}"
                )
                if highest_revenue_book
                else
                "No sales data"
            ),

            (
                "Repeat Customers",

                (
                    str(
                        repeat_customers[0]
                    )
                    if repeat_customers
                    else
                    "0"
                )
            )
        ]

        for title, value in values:

            frame = tk.Frame(
                parent,
                bg="#F4F6F8"
            )

            frame.pack(
                fill="x",
                padx=20,
                pady=6
            )

            tk.Label(
                frame,
                text=title,
                bg="#F4F6F8",
                fg="#17365D",
                font=("Arial", 10, "bold")
            ).pack(
                anchor="w",
                padx=12,
                pady=(8, 1)
            )

            tk.Label(
                frame,
                text=value,
                bg="#F4F6F8",
                fg="#333333",
                font=("Arial", 10),
                wraplength=430,
                justify="left"
            ).pack(
                anchor="w",
                padx=12,
                pady=(0, 8)
            )

    # ========================================================
    # TOP 5 TABLES
    # ========================================================

    def create_top_tables(
        self,
        parent
    ):

        tk.Label(
            parent,
            text="Top 5 Customers by Revenue",
            bg="white",
            fg="#333333",
            font=("Arial", 10, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 6)
        )

        customer_rows = self.query_all(
            "SELECT "
            "c.customer_name, "
            "COALESCE(SUM(od.quantity * od.price), 0) AS revenue "
            "FROM customers c "
            "JOIN orders o "
            "ON o.customer_id = c.customer_id "
            "JOIN order_details od "
            "ON od.order_id = o.order_id "
            "GROUP BY "
            "c.customer_id, "
            "c.customer_name "
            "ORDER BY revenue DESC "
            "LIMIT 5"
        )

        self.make_small_tree(
            parent,
            [
                "Customer",
                "Revenue"
            ],
            [
                [
                    row[0],
                    f"₹{float(row[1]):,.2f}"
                ]
                for row in customer_rows
            ]
        )

        tk.Label(
            parent,
            text="Top 5 Books by Quantity Sold",
            bg="white",
            fg="#333333",
            font=("Arial", 10, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 6)
        )

        book_rows = self.query_all(
            "SELECT "
            "b.title, "
            "COALESCE(SUM(od.quantity), 0) AS qty "
            "FROM books b "
            "JOIN order_details od "
            "ON od.book_id = b.book_id "
            "GROUP BY "
            "b.book_id, "
            "b.title "
            "ORDER BY qty DESC "
            "LIMIT 5"
        )

        self.make_small_tree(
            parent,
            [
                "Book",
                "Qty Sold"
            ],
            [
                [
                    row[0],
                    str(row[1])
                ]
                for row in book_rows
            ]
        )

    # ========================================================
    # SMALL TREEVIEW
    # ========================================================

    def make_small_tree(
        self,
        parent,
        headings,
        rows
    ):

        frame = tk.Frame(
            parent,
            bg="white"
        )

        frame.pack(
            fill="x",
            padx=20
        )

        tree = ttk.Treeview(
            frame,
            columns=headings,
            show="headings",
            height=5
        )

        for heading in headings:

            tree.heading(
                heading,
                text=heading
            )

            tree.column(
                heading,
                width=210,
                anchor="center"
            )

        for row in rows:

            tree.insert(
                "",
                "end",
                values=row
            )

        tree.pack(
            fill="x"
        )


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = BookstoreApp(
        root
    )

    root.mainloop()
