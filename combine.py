import os

d = r'c:\Users\harip\OneDrive\Documents\vss\DTS'
parts = ['p1.html', 'p2.html', 'p3.html']
combined = ''
for p in parts:
    with open(os.path.join(d, p), 'r', encoding='utf-8') as f:
        combined += f.read() + '\n'

with open(os.path.join(d, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(combined)

print(f'Combined {len(parts)} parts into index.html: {len(combined)} chars')

# Clean up part files
for p in parts:
    os.remove(os.path.join(d, p))
print('Cleaned up part files')

# Also clean up utility scripts
for s in ['fix_encoding.py', 'debug.py']:
    fp = os.path.join(d, s)
    if os.path.exists(fp):
        os.remove(fp)
        print(f'Removed {s}')
