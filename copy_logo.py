import shutil, os, unicodedata
pngs = [f for f in os.listdir('.') if f.endswith('.png')]
for f in pngs:
    fn = unicodedata.normalize('NFC', f)
    if 'бородой' in fn and 'чб' not in fn and not fn.startswith('logo'):
        shutil.copy2(f, 'logo.png')
        print('Copied:', repr(f))
        break
