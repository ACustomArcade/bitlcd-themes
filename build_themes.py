#!usr/bin/python3

import hashlib
import os
import sys
import zipfile

BITLCD_SUBDIR = 'thirdparty'
subdirs = next(os.walk('.'))[1]

for subdir in subdirs:
    if subdir == '.git':
        continue
    
    files = next(os.walk(subdir))[2]

    zip_filename = f'bitlcd-{subdir}.zip'

    with zipfile.ZipFile(zip_filename, mode="w") as archive:
        for filename in files:
            filepath = os.path.join(subdir, filename)
            zipfilepath = os.path.join(BITLCD_SUBDIR, filename)
            archive.write(filepath, zipfilepath)

    with open(zip_filename, 'rb') as themezip:
        data = themezip.read()    
        theme_md5 = hashlib.md5(data).hexdigest()
        md5_filename = f'{zip_filename}.md5'

    with open(md5_filename, 'w') as md5file:
        md5file.write(f'{theme_md5}\n')
