times = ('Palmeiras', 'Flamengo', 'Athletico-PR', 'Fluminense', 'Cruzeiro', 
         'Bahia', 'Bragantino', 'Botafogo', 'Coritiba', 'Atlético-MG', 'Corinthias', 
         'São Paulo', 'EC Vitória', 'Grêmio', 'Mirassol', 'Internacional', 'Santos',
          'Vasco', 'Remo', 'Chapecoense')
print('=-'*15)
print(f'Lista de times do Brasileirão: {times}')
print('=-'*15)
print(f'Os cinco primeiros times da tabela são: {times[0:5]}')
print('=-'*15)
print(f'Os últimos 4 times na tabela são: {times[-4:]}')
print('=-'*15)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('=-'*15)
print(f'O INTERNACIONAL está na posição: {times.index("Internacional")+1}')