##Uso del modelo
#Nombre


#Proposito
#

load("modeloknn.RData")

#Definición input
input <- data.frame(edad_casa=3.5,dist_mrt=5:1600,cant_tiendas=3)
input_preprocesado <- scale(input, center = media_total,
                            scale = desv_est_total)
output <- predict(modelo_knn_k4,newdata = input_preprocesado)