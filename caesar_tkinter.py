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
        self.frames = {}
        self.caesar_frame = CaesarFrame()
        self.caesar_frame.grid(row=1, column=1, sticky="nsew")
        self.frames['caesar_frame'] = self.caesar_frame
        self.atbash_frame = AtbashFrame()
        self.atbash_frame.grid(row=1, column=1, sticky="nsew")
        self.frames['atbash_frame'] = self.atbash_frame
        self.main_frame = MainFrame()
        self.main_frame.grid(row=1, column=1, sticky="nsew")
        self.frames['main_frame'] = self.main_frame
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.geometry(f'{self.width}x{self.height}')
        self.title('ciphers tkinter')
        self.mainmenu = tk.Menu(master=self)
        self.config(menu=self.mainmenu)
        self.cipher_menu_var = tk.StringVar()
        self.cipher_menu = tk.Menu(master=self.mainmenu, tearoff=0)
        self.cipher_menu.add_radiobutton(label='caesar',
                                         command=lambda: self.show_frame(self.caesar_frame), value='caesar',
                                         variable=self.cipher_menu_var)
        self.cipher_menu.add_radiobutton(label='atbash',
                                         command=lambda: self.show_frame(self.atbash_frame), value='atbash',
                                         variable=self.cipher_menu_var)
        self.mainmenu.add_cascade(label='ciphers', menu=self.cipher_menu)
        self.language_menu_var = tk.StringVar(value='eng')
        self.language_menu = tk.Menu(master=self.mainmenu, tearoff=0)
        self.language_menu.add_radiobutton(label='russian', command=lambda: self.set_app_language('rus'), value='rus',
                                           variable=self.language_menu_var)
        self.language_menu.add_radiobutton(label='english', command=lambda: self.set_app_language('eng'), value='eng',
                                           variable=self.language_menu_var)
        self.mainmenu.add_cascade(label='language', menu=self.language_menu)

    @staticmethod
    def show_frame(frame):
        frame.tkraise()

    def set_app_language(self, lang: str):
        self.mainmenu.entryconfigure(1, label=constants.menus['ciphers'][lang])
        self.mainmenu.entryconfigure(2, label=constants.menus['language'][lang])
        self.cipher_menu.entryconfigure(0, label=constants.menus['caesar'][lang])
        self.cipher_menu.entryconfigure(1, label=constants.menus['atbash'][lang])
        self.language_menu.entryconfigure(0, label=constants.menus['russian'][lang])
        self.language_menu.entryconfigure(1, label=constants.menus['english'][lang])

        for frame in self.frames.values():
            frame.encrypted_text_label_var.set(constants.labels['encrypted_text_label'][lang])
            frame.encrypted_text_var.set(constants.labels['encrypted_text'][lang]) if not frame.entry_cleared[
                'key_entry_var'] or not frame.entry_cleared['text_entry_var'] else frame.encrypted_text_var.get()
            frame.rus_button['text'] = constants.buttons['rus'][lang]
            frame.eng_button['text'] = constants.buttons['eng'][lang]
            frame.key_entry_var.set(constants.entrys['key_entry'][lang]) if not frame.entry_cleared[
                'key_entry_var'] else frame.key_entry_var.get()
            frame.text_entry_var.set(constants.entrys['text_entry'][lang]) if not frame.entry_cleared[
                'text_entry_var'] else frame.text_entry_var.get()


