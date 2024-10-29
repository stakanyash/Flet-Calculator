# Flet Calculator by stakanyash (ksh1vn) version 0.9.7

# Know issues: NumPad is not working

# Libs import
import flet as ft
import locale

# Localization list
translations = {
    "en": {
        "title": "Flet Calculator",
        "error": "Error",
        "division_by_zero": "Division by zero!",
        "syntax_error": "Syntax error!",
        "name_error": "Name error!",
        "index_error": "Index error!",
        "zero_print": "Division by zero error has occurred",
        "name_print": "Name error has occurred",
        "syntax_print": "Syntax error has occurred",
        "index_print": "Index error has occurred"
    },
    "ru": {
        "title": "Калькулятор Flet",
        "error": "Ошибка",
        "division_by_zero": "Деление на ноль!",
        "syntax_error": "Синтаксическая ошибка!",
        "name_error": "Ошибка имени!",
        "index_error": "Ошибка индекса!",
        "zero_print": "Случилась ошибка деления на ноль",
        "name_print": "Случилась ошибка имени",
        "syntax_print": "Случилась ошибка синтаксиса",
        "index_print": "Случилась ошибка индекса"
    }
}

# Detect system language
system_lang = locale.getdefaultlocale()[0][:2]
lang = translations.get(system_lang, translations["en"])

