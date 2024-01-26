# Flet Calculator by ksh1vn alpha version 0.1 for Android

# TODO: Add support input from keyboard (for Windows version)

# Flet import

import flet as ft

# Create page

def main(page: ft.page):
    page.title = "Калькулятор"
    page.description = "Flet Calculator"
    page.bgcolor = "#1A1C1E"

    # Make buttons functional

    def keyboard(e):
        data = e.control.data

        if data in ["1","2","3","4","5","6","7","8","9","0",".","+","-","*","/","(",")"]:
            txt.value = str(txt.value) + str(data)
            page.update()
    # Equal button functional

        if data =="=":
            try:
                txt.value = str(eval(txt.value))
            except ZeroDivisionError:
                txt.value = "Division by zero!"
            except SyntaxError:
                txt.value = "Invalid syntax."
            page.update()

    # CLS button functional

        if data=="e":
            try:
                st = list(txt.value)
                st.pop()
                txt.value = "".join(map(str,st))
                page.update()
            except IndexError:
                txt.value = "Index error."
            page.update()

    # Clear button functional

        if data=="C":
            txt.value = ""
            page.update()

    # Create text field, set read-only, color and size

    txt = ft.TextField(
        read_only=True,
        border_color="#1A1C1E",
        text_style=ft.TextStyle(size=65,color="#9ECAFF"),
        height=220,
        text_align=ft.TextAlign.RIGHT
    )

    # Add text field to main window

    page.add(txt)

    # Buttons

    cls_btn = ft.ElevatedButton(
        text="<",data="e",on_click=keyboard, height=100, width=80
    )
    
    left_pbtn = ft.ElevatedButton(
        text="(",data="(",on_click=keyboard, height=100, width=80
    )

    right_pbtn = ft.ElevatedButton(
        text=")",data=")",on_click=keyboard, height=100, width=80
    )
    
    division_btn = ft.ElevatedButton(
        text="/",data="/",on_click=keyboard, height=100, width=80
    )

    seven_btn = ft.ElevatedButton(
        text="7",data="7",on_click=keyboard, height=100, width=80
    )
    
    eight_btn = ft.ElevatedButton(
        text="8",data="8",on_click=keyboard, height=100, width=80
    )

    nine_btn = ft.ElevatedButton(
        text="9",data="9",on_click=keyboard, height=100, width=80
    )
    
    multi_btn = ft.ElevatedButton(
        text="X",data="*",on_click=keyboard, height=100, width=80
    )

    four_btn = ft.ElevatedButton(
        text="4",data="4",on_click=keyboard, height=100, width=80
    )
    
    five_btn = ft.ElevatedButton(
        text="5",data="5",on_click=keyboard, height=100, width=80
    )

    six_btn = ft.ElevatedButton(
        text="6",data="6",on_click=keyboard, height=100, width=80
    )
    
    minus_btn = ft.ElevatedButton(
        text="-",data="-",on_click=keyboard, height=100, width=80
    )

    one_btn = ft.ElevatedButton(
        text="1",data="1",on_click=keyboard, height=100, width=80
    )
    
    two_btn = ft.ElevatedButton(
        text="2",data="2",on_click=keyboard, height=100, width=80
    )

    three_btn = ft.ElevatedButton(
        text="3",data="3",on_click=keyboard, height=100, width=80
    )
    
    plus_btn = ft.ElevatedButton(
        text="+",data="+",on_click=keyboard, height=100, width=80
    )

    clear_button = ft.ElevatedButton(
        text="C",data="C",on_click=keyboard, height=100, width=80
    )
    
    zero_button = ft.ElevatedButton(
        text="0",data="0",on_click=keyboard, height=100, width=80
    )

    dot_button = ft.ElevatedButton(
        text=".",data=".",on_click=keyboard, height=100, width=80
    )
    
    equal_button = ft.ElevatedButton(
        text="=",data="=",on_click=keyboard, height=100, width=80
    )

    # Make rows for buttons and set aligment

    row1st = ft.Row(
        controls=[cls_btn, left_pbtn, right_pbtn, division_btn],
        alignment=ft.MainAxisAlignment.SPACE_AROUND
    )

    row2nd = ft.Row(
        controls=[seven_btn, eight_btn, nine_btn, multi_btn],
        alignment=ft.MainAxisAlignment.SPACE_AROUND
    )

    row3rd = ft.Row(
        controls=[four_btn, five_btn, six_btn, minus_btn],
        alignment=ft.MainAxisAlignment.SPACE_AROUND
    )

    row4th = ft.Row(
        controls=[one_btn, two_btn, three_btn, plus_btn],
        alignment=ft.MainAxisAlignment.SPACE_AROUND
    )

    row5th = ft.Row(
        controls=[clear_button, zero_button, dot_button, equal_button],
        alignment=ft.MainAxisAlignment.SPACE_AROUND
    )

    # Add rows to main window
    page.add(row1st, row2nd, row3rd, row4th, row5th)

# Start application from def main
ft.app(target=main)