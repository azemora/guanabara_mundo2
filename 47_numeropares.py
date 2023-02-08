'''
for c in range (0, 50):
    if c % 2 == 0:
        print(f'Número par: {c}')
'''
# mais otimizado, reduzindo iterações
for c in range (2, 51, 2):
    print(f'Número par: {c}')
