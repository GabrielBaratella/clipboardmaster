import pyperclip
import time
import datetime

def save_clipboard_content(last_clipboard_content):
    clipboard_content = pyperclip.paste()
    if clipboard_content != last_clipboard_content:
        data_formatada = datetime.date.today().strftime("%d-%m-%Y")
        hora_formatada = datetime.datetime.now().strftime("%H:%M")
        with open(f"{data_formatada}.txt", 'a') as file:
            file.write(f'######### {hora_formatada} ##########\n\n{clipboard_content}\n\n')
        print("Conteúdo do clipboard salvo com sucesso no arquivo 'clipboard_content.txt'")
        return clipboard_content
    return last_clipboard_content

def main():
    last_clipboard_content = ''
    while True:
        last_clipboard_content = save_clipboard_content(last_clipboard_content)
        time.sleep(1)

if __name__ == "__main__":
    main()
