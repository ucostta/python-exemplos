#Formatação de Strings
from datetime import datetime
ano_atual = datetime.now().year
clube = 'Palmeiras'
ano_fundacao = 1914
campeonato_brasileiro = 12
print(f"{clube} possui {campeonato_brasileiro} campeonatos brasileiros.")
print(f"São {ano_atual - ano_fundacao} anos de existencia.")