import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Criando um DataFrame com os dados fornecidos
dados_gasolina = pd.DataFrame({
    'dia': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'preco': [5.11, 4.99, 5.02, 5.21, 5.07, 5.09, 5.13, 5.12, 4.94, 5.03]
})

# Criando um gráfico de linha com Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(data=dados_gasolina, x='dia', y='preco', marker='o')

# Adicionando rótulos e título
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.title('Preço da Gasolina ao Longo do Tempo')

# Salvando o gráfico como uma imagem PNG
plt.savefig('gasolina.png')

# Exibindo o gráfico
plt.show()
