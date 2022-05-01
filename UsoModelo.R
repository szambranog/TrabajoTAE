##Uso del modelo
#Nombre


#Proposito
#

load("modeloknnAbuelxs.RData")

#Definición input
input <- data.frame(P6020=1, P6040=72, P5502=5, P6071=1, P6080=6, num_ninxs=2, num_adultxs=1, num_abuelxs=2,
                    P6160=1, P8587=3, P1930=1, afiliado=1)
input_preprocesado <- scale(input, center = media_total,
                            scale = desv_est_total)
output <- predict(modelo_knn_A_k4 ,newdata = input_preprocesado)