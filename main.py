import flet as ft
import string
import random

def main(page: ft.Page):
   page.window.width = 400
   page.window.min_width = 400
   page.window.height = 700
   page.window.min_height = 700
   page.window.resizable = False
   page.window.maximizable = False
   page.theme_mode = ft.ThemeMode.LIGHT
   page.padding = 0
   page.vertical_alignment = ft.MainAxisAlignment.CENTER
   page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
   
   
   options = {}
   generate_button = ft.Ref[ft.Container]()
   txt_password = ft.Ref[ft.Text]()
   characteres_count = ft.Ref[ft.Slider]()
   btn_clipboard = ft.Ref[ft.IconButton]()


   
   
   def toggle_option(e):
    nonlocal options
    options.update({e.control.data: e.control.value})
    # print (options)

    if any(options.values()):
       generate_button.current.disabled = False
       generate_button.current.opacity = 1
       #btn_clipboard.current.disabled = False
       #btn_clipboard.current.opacity = 1

    else:
       generate_button.current.disabled = True
       generate_button.current.opacity = 0.3
       #btn_clipboard.current.disabled = True
       #btn_clipboard.current.opacity = 0

    generate_button.current.update()
    #btn_clipboard.current.update()


   
   def generate_password(e):
    pwd = ""
    
    if options.get("uppercase"):
      pwd += string.ascii_uppercase 

    if options.get("lowercase"):
      pwd += string.ascii_lowercase 

    if options.get("digits"):
      pwd += string.digits 

    if options.get("punctuation"):
      pwd += string.punctuation 
    
    
    count = int(characteres_count.current.value)
    password = random.choices(pwd, k=count)

    txt_password.current.value = ''.join(password)
    txt_password.current.update()

    btn_clipboard.current.selected = False
    btn_clipboard.current.update()


    btn_clipboard.current.disabled = False
    btn_clipboard.current.opacity = 1
    btn_clipboard.current.update()




   def copy_to_clipboard(e):
    pwd = txt_password.current.value

    if pwd:
      page.set_clipboard(pwd)
      btn_clipboard.current.selected = True
      btn_clipboard.current.update()




   

   layout = ft.Container(
      expand=True,
      padding=ft.padding.only(top=0, left=20, right=20, bottom=0),
      alignment=ft.alignment.center,
      content=ft.Column(
          scroll=ft.ScrollMode.HIDDEN,
          horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
         controls=[
            ft.Text(
                value="Gerador de Senhas",
                size=30,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
            ),

            ft.Divider(height=30, thickness=0.5),

            ft.Container(
                bgcolor=ft.colors.with_opacity(0.3, ft.colors.BLACK),
                border_radius=ft.border_radius.all(5),
                padding=ft.padding.all(10),
               content=ft.Row(
                   alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                  controls=[
                     ft.Text(
                        ref=txt_password,
                        value="",
                        selectable=True,
                        size=20,
                        height=30,
                     ),
                     ft.IconButton(
                        ref=btn_clipboard,
                        icon=ft.icons.COPY,
                        icon_color=ft.colors.WHITE30,
                        selected_icon=ft.icons.CHECK,
                        selected_icon_color=ft.colors.INDIGO,
                        selected=False,
                        disabled=True,
                        opacity=0,
                        on_click=copy_to_clipboard,
                     ),
                  ],
               ),
            ),

            ft.Text(
                value="CARACTERES",
                weight=ft.FontWeight.BOLD,
                size=14,
            ),

            ft.Container(
                bgcolor=ft.colors.with_opacity(0.3, ft.colors.BLACK),
                border_radius=ft.border_radius.all(5),
                content=ft.Slider(
                    ref=characteres_count,
                    value=10,
                    min=4,
                    max=20,
                    divisions=10,
                    label="{value}"
                ),
            ),

            ft.Text(
                value="PREFERÊNCIAS",
                weight=ft.FontWeight.BOLD,
                size=14,
            ),

            ft.ListTile(
                title=ft.Text(
                    value="Letras maiúsculas",
                    size=18,
                ),
                trailing=ft.Switch(
                    adaptive=True,
                    active_color=ft.colors.INDIGO,
                    data="uppercase",
                    on_change=toggle_option,
                ),
                toggle_inputs=True,
            ),

            ft.ListTile(
                title=ft.Text(
                    value="Letras minúsculas",
                    size=18,
                ),
                trailing=ft.Switch(
                    adaptive=True,
                    active_color=ft.colors.INDIGO,
                    data="lowercase",
                    on_change=toggle_option,
                ),
                toggle_inputs=True,
            ),

            ft.ListTile(
                title=ft.Text(
                    value="Incluir números",
                    size=18,
                ),
                trailing=ft.Switch(
                    adaptive=True,
                    active_color=ft.colors.INDIGO,
                    data="digits",
                    on_change=toggle_option,
                ),
                toggle_inputs=True,
            ),

            ft.ListTile(
                title=ft.Text(
                    value="Incluir símbolos",
                    size=18,
                ),
                trailing=ft.Switch(
                    adaptive=True,
                    active_color=ft.colors.INDIGO,
                    data="punctuation",
                    on_change=toggle_option,
                ),
                toggle_inputs=True,
            ),

            ft.Container(
                ref=generate_button,
                gradient=ft.LinearGradient(
                    colors=[ft.colors.INDIGO, ft.colors.BLUE],
                ),
                alignment=ft.alignment.center,
                padding=ft.padding.all(20),
                border_radius=ft.border_radius.all(5),
                content=ft.Text(
                    value="GERAR SENHA",
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.WHITE,
                    size=16,
                ),
                on_click=generate_password,
                disabled=True,
                opacity=0.3,
                animate_opacity=ft.Animation(duration=700, curve=ft.AnimationCurve.DECELERATE)
            ),
         ]
      ),
   ) # fim do layout



   # Adicionando o layout à página e adicionando uma SafeArea para prevenir o overflow
   page.add(
      ft.SafeArea(
          layout,
          expand=True,
      )
   )
   
ft.app(main)