import pillow_heif
from PIL import Image
import os

pillow_heif.register_heif_opener()

heic_files = [f for f in os.listdir('.') if f.lower().endswith('.heic')]
for f in heic_files:
    try:
        img = Image.open(f)
        out = f.rsplit('.',1)[0] + '.jpg'
        img = img.convert('RGB')
        img.save(out, 'JPEG', quality=88)
        print(f'OK: {f} -> {out}')
    except Exception as e:
        print(f'ERR: {f}: {e}')
print('Done.')