# Create page
def main(page: ft.Page):
    page.title = lang["title"]
    page.description = lang["title"]
    page.window_height = 615
    page.window_width = 340
    page.theme_mode = "dark"
    page.window_resizable = False
    page.window_maximizable = False

    # Add dialog_open variable to track if a dialog is open
    global dialog_open
    dialog_open = False

    # Zero division error alert          
    def close_dlgzero(e):
        global dialog_open
        divzero_error.open = False
        dialog_open = False  # Close dialog state
        page.update()

    divzero_error = ft.AlertDialog(
        modal=True,
        title=ft.Text(lang["error"]),
        content=ft.Text(lang["division_by_zero"]),
        actions=[
            ft.TextButton("OK", on_click=close_dlgzero)
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print(lang["zero_print"]),
    )

    # Name error alert          
    def close_dlgname(e):
        global dialog_open
        name_error.open = False
        dialog_open = False  # Close dialog state
        page.update()

    name_error = ft.AlertDialog(
        modal=True,
        title=ft.Text(lang["error"]),
        content=ft.Text(lang["name_error"]),
        actions=[
            ft.TextButton("OK", on_click=close_dlgname)
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print(lang["name_print"]),
    )

    # Syntax error alert
    def close_dlgsyntax(e):
        global dialog_open
        syntax_error.open = False
        dialog_open = False  # Close dialog state
        page.update()

    syntax_error = ft.AlertDialog(
        modal=True,
        title=ft.Text(lang["error"]),
        content=ft.Text(lang["syntax_error"]),
        actions=[
            ft.TextButton("OK", on_click=close_dlgsyntax)
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print(lang["syntax_print"]),
    )

    # Index error alert
    def close_dlgindex(e):
        global dialog_open
        index_error.open = False
        dialog_open = False  # Close dialog state
        page.update()

    index_error = ft.AlertDialog(
        modal=True,
        title=ft.Text(lang["error"]),
        content=ft.Text(lang["index_error"]),
        actions=[
            ft.TextButton("OK", on_click=close_dlgindex)
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print(lang["index_print"]),
    )

    def handle_key_event(e):
        key = e.key

        # Закрытие диалоговых окон по Enter
        if key == "Enter":
            if divzero_error.open:
                close_dlgzero(e)
                return
            elif name_error.open:
                close_dlgname(e)
                return
            elif syntax_error.open:
                close_dlgsyntax(e)
                return
            elif index_error.open:
                close_dlgindex(e)
                return

        # Поддержка основных клавиш и клавиш NumPad
        if key in ["0", "Numpad0"]:
            mainfield.value += "0"
        elif key in ["1", "Numpad1"]:
            mainfield.value += "1"
        elif key in ["2", "Numpad2"]:
            mainfield.value += "2"
        elif key in ["3", "Numpad3"]:
            mainfield.value += "3"
        elif key in ["4", "Numpad4"]:
            mainfield.value += "4"
        elif key in ["5", "Numpad5"]:
            mainfield.value += "5"
        elif key in ["6", "Numpad6"]:
            mainfield.value += "6"
        elif key in ["7", "Numpad7"]:
            mainfield.value += "7"
        elif key in ["8", "Numpad8"]:
            mainfield.value += "8"
        elif key in ["9", "Numpad9"]:
            mainfield.value += "9"
        elif key in [".", "NumpadDecimal"]:
            mainfield.value += "."
        elif key in ["+", "NumpadAdd"]:
            mainfield.value += "+"
        elif key in ["-", "NumpadSubtract"]:
            mainfield.value += "-"
        elif key in ["*", "NumpadMultiply"]:
            mainfield.value += "*"
        elif key in ["/", "NumpadDivide"]:
            mainfield.value += "/"
        elif key == "Backspace":
            mainfield.value = mainfield.value[:-1]
        elif key == "Enter":
            try:
                mainfield.value = str(eval(mainfield.value))
            except ZeroDivisionError:
                page.dialog = divzero_error
                divzero_error.open = True
                mainfield.value = ""
                page.update() 
            except SyntaxError:
                page.dialog = syntax_error
                syntax_error.open = True
                mainfield.value = ""
                page.update()
            except NameError:
                page.dialog = name_error
                name_error.open = True
                mainfield.value = ""
                page.update()
        elif key == "Escape":  # Очистка ввода
            mainfield.value = ""
    
        page.update()

    # Connect keyboard event handler
    page.on_keyboard_event = handle_key_event

    def nightbtn_clicked(e):
        # Change theme
        page.theme_mode = "light" if page.theme_mode =="dark" else "dark"
        page.update()

        # Text field color change

        mainfield.text_style = ft.TextStyle(size=55,color="#9ECAFF") if page.theme_mode=="dark" else ft.TextStyle(size=55,color="#000000")
        mainfield.hint_style = ft.TextStyle(size=55,color="#2F3C4C") if page.theme_mode=="dark" else ft.TextStyle(size=55,color="#d2cec3")

        # Icon of theme button and color change

        theme_btn.icon = ft.icons.SUNNY if page.theme_mode=="dark" else ft.icons.DARK_MODE
        theme_btn.icon_color = "#9ecaff" if page.theme_mode=="dark" else "#000000"

        # Buttons background color change

        buttonsbg = [
            bckspace_btn,
            left_pbtn,
            right_pbtn,
            division_btn,
            seven_btn,
            eight_btn,
            nine_btn,
            multi_btn,
            four_btn,
            five_btn,
            six_btn,
            minus_btn,
            one_btn,
            two_btn,
            three_btn,
            plus_btn,
            clear_button,
            zero_button,
            dot_button
        ]

        for button in buttonsbg:
            button.style = ft.ButtonStyle(bgcolor="#202429") if page.theme_mode=="dark" else ft.ButtonStyle(bgcolor="#f6f6f6")

        # Buttons text color change

        bckspace_btn.icon_color = "#9ecaff" if page.theme_mode=="dark" else "#000000"

        color_dict = {
            "dark": "#9ecaff",
            "light": "#000000"
        }

        def create_text_container(value, size, color):
            return ft.Container(
                content=ft.Column([
                    ft.Text(value=value, size=size, color=color)
            ], alignment=ft.MainAxisAlignment.CENTER)
        )

        left_pbtn.content = create_text_container("(", 23, color_dict[page.theme_mode])
        right_pbtn.content = create_text_container(")", 23, color_dict[page.theme_mode])
        division_btn.content = create_text_container("÷", 30, color_dict[page.theme_mode])

        buttonstext = [
            (seven_btn, "7", 23),
            (eight_btn, "8", 23),
            (nine_btn, "9", 23),
            (multi_btn, "×", 30),
            (four_btn, "4", 23),
            (five_btn, "5", 23),
            (six_btn, "6", 23),
            (minus_btn, "−", 30),
            (one_btn, "1", 23),
            (two_btn, "2", 23),
            (three_btn, "3", 23),
            (plus_btn, "+", 30),
            (clear_button, "C", 23),
            (zero_button, "0", 23),
            (dot_button, ".", 30)
        ]

        for button, value, size in buttonstext:
            button.content = create_text_container(value, size, color_dict[page.theme_mode])

        # Update page
        page.update()

    # Make buttons functional
    def text_enter(e):
        data = e.control.data

        if data in ["1","2","3","4","5","6","7","8","9","0",".","+","-","*","/","(",")"]:
            mainfield.value = str(mainfield.value) + str(data)
            page.update()

    # Equal button functional
        if data =="=":
            try:
                mainfield.value = str(eval(mainfield.value))
            except ZeroDivisionError:
                page.dialog = divzero_error
                divzero_error.open = True
                mainfield.value = ""
                page.update() 
            except SyntaxError:
                page.dialog = syntax_error
                syntax_error.open = True
                mainfield.value = ""
                page.update()
            except NameError:
                page.dialog = name_error
                name_error.open = True
                mainfield.value = ""
                page.update()
            page.update()

    # CLS button functional
        if data=="e":
            try:
                st = list(mainfield.value)
                st.pop()
                mainfield.value = "".join(map(str,st))
            except IndexError:
                page.dialog = index_error
                index_error.open = True
                mainfield.value = ""
                page.update()
            page.update()

    # Clear button functional
        if data=="C":
            mainfield.value = ""
            page.update()

    # Create text field, set read-only, color and size
    mainfield = ft.TextField(
        read_only = True,
        border = ft.InputBorder.NONE,
        text_style = ft.TextStyle(size=55,color="#9ECAFF"),
        text_align = ft.TextAlign.RIGHT,
        hint_text = "0",
        hint_style = ft.TextStyle(size=55,color="#2F3C4C")
    )

    # Add text field to main window
    page.add(mainfield)

    # Buttons
    clear_button = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="C", size=23)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="C",on_click=text_enter, height=70, width=70, style=ft.ButtonStyle(bgcolor="#202429")
    )
    
    zero_button = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="0", size=23)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="0",on_click=text_enter, height=70, width=70, style=ft.ButtonStyle(bgcolor="#202429")
    )

    dot_button = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value=".", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data=".",on_click=text_enter, height=70, width=70, style=ft.ButtonStyle(bgcolor="#202429")
    )
    
    equal_button = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="=", size=30, color="#ffffff")],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="=",on_click=text_enter, height=70, width=70, style=ft.ButtonStyle(bgcolor="#00ba00")
    )

    one_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="1", size=23)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="1",on_click=text_enter, height=70, width=70, style=ft.ButtonStyle(bgcolor="#202429")
    )
    
    two_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="2", size=23)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="2",on_click=text_enter, height=70, width=70, style=ft.ButtonStyle(bgcolor="#202429")
    )

    three_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="3", size=23)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="3",on_click=text_enter, height=70, width=70, style=ft.ButtonStyle(bgcolor="#202429")
    )
    
    plus_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="+", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="+",on_click=text_enter, height=70, width=70, style=ft.ButtonStyle(bgcolor="#202429")
    )

    four_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="4", size=23)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="4",on_click=text_enter, height=70, width=70, style=ft.ButtonStyle(bgcolor="#202429")
    )
    
    five_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="5", size=23)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="5",on_click=text_enter, height=70, width=70, style=ft.ButtonStyle(bgcolor="#202429")
    )

    six_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="6", size=23)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="6",on_click=text_enter, height=70, width=70, style=ft.ButtonStyle(bgcolor="#202429")
    )
    
    minus_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="−", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="-",on_click=text_enter, height=70, width=70, style=ft.ButtonStyle(bgcolor="#202429")
    )

    seven_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="7", size=23)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="7",on_click=text_enter, height=70, width=70, style=ft.ButtonStyle(bgcolor="#202429")
    )
    
    eight_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="8", size=23)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="8",on_click=text_enter, height=70, width=70, style=ft.ButtonStyle(bgcolor="#202429")
    )

    nine_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="9", size=23)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="9",on_click=text_enter, height=70, width=70, style=ft.ButtonStyle(bgcolor="#202429")
    )
    
    multi_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="×", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="*",on_click=text_enter, height=70, width=70, style=ft.ButtonStyle(bgcolor="#202429")
    )

    bckspace_btn = ft.IconButton(
        icon=ft.icons.BACKSPACE_OUTLINED, on_click=text_enter, data="e", height=70, width=70, style=ft.ButtonStyle(bgcolor="#202429"), icon_color="#9ecaff"
    )
    
    left_pbtn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="(", size=23)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="(",on_click=text_enter, height=70, width=70, style=ft.ButtonStyle(bgcolor="#202429")
    )

    right_pbtn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value=")", size=23)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data=")",on_click=text_enter, height=70, width=70, style=ft.ButtonStyle(bgcolor="#202429")
    )
    
    division_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="÷", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="/",on_click=text_enter, height=70, width=70, style=ft.ButtonStyle(bgcolor="#202429")
    )

    theme_btn = ft.IconButton(
        icon=ft.icons.SUNNY, on_click=nightbtn_clicked, icon_color="#9ecaff"
    )

    # Make rows for buttons and set aligment
    row1st = ft.Row(
        controls=[left_pbtn, right_pbtn, division_btn, bckspace_btn],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    row2nd = ft.Row(
        controls=[seven_btn, eight_btn, nine_btn, multi_btn],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    row3rd = ft.Row(
        controls=[four_btn, five_btn, six_btn, minus_btn],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    row4th = ft.Row(
        controls=[one_btn, two_btn, three_btn, plus_btn],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    row5th = ft.Row(
        controls=[clear_button, zero_button, dot_button, equal_button],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # Add rows to main window
    page.add(theme_btn, row1st, row2nd, row3rd, row4th, row5th)

# Start application from def main
ft.app(target=main)