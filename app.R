library(shiny)
library(caret)
load('modeloknnNinxs.RData')
load('modeloknnAbuelxs.RData')

# Define UI for application that draws a histogram
ui <- fluidPage(
  
  # Application title
  titlePanel('Características de la casa'),
  
  # Sidebar with a slider input for number of bins 
  sidebarLayout(
    sidebarPanel(
      radioButtons('sexo_n', 'Sexo niñx:', c('Hombre' = 1, 'Mujer' = 2)),
      sliderInput('edad_n', 'Edad niñx:', min = 0, max = 12, value = 6),
      radioButtons('papa_n', '¿Padre del niñx en el hogar?:', c('Si' = 1, 'No' = 2, 'Fallecido' = 3)),
      radioButtons('mama_n', '¿Madre del niñx en el hogar?:', c('Si' = 1, 'No' = 2, 'Fallecida' = 3)),
      radioButtons('etnia_n', 'Se reconoce como:', c('Indígena' = 1, 'Gitanx' = 2, 'Raizal' = 3, 'Palenquerx' = 4, 'Negrx' = 5, 'Ninguna' = 6)),
      sliderInput('num_nin_n', 'Número de niñxs en el hogar:', min = 1, max = 7, value = 4),
      sliderInput('num_adu_n', 'Número de adultxs en el hogar:', min = 1, max = 5, value = 3),
      sliderInput('num_abu_n', 'Número de abuelxs en el hogar:', min = 1, max = 16, value = 8),
      radioButtons('leer_n', '¿Sabe leer y escribir?:', c('Si' = 1, 'No' = 2, 'No informa' = 0)),
      radioButtons('estudia_n', '¿Actualmente estudia?:', c('Si' = 1, 'No' = 2)),
      radioButtons('enfermedad_n', '¿Tiene una enfermedad crónica?:', c('Si' = 1, 'No' = 2)),
      radioButtons('afiliado_n', '¿A cuál régimen está afiliado?:', c('Contributivo' = 1, 'Especial' = 2, 'Subsidiado' = 3, 'No sabe, no informa' = 9, 'No está afiliado' = 0)),
      radioButtons('permanece_n', '¿Dónde o con quién permanece la mayor parte del tiempo?:', c('Asiste a un hogar comunitario, jardín, centro de desarrollo infantil o colegio' = 1, 'Con su padre o madre en la casa' = 2, 'Con su padre o madre en el trabajo' = 3, 'Con empleado/a o niñero/a en la casa' = 4, 'Al cuidado de un/a pariente de 18 años o más' = 5, 'Al cuidado de un/a pariente menor de 18 años' = 6, 'En casa solo' = 7, 'Otro' = 8)),
      radioButtons('permanece_ed_n', '¿Esta persona ha recibido formación para la crianza?:', c('Si' = 1, 'No' = 2, 'No sabe' = 9)),
      radioButtons('no_asiste_n', '¿Cuál es la razón principal por la que no asiste a hogar comunitario, jardín, centro de desarrollo infantil o colegio?:', c('No informa' = 0, 'No hay una institución cercana' = 1, 'Es muy costoso' = 2, 'No encontró cupo' = 3, 'Prefiere que no asista todavía' = 4, 'Tiene un/a familiar en la casa que lo/la cuida' = 5, 'Considera que no está en edad de asistir, o es recién nacido/a' = 6, 'Solo asiste algunas horas o algunos días de la semana' = 7, 'Otra' = 8)),
      radioButtons('tipo_est_n', '¿A qué tipo de establecimiento asiste?:', c('No informa/ no asiste' = 0, 'Hogar comunitario de Bienestar Familiar' = 1, 'Hogar infantil o jardín de Bienestar Familiar' = 2, 'Centro de desarrollo Infantil Público' = 3, 'Jardín o colegio oficial' = 4, 'Jardín o colegio privado' = 5)),
      radioButtons('actividad_n', '¿Con qué frecuencia realiza actividades de distracción?:', c('Todos los días' = 1, 'Al menos una vez a la semana pero no cada día' = 2, 'Al menos una vez al mes, pero no cada semana' = 3, 'Al menos una vez al mes, pero no todos los meses' = 4, 'No realiza' = 5)),
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
      textOutput('sexo_n'),
      textOutput('edad_n'),
      textOutput('papa_n'),
      textOutput('mama_n'),
      textOutput('etnia_n'),
      textOutput('num_nin_n'),
      textOutput('num_adu_n'),
      textOutput('num_abu_n'),
      textOutput('leer_n'),
      textOutput('estudia_n'),
      textOutput('enfermedad_n'),
      textOutput('afiliado_n'),
      textOutput('permanece_n'),
      textOutput('permanece_ed_n'),
      textOutput('no_asiste_n'),
      textOutput('tipo_est_n'),
      textOutput('actividad_n'),
      textOutput('pred_n')
      
      # plotOutput('distPlot')
    )
  )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
  
  output$pred_n <- renderText({
    entrada <- data.frame(P6020 = input$sexo_n, P6040 = input$edad_n,
                          P6081 = input$papa_n, P6083 = input$mama_n,
                          P6080 = input$etnia_n, num_ninxs = input$num_nin_n,
                          num_adultxs = input$num_adu_n, num_abuelxs = input$num_abu_n,
                          P6160 = input$leer_n, P8586 = input$estudia_n,
                          P1930 = input$enfermedad_n, afiliado = input$afiliado_n,
                          P51 = input$permanece_n, P771 = input$permanece_ed_n,
                          P772 = input$no_asiste_n, P773 = input$tipo_est_n,
                          actividad = input$actividad_n)
    entrada_preprocesada <- scale(entrada, center = media_total_N, scale = desv_est_total_N)
    salida_n <- predict(modelo_knn_N_k4, newdata = entrada_preprocesada)
    return(salida)
  })
  
  output$sexo_n <- renderText({input$sexo_n})
  output$edad_n <- renderText({input$edad_n})
  output$papa_n <- renderText({input$papa_n})
  output$mama_n <- renderText({input$mama_n})
  output$etnia_n <- renderText({input$etnia_n})
  output$num_nin_n <- renderText({input$num_nin_n})
  output$num_adu_n <- renderText({input$num_adu_n})
  output$num_abu_n <- renderText({input$num_abu_n})
  output$leer_n <- renderText({input$leer_n})
  output$estudia_n <- renderText({input$estudia_n})
  output$enfermedad_n <- renderText({input$enfermedad_n})
  output$afiliado_n <- renderText({input$afiliado_n})
  output$permanece_n <- renderText({input$permanece_n})
  output$permanece_ed_n <- renderText({input$permanece_ed_n})
  output$no_asiste_n <- renderText({input$no_asiste_n})
  output$tipo_est_n <- renderText({input$tipo_est_n})
  output$actividad_n <- renderText({input$actividad_n})
  
}
  
# Run the application 
shinyApp(ui = ui, server = server)

