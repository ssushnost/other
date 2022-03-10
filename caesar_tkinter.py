import tkinter as tk
import constants


class Ciphers:
    alphabets = constants.alphabets
    other = constants.other
    rus_alph = constants.rus_alph
    rus_alph_upper = constants.rus_alph_upper
    eng_alph = constants.eng_alph
    eng_alph_upper = constants.eng_alph_upper

    def __init__(self, text, key, lang):
        self.ciphers_dict = {'caesar': self.caesar, 'atbash': self.atbash}
        self.text = text
        self.key = key
        self.lang = lang

    def caesar(self) -> str:
        key = str(self.key) if isinstance(self.key, int) else self.key
        encrypted_result = ''
        if key.isdigit():
            key = int(key)
            lang_alph_lower = Ciphers.alphabets[self.lang]['lower']
            lang_alph_upper = Ciphers.alphabets[self.lang]['upper']
            # если text != ''
            if self.text:
                for letter in self.text:
                    if letter in lang_alph_lower:
                        index = lang_alph_lower.index(letter)
                        encrypted_result += lang_alph_lower[(index + key) % len(lang_alph_lower)]
                    elif letter in lang_alph_upper:
                        index = lang_alph_upper.index(letter)
                        encrypted_result += lang_alph_upper[(index + key) % len(lang_alph_upper)]
                    elif letter in Ciphers.other:
                        encrypted_result += letter
                    else:
                        print('unexpected letter', letter)
        return encrypted_result

    # доделать
    def atbash(self) -> str:
        encrypted_result = ''
        lang_alph_lower = Ciphers.alphabets[self.lang]['lower']
        lang_alph_upper = Ciphers.alphabets[self.lang]['upper']
        if self.text:
            for letter in self.text:
                if letter in lang_alph_lower:
                    index = lang_alph_lower.index(letter)
                    encrypted_result += lang_alph_lower[-1 - index]
                elif letter in lang_alph_upper:
                    index = lang_alph_upper.index(letter)
                    encrypted_result += lang_alph_upper[-1 - index]
                elif letter in Ciphers.other:
                    encrypted_result += letter
                else:
                    print('unexpected letter', letter)
        return encrypted_result


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.geometry(f'{self.width}x{self.height}')
        self.title('ciphers tkinter')
        self.mainmenu = tk.Menu(master=self)
        self.config(menu=self.mainmenu)
        self.cipher_menu = tk.Menu(master=self.mainmenu, tearoff=0)
        self.cipher_menu.add_command(label='caesar',
                                     command=lambda frame_name='caesar_frame': self.show_frame(frame_name))
        self.cipher_menu.add_command(label='atbash',
                                     command=lambda frame_name='atbash_frame': self.show_frame(frame_name))
        self.mainmenu.add_cascade(label='ciphers', menu=self.cipher_menu)
        self.language_menu = tk.Menu(master=self.mainmenu, tearoff=0)
        self.language_menu.add_command(label='russian')
        self.language_menu.add_command(label='english')
        self.mainmenu.add_cascade(label='language', menu=self.language_menu)
        self.frames = {}
        self.set_frames()

    def set_frames(self):
        self.caesar_frame = CaesarFrame()
        self.caesar_frame.grid(row=1, column=1, sticky="nsew")
        self.frames['caesar_frame'] = self.caesar_frame

        self.atbash_frame = AtbashFrame()
        self.atbash_frame.grid(row=1, column=1, sticky="nsew")
        self.frames['atbash_frame'] = self.atbash_frame

        self.main_frame = MainFrame()
        self.main_frame.grid(row=1, column=1, sticky="nsew")
        self.frames['main_frame'] = self.main_frame

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()


