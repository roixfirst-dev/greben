import unicodedata
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find and replace logo filename
old = unicodedata.normalize('NFC', 'Гребень лого с бородой цветной.png')
html = html.replace(old, 'logo.png')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Count replaced:', html.count('logo.png'))
