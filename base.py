#Projeto Tchau

#inicio

xq = int(input("forneça a coordenada x de um ponto qualquer:"))
xa = int(input("forneça a coordenada x da antena:"))
yq = int(input("forneça a coordenada y de um ponto qualquer:"))
ya = int(input("forneça a coordenada x da antena:"))

pontos = 4
pontos_cobertos = 0
porcentagem = 0

# Entrada das variaveis 

distancia_antena_ponto = (xq-xa)**2+(yq-ya)**2
primeiro_raio_de_cobertura = 640000
segundo_raio_de_cobertura = 490000


    
if distancia_antena_ponto <= primeiro_raio_de_cobertura and segundo_raio_de_cobertura :
    
       print("true")
       pontos_cobertos = +1 
       
       porcentagem = pontos_cobertos * 100 / 4
       print("Cobertas por antenas", porcentagem, "% dos pontos")
                
else:      
       print("false")


       
       
       
     
            
        
    
#Fim do programa 