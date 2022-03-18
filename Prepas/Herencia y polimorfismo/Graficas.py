
'''  Cómo hacer gráficas con Python - Bytes  '''

from matplotlib import pyplot

lenguajes = ('Python', 'C', 'Java', 'Go', 'JavaScript')
slices = (100, 130, 90, 80, 128)
colores = ('red', 'blue', 'green', '#DD98AA', '#18492D')
#valores=(0.1,0,0,0,0)

#SERIA COMO EL NIVEL DE SEPARACION DEL RADIO
valores = (0.1, 0, 0, 0, 0)


#AGREGANDO UN 5to VALOR
# valores=(0,0,0,0,0,0)
# colores=('red','blue','green','#DD98AA','#18492D','gray')
# lenguajes=('Python', 'C', 'Java', 'Go', 'JavaScript','C++')
# slices=(100,130,90,80,128,140)


#pyplot.rcParams['toolbar']='None'

_, _, texto = pyplot.pie(slices, colors=colores, labels=lenguajes,
                         autopct='%1.1f%%', explode=valores, startangle=90)

for text in texto:
    text.set_color('white')


pyplot.axis('equal')
pyplot.title('Grafica de lenguajes de programacion')
#pyplot.legend(labels=lenguajes)
pyplot.show()
pyplot.savefig('lenguajes.png')















# '''INSTAGRAM: @coders.eduyear'''


# '''GRAFICA DE PIE'''

# import matplotlib.pyplot as plt


# labels= 'Dog', 'Cat', 'Lyon', 'bird'
# sizes=[15,30,45,10]

# fig1,ax1=plt.subplots()
# ax1.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)

# ax1.axis('equal')
# plt.show()


# '''GRAFICA DE BARRAS'''

# import matplotlib.pyplot as plt
# fig=plt.figure()
# ax=fig.add_axes([0,0,1,1])
# #plt.show()
# langs=['C','C++','Python','Java','PHP']
# students=[23,17,35,29,12]
# ax.bar(langs,students,color='gray')
# plt.show()






















'''📊 ¿Cómo hacer varias gráficas en una sola ventana? | Subplot | Matplotlib | Python | ¡Muy Básico!'''

# import matplotlib.pyplot as plt
# import numpy as np

# fig=plt.figure(figsize=(15,15))
# fig.tight_layout()
# colores=['blue','green','red','cyan','magenta','yellow','black','white']

# for i in range(1,7):
#     x=np.arange(0,16,2)
#     #ESTO QUIERE DECIR, COMIENZA EN 0 LLEGA HASTA EL 16 Y VA DE 2 EN 2
#     y=pow(x,np.random.randint(0,6))+np.random.randint(0,10)*x+np.random.randint(-5,10)
#     ax=plt.subplot(2,3,i)

#     ax.plot(x,y,color=colores[i])
#     ax.set_xlabel('x')
#     ax.set_ylabel('y')
#     ax.set_title('Grafica'+str(i))

# plt.show()
