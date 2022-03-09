eng_alph = 'abcdefghijklmnopqrstuvwxyz'
eng_alph_upper = eng_alph.upper()
rus_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
rus_alph_upper = rus_alph.upper()
other = '`1234567890-=~!@#$%^&*()_+][}{\';":/?\\.>,< '
labels = {'encrypted_text':{'rus':'зашифрованный текст:','eng':'encrypted text:'}}
alphabets = {
    'rus':
        {
            'lower': rus_alph,
            'upper': rus_alph_upper
        },
    'eng':
        {
            'lower': eng_alph,
            'upper': eng_alph_upper
        }
}