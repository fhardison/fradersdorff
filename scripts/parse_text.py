from pathlib import Path
import re


DATA = Path('../source/working.txt').read_text()


OUT = {}
buffer = ''
head = ''
i = 0

for line in DATA.split('\n'):
    match = re.match(r'[A-Z\-, ]{2,}', line.strip())
    if match:
        i += 1
        if buffer:
            if 'SQU' in head:
                print(buffer)
                print()
            OUT[re.sub(r'[., \-]', r'', head)] = buffer
            pass
        head = match.group(0)
        buffer = line
    else:
        if buffer:
            buffer += line


Path('../src/fradersdorff.tsv').write_text('\n'.join([x[0] + '\t' + x[1] for x in OUT.items()]))

print(OUT['SQUEAL'])
print(i)

        
