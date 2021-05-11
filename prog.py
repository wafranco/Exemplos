import pandas as pd # isso aqui gerencia os dados
import matplotlib.pyplot as plt # isso aqui permite fazer gráficos
# pega os dados solares de WDC-SILSO, Royal Observatory of Belgium, Brussels
sun = pd.read_table('http://sidc.oma.be/silso/INFO/sndhemcsv.php', sep=';', encoding= "ISO-8859-1", header=-1)
# faz o gráfico de cada hemisfério do sol
fig = plt.figure()
plt.scatter(sun[3], sun[5], label='Norte', alpha=0.5)
plt.scatter(sun[3], sun[6], label='Sul', alpha=0.5)
plt.title("Atividade solar diária\n")
plt.ylabel('Número de manchas solares')
plt.xlabel('Ano')
plt.legend(loc='upper right')
plt.show()



