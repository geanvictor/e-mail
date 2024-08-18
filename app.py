import PySimpleGUI as sg

sg.theme('reddit')

janela_principal =[
    [sg.Text('email'),sg.Input(key='email')],
    [sg.Text('senha'),sg.Input(key='senha',password_char='*')],
    [sg.FolderBrowse('Escolher  pasta anexos',target='input_anexos'), sg.Input
    (key='input_anexos')],
    [sg.FolderBrowse('Escolher  pasta planilha',target='input_planilha'), sg.Input
    (key='input_planilha')],
    [sg.Button('salvar')]
]

janela= sg.Window('principal',layout=janela_principal)

while True:
    event, values =janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'salvar':
        email = values['email']
        senha = values['senha']
        caminho_pasta_anexos = ['input_anexos']
        caminho_pasta_planilha=values ['input_planilha']
        
        print(f'o e-mail digitado foi {email}')
        print(f'a senha digitado foi {senha}')
        print(f'o caminho da pasta de anexos é {caminho_pasta_anexos}')
        print(f'o caminho para a pasta de planilhas é {caminho_pasta_planilha}')
        
        