class FrameConstructor(tk.Frame):
    def __init__(self, cipher):
        super().__init__()
        self.cipher = cipher
        self.encrypted_text_var = tk.StringVar(value=constants.labels['encrypted_text']['eng'])
        self.encrypted_text = tk.Entry(master=self, textvariable=self.encrypted_text_var, state='readonly')
        self.encrypted_text_label_var = tk.StringVar(value=constants.labels['encrypted_text_label']['eng'])
        self.encrypted_text_label = tk.Label(master=self, textvariable=self.encrypted_text_label_var)
        self.lang_var = tk.StringVar(value='eng')
        self.rus_button = tk.Radiobutton(self, text="rus",
                                         indicatoron=False, value="rus", width=15,
                                         command=self.lang_button_command, variable=self.lang_var)

        self.eng_button = tk.Radiobutton(self, text="eng",
                                         indicatoron=False, value="eng", width=15,
                                         command=self.lang_button_command, variable=self.lang_var)
        self.lang_buttons = {'eng': self.eng_button, 'rus': self.rus_button}
        self.key_entry_var = tk.StringVar(value='key')
        self.key_entry = tk.Entry(master=self, textvariable=self.key_entry_var)
        self.key_entry.var = self.key_entry_var
        self.key_entry.var_name = 'key_entry_var'
        self.key_entry.bind('<1>',
                            lambda event, entry=self.key_entry: self.clear_entry_background(entry))
        self.text_entry_var = tk.StringVar(value='text')
        self.text_entry = tk.Entry(master=self, textvariable=self.text_entry_var)
        self.text_entry.var = self.text_entry_var
        self.text_entry.var_name = 'text_entry_var'
        self.text_entry.bind('<1>',
                             lambda event, entry=self.text_entry: self.clear_entry_background(
                                 entry))
        self.trace_funcs = {'text_entry_var': self.text_entry_var_trace,
                            'key_entry_var': self.key_entry_var_trace}
        self.entry_cleared = {'text_entry_var': False,
                              'key_entry_var': False}
        self.encrypted_alph_var = tk.StringVar(value=constants.labels['encrypted_text']['eng'])
        self.encrypted_alph = tk.Entry(master=self, textvariable=self.encrypted_alph_var, state='readonly')

    def set_encrypted_alph(self):
        self.encrypted_alph.grid(row=1, column=1)

    def set_encrypted_text(self):
        self.encrypted_text.grid(row=0, column=1)

    def set_encrypted_text_label(self):
        self.encrypted_text_label.grid(row=0, column=0)

    def set_lang_buttons(self):
        self.rus_button.grid(row=3, column=0)
        self.eng_button.grid(row=4, column=0)

    def set_key_entry(self):
        self.key_entry.grid(row=2, column=0)

    def set_text_entry(self):
        self.text_entry.grid(row=1, column=0)

    def lang_button_command(self):

        text = self.text_entry_var.get()
        lang = self.lang_var.get()
        key = self.key_entry_var.get()

        lang_alph_lower = Ciphers.alphabets[lang]['lower']
        lang_alph_upper = Ciphers.alphabets[lang]['upper']
        max_key_entry_value = len(lang_alph_lower) - 1
        text_last_letter = text[-1] if text else ''

        if text_last_letter not in lang_alph_lower + lang_alph_upper:
            self.text_entry_var.set('')
            self.encrypted_text_var.set('')

        if key.isdigit() and int(key) > max_key_entry_value:
            self.key_entry_var.set(max_key_entry_value)

    def text_entry_var_trace(self, cipher_name):

        text = self.text_entry_var.get()
        key = self.key_entry_var.get()
        lang = self.lang_var.get()

        cipher = Ciphers(text, key, lang)
        cipher_func = cipher.ciphers_dict[cipher_name]

        text_last_letter = text[-1] if text else ''
        all_text_except_last_letter = text[:-1]
        lang_alph_lower = Ciphers.alphabets[lang]['lower']
        lang_alph_upper = Ciphers.alphabets[lang]['upper']
        lang_button = self.rus_button if lang == 'rus' else self.eng_button

        if text:
            if text_last_letter not in lang_alph_lower + lang_alph_upper and text_last_letter not in Ciphers.other:
                self.text_entry_var.set(all_text_except_last_letter)
                self.flash(lang_button, 100)
            else:
                self.encrypted_text_var.set(cipher_func())

    #  лагает при спаме
    def flash(self, obj, delay):
        self.after(delay, obj.flash())

    def key_entry_var_trace(self, cipher_name):

        text = self.text_entry_var.get()
        key = self.key_entry_var.get()
        lang = self.lang_var.get()

        lang_alph_lower = Ciphers.alphabets[lang]['lower']
        lang_button = self.lang_buttons[lang]
        max_key_entry_value = len(lang_alph_lower) - 1
        all_text_except_last_letter = key[:-1]

        if key.isdigit():
            if int(key) > max_key_entry_value:
                key = max_key_entry_value
                self.key_entry_var.set(key)
                self.flash(lang_button, 100)
            cipher = Ciphers(text, key, lang)
            cipher_func = cipher.ciphers_dict[cipher_name]
            self.encrypted_text_var.set(cipher_func())
        else:
            self.key_entry_var.set(all_text_except_last_letter)

    def clear_entry_background(self, entry):
        entry_var = entry.var
        entry_var_name = entry.var_name
        entry_var.set('')
        entry.unbind('<1>')
        trace_func = self.trace_funcs[entry_var_name]
        entry_var.trace_add('write', lambda name, index, mode: trace_func(self.cipher))
        self.entry_cleared[entry_var_name] = True


class CaesarFrame(FrameConstructor):
    def __init__(self):
        super().__init__(cipher='caesar')
        self.set_encrypted_alph()
        self.set_encrypted_text()
        self.set_encrypted_text_label()
        self.set_key_entry()
        self.set_text_entry()
        self.set_lang_buttons()


class AtbashFrame(FrameConstructor):
    def __init__(self):
        super().__init__(cipher='atbash')
        self.set_encrypted_alph()
        self.set_encrypted_text()
        self.set_encrypted_text_label()
        self.set_text_entry()
        self.set_lang_buttons()


class MainFrame(FrameConstructor):
    def __init__(self):
        super().__init__(cipher='None')


app = App()
app.mainloop()
