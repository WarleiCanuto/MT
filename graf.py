from matplotlib import pyplot
from MT import plot

data_it, data_tam, data_plvrs, data0, data1 = plot()
print(data_it)
print(data_tam)
pyplot.scatter(data_tam, data_it)
#pyplot.plot(data0, 'r') #Numero de 0s VERMELHO (*10000)
#pyplot.plot(data1, 'g') #Numero de 1s VERDE (*10000)
pyplot.title('Gráfico de Dispersão')
pyplot.ylabel("Iterações")
pyplot.xlabel("Tamanho da Palavra")
pyplot.show()