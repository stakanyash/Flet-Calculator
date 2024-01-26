# Flet Calculator by ksh1vn version 0.9.0

# TODO: Add support input from keyboard

# Libs import

import flet as ft
from tkinter import messagebox

# Create page

def main(page: ft.page):
    page.title = "Calculator"
    page.description = "Flet Calculator"
    page.window_height = 345
    page.window_width = 280
    page.bgcolor = "#1A1C1E"
    page.window_resizable = False

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
                messagebox.showerror("Error", "Division by zero.")
                mainfield.value = ""
            except SyntaxError:
                messagebox.showerror("Error", "Invalid syntax.")
                mainfield.value = ""
            page.update()

    # CLS button functional

        if data=="e":
            try:
                st = list(mainfield.value)
                st.pop()
                mainfield.value = "".join(map(str,st))
            except IndexError:
                messagebox.showerror("Error", "Sequence index out of range. Don't try to clear empty text field.")
                mainfield.value = ""
            page.update()

    # Clear button functional

        if data=="C":
            mainfield.value = ""
            page.update()

    # Create text field, set read-only, color and size

    mainfield = ft.TextField(
        read_only=True,
        border_color="#1A1C1E",
        text_style=ft.TextStyle(size=28,color="#9ECAFF", font_family="Segoe UI"),
        text_align=ft.TextAlign.RIGHT,
        hint_text = "0",
        hint_style=ft.TextStyle(size=28,color="#2F3C4C", font_family="Segoe UI")
    )

    # Add text field to main window

    page.add(mainfield)

    # Buttons

    cls_btn = ft.ElevatedButton(
        text="<",data="e",on_click=text_enter
    )
    
    left_pbtn = ft.ElevatedButton(
        text="(",data="(",on_click=text_enter
    )

    right_pbtn = ft.ElevatedButton(
        text=")",data=")",on_click=text_enter
    )
    
    division_btn = ft.ElevatedButton(
        text="/",data="/",on_click=text_enter
    )

    seven_btn = ft.ElevatedButton(
        text="7",data="7",on_click=text_enter
    )
    
    eight_btn = ft.ElevatedButton(
        text="8",data="8",on_click=text_enter
    )

    nine_btn = ft.ElevatedButton(
        text="9",data="9",on_click=text_enter
    )
    
    multi_btn = ft.ElevatedButton(
        text="X",data="*",on_click=text_enter
    )

    four_btn = ft.ElevatedButton(
        text="4",data="4",on_click=text_enter
    )
    
    five_btn = ft.ElevatedButton(
        text="5",data="5",on_click=text_enter
    )

    six_btn = ft.ElevatedButton(
        text="6",data="6",on_click=text_enter
    )
    
    minus_btn = ft.ElevatedButton(
        text="-",data="-",on_click=text_enter
    )

    one_btn = ft.ElevatedButton(
        text="1",data="1",on_click=text_enter
    )
    
    two_btn = ft.ElevatedButton(
        text="2",data="2",on_click=text_enter
    )

    three_btn = ft.ElevatedButton(
        text="3",data="3",on_click=text_enter
    )
    
    plus_btn = ft.ElevatedButton(
        text="+",data="+",on_click=text_enter
    )

    clear_button = ft.ElevatedButton(
        text="C",data="C",on_click=text_enter
    )
    
    zero_button = ft.ElevatedButton(
        text="0",data="0",on_click=text_enter
    )

    dot_button = ft.ElevatedButton(
        text=".",data=".",on_click=text_enter
    )
    
    equal_button = ft.ElevatedButton(
        text="=",data="=",on_click=text_enter
    )

    # Make rows for buttons and set aligment

    row1st = ft.Row(
        controls=[cls_btn, left_pbtn, right_pbtn, division_btn],
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
    page.add(row1st, row2nd, row3rd, row4th, row5th)

# Start application from def main
ft.app(target=main)