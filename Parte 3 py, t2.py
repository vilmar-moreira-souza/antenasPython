# Projeto Tchau

# inicio
# Suponha que as antenas fornecidas pelo seu estagiário são:
# A antena 1 está localizada na posição A1=(15200,11901) e o seu raio de alcance é R1=800m.
# antena1
a1x = 15200
a1y = 11901
R1 = 800
# A antena 2 está localizada na posição A2=(16093,12287) e o seu raio de alcance é R2=700m.
# antena2
a2x = 16093
a2y = 12287
R2 = 700
#variaveis 
pontos = 0  # quantidade de pontos analizados (iniciado com 0)
pontos_cobertos = 0   # pontos cobertos pelas antenas (iniciado com 0)
porcentagem = 0 # porcentagem de pontos cobertos pelas antenas (iniciado com 0)
# pedindo coodenadas xq e de yq para usuario
pontos = int(input("quantos pontos deseja testar?"))# tera que digitar o numero de pontos que colocar
#
#
for i in range(0, pontos):
       xq = int(input("forneça a coordenada X de um ponto Q =(x,y)"))
       # xa = int(input("forneça a coordenada x da antena:"))  <-apagar
       yq = int(input("forneça a coordenada Y de um ponto Q =(x,y)"))
       # ya = int(input("forneça a coordenada x da antena:")) <-apagar
       distancia_antena_ponto = (xq-a1x)**2+(yq-a1y)**2
       primeiro_raio_de_cobertura = (R1)**2
       segundo_raio_de_cobertura = (R2)**2
       # verifica se o ponto Q é coberto por pelo menos uma antena
       if distancia_antena_ponto <= primeiro_raio_de_cobertura or segundo_raio_de_cobertura:
              print("ponto ", i , " True - coberto pela antena")
              pontos_cobertos = pontos_cobertos +1
       else:
              print("ponto ", i , " False - não coberto pela antena")
#
#
#mostra % dos pontos que sao cobertos 
porcentagem = pontos_cobertos * 100 / pontos
print("----------------------------- ")
print(pontos," pontos analisados")
print("Cobertos por antenas", porcentagem, "% dos pontos")   
#    
# Fim do programa 
