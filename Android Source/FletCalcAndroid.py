# Flet Calculator by ksh1vn alpha version 0.6 for Android

# App interface developed for Samsung Galaxy A10. Normal work of the interface on other devices is not guaranteed.

# TODO: Center text in text field (for now done with creation of empty text field before main)
# TODO: Add menu, add white theme, add button to switch themes between black and white.

# Flet libs import

import flet as ft

# Create page

def main(page: ft.page):
    page.title = "Flet Calculator"
    page.description = "Flet Calculator v0.6"
    page.bgcolor = "#1A1C1E"

    # Make buttons functional

    def text_enter(e):
        data = e.control.data

        if data in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "+", "-", "*", "/", "(", ")"]:
            txt.value = str(txt.value) + str(data)
            page.update()

    # Zero division error alert
            
        def close_dlgzero(e):
            divzero_error.open = False
            page.update()

        divzero_error = ft.AlertDialog(
            modal=True,
            title=ft.Text("Error"),
            content=ft.Text("Division by zero!"),
            actions=[
                ft.TextButton("OK", on_click=close_dlgzero)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Division by zero error has occurred"),
        )

    # Syntax error alert

        def close_dlgsyntax(e):
            syntax_error.open = False
            page.update()

        syntax_error = ft.AlertDialog(
            modal=True,
            title=ft.Text("Error"),
            content=ft.Text("Syntax error!"),
            actions=[
                ft.TextButton("OK", on_click=close_dlgsyntax)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Syntax error has occurred"),
        )

    # Index error alert

        def close_dlgindex(e):
            index_error.open = False
            page.update()

        index_error = ft.AlertDialog(
            modal=True,
            title=ft.Text("Error"),
            content=ft.Text("Index error! Clearing an empty input field is not possible!"),
            actions=[
                ft.TextButton("OK", on_click=close_dlgindex)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Index error has occurred"),
        )

    # Equal button functional

        if data =="=":
            try:
                txt.value = str(eval(txt.value))
            except ZeroDivisionError:
                page.dialog = divzero_error
                divzero_error.open = True
                txt.value = ""
                page.update() 
            except SyntaxError:
                page.dialog = syntax_error
                syntax_error.open = True
                txt.value = ""
                page.update() 
            page.update()

    # CLS button functional

        if data=="e":
            try:
                st = list(txt.value)
                st.pop()
                txt.value = "".join(map(str,st))
                page.update()
            except IndexError:
                page.dialog = index_error
                index_error.open = True
                txt.value = ""
                page.update() 
            page.update()

    # Clear button functional

        if data=="C":
            txt.value = ""
            page.update()

    # Empty text field to ajust main text field position (to be removed)

    nonetext = ft.TextField(
        read_only = True,
        border = ft.InputBorder.NONE
    )

    page.add(nonetext)

    # Create text field, set read-only, color and size

    txt = ft.TextField(
        read_only = True,
        border = ft.InputBorder.NONE,
        text_style = ft.TextStyle(size=65,color="#9ECAFF"),
        height = 170,
        text_align = ft.TextAlign.RIGHT,
        hint_text = "0",
        hint_style = ft.TextStyle(size=65,color="#2F3C4C")
    )

    # Add text field to main window

    page.add(txt)

    # Buttons

    clear_button = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="C", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="C", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )
    
    zero_button = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="0", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="0", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )

    dot_button = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value=".", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data=".", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )
    
    equal_button = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="=", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="=", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )

    one_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="1", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="1", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )
    
    two_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="2", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="2", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )

    three_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="3", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="3", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )
    
    plus_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="+", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="+", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )

    four_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="4", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="4", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )
    
    five_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="5", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="5", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )

    six_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="6", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="6", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )
    
    minus_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="-", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="-", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )

    seven_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="7", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="7", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )
    
    eight_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="8", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="8", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )

    nine_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="9", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="9", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )
    
    multi_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="X", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="*", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )

    cls_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="CLS", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="e", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )
    
    left_pbtn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="(", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="(", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )

    right_pbtn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value=")", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data=")", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )
    
    division_btn = ft.TextButton(
        content=ft.Container(
            content=ft.Column(
                [ft.Text(value="/", size=30)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        data="/", on_click=text_enter, height=100, width=80, style=ft.ButtonStyle(bgcolor="#202429")
    )

    # Make rows for buttons and set aligment

    row1st = ft.Row(
        controls = [cls_btn, left_pbtn, right_pbtn, division_btn],
        alignment = ft.MainAxisAlignment.SPACE_AROUND
    )

    row2nd = ft.Row(
        controls = [seven_btn, eight_btn, nine_btn, multi_btn],
        alignment = ft.MainAxisAlignment.SPACE_AROUND
    )

    row3rd = ft.Row(
        controls = [four_btn, five_btn, six_btn, minus_btn],
        alignment = ft.MainAxisAlignment.SPACE_AROUND
    )

    row4th = ft.Row(
        controls = [one_btn, two_btn, three_btn, plus_btn],
        alignment = ft.MainAxisAlignment.SPACE_AROUND
    )

    row5th = ft.Row(
        controls = [clear_button, zero_button, dot_button, equal_button],
        alignment = ft.MainAxisAlignment.SPACE_AROUND
    )

    # Add rows to main window
    page.add(row1st, row2nd, row3rd, row4th, row5th)

# Start application from def main
ft.app(target=main)