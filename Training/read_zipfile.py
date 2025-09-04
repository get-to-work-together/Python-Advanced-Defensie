import zipfile

filename = 'threading-guide.zip'

with zipfile.ZipFile(filename) as zf:
    for filename in zf.filelist:
        print(filename)
    with zf.open('threading-guide/example29.py') as f:
        print(f.read().decode())