class FrameConstructor(tk.Frame):
    def __init__(self, parent, cipher):
        super().__init__()
        self.parent = parent
        self.cipher = cipher
        self.set_string_vars()

    def set_string_vars(self):
        self.parent.encrypted_text_var = tk.StringVar()
        self.parent.key_entry_var = tk.StringVar(value='key', name='key_entry_var')
        self.parent.lang_var = tk.StringVar(value='eng')
        self.parent.encrypted_text_label_var = tk.StringVar(
            value=constants.labels['encrypted_text'][self.parent.lang_var.get()])

    def set_info(self):
        self.parent.info_label = tk.Label(text='information')
        self.parent.info_label.grid(row=5, column=5)

    def set_encrypted_text(self):
        self.parent.encrypted_text = tk.Label(master=self.parent, textvariable=self.parent.encrypted_text_var)
        self.parent.encrypted_text.grid(row=0, column=1)

    def set_encrypted_text_label(self):
        self.parent.encrypted_text_label = tk.Label(master=self.parent, textvariable=self.parent.encrypted_text_label_var)
        self.parent.encrypted_text_label.grid(row=0, column=0)

    def set_lang_buttons(self):
        self.parent.rus_button = tk.Radiobutton(self.parent, text="rus", variable=self.parent.lang_var,
                                                indicatoron=False, value="rus",width=15,
                                                command=self.parent.lang_button_command)
        self.parent.rus_button.grid(row=3, column=0)
        self.parent.eng_button = tk.Radiobutton(self.parent, text="eng", variable=self.parent.lang_var,
                                                indicatoron=False, value="eng", width=15,
                                                command=self.parent.lang_button_command)
        self.parent.eng_button.grid(row=4, column=0)
        self.parent.lang_buttons = {'eng': self.parent.eng_button, 'rus': self.parent.rus_button}

    def set_key_entry(self):
        self.parent.key_entry = tk.Entry(master=self.parent, name='key_entry', textvariable=self.parent.key_entry_var)
        self.parent.key_entry.grid(row=2, column=0)
        self.parent.key_entry.bind('<1>',
                                   lambda event, entry=self.parent.key_entry: self.parent.clear_entry_background(entry))

    def set_text_entry(self):
        self.parent.text_entry_var = tk.StringVar(value='text', name='text_entry_var')
        self.parent.text_entry = tk.Entry(master=self.parent, name='text_entry',
                                          textvariable=self.parent.text_entry_var)
        self.parent.text_entry.grid(row=1, column=0)
        self.parent.text_entry.bind('<1>',
                                    lambda event, entry=self.parent.text_entry: self.parent.clear_entry_background(
                                        entry))

    def lang_button_command(self):
        text = self.parent.text_entry_var.get()
        lang = self.parent.lang_var.get()
        key = self.parent.key_entry_var.get()
        self.parent.encrypted_text_label_var.set(constants.labels['encrypted_text'][lang])
        lang_alph_lower = Ciphers.alphabets[lang]['lower']
        lang_alph_upper = Ciphers.alphabets[lang]['upper']
        max_key_entry_value = len(lang_alph_lower) - 1
        text_last_letter = text[-1] if text else ''
        if text_last_letter not in lang_alph_lower + lang_alph_upper:
            self.parent.text_entry_var.set('')
            self.parent.encrypted_text_var.set('')
        if key.isdigit() and int(key) > max_key_entry_value:
            self.parent.key_entry_var.set(max_key_entry_value)

    def text_entry_var_trace(self, cipher_name):
        text = self.parent.text_entry_var.get()
        key = self.parent.key_entry_var.get()
        lang = self.parent.lang_var.get()
        cipher = Ciphers(text, key, lang)
        cipher_func = cipher.ciphers_dict[cipher_name]
        text_last_letter = text[-1] if text else ''
        all_text_except_last_letter = text[:-1]
        if text:
            if lang == 'rus':
                if text_last_letter in Ciphers.eng_alph + Ciphers.eng_alph_upper:
                    self.parent.text_entry_var.set(all_text_except_last_letter)
                    self.parent.flash(self.parent.rus_button, 100)
                else:
                    self.parent.encrypted_text_var.set(cipher_func())
            elif lang == 'eng':
                if text_last_letter in Ciphers.rus_alph + Ciphers.rus_alph_upper:
                    self.parent.text_entry_var.set(all_text_except_last_letter)
                    self.parent.flash(self.parent.eng_button, 100)
                else:
                    self.parent.encrypted_text_var.set(cipher_func())
            else:
                print('unexpected language: ' + lang)

    #  лагает при спаме
    def flash(self, obj, delay):
        # Unresolved attribute reference 'after' for class 'AppFrame' если не наследовать от tk.Tk
        self.parent.after(delay, obj.flash())

    def key_entry_var_trace(self, cipher_name):
        text = self.parent.text_entry_var.get()
        key = self.parent.key_entry_var.get()
        lang = self.parent.lang_var.get()
        cipher = Ciphers(text, key, lang)
        cipher_func = cipher.ciphers_dict[cipher_name]
        lang_alph_lower = Ciphers.alphabets[lang]['lower']
        lang_button = self.parent.lang_buttons[lang]
        max_key_entry_value = len(lang_alph_lower) - 1
        all_text_except_last_letter = key[:-1]
        if key.isdigit():
            if int(key) > max_key_entry_value:
                key = max_key_entry_value
                self.parent.key_entry_var.set(key)
                self.parent.flash(lang_button, 100)
            self.parent.encrypted_text_var.set(cipher_func())
        else:
            self.parent.key_entry_var.set(all_text_except_last_letter)

    def clear_entry_background(self, entry):
        entry_var_string = entry['textvariable']
        entry_var = eval('self.' + entry_var_string)
        entry_var.set('')
        entry.unbind('<1>')
        self.parent.encrypted_text_var.set('')
        trace_func = eval('self.' + entry_var_string + '_trace')
        entry_var.trace_add('write', lambda name, index, mode: trace_func(self.parent.cipher))


class CaesarFrame(FrameConstructor):
    def __init__(self):
        super().__init__(parent=self, cipher='caesar')
        self.set_encrypted_text()
        self.set_encrypted_text_label()
        self.set_key_entry()
        self.set_text_entry()
        self.set_lang_buttons()


class AtbashFrame(FrameConstructor):
    def __init__(self):
        super().__init__(parent=self, cipher='atbash')
        self.set_encrypted_text()
        self.set_encrypted_text_label()
        self.set_text_entry()
        self.set_lang_buttons()


class MainFrame(FrameConstructor):
    def __init__(self):
        super().__init__(parent=self, cipher='None')


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
