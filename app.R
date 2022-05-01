#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application that draws a histogram
ui <- fluidPage(

    # Application title
    titlePanel("Old Faithful Geyser Data"),

    # Sidebar with a slider input for number of bins 
    sidebarLayout(
        sidebarPanel(
            sliderInput("bins",
                        "Number of bins:",
                        min = 1,
                        max = 50,
                        value = 30)
        ),

        # Show a plot of the generated distribution
        mainPanel(
           plotOutput("distPlot")
        )
    )
)

# Define server logic required to draw a histogram
server <- function(input, output) {

    output$distPlot <- renderPlot({
        # generate bins based on input$bins from ui.R
        x    <- faithful[, 2]
        bins <- seq(min(x), max(x), length.out = input$bins + 1)

        # draw the histogram with the specified number of bins
        hist(x, breaks = bins, col = 'darkgray', border = 'white')
    })
}

# Run the application 
shinyApp(ui = ui, server = server)



#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(caret)
load("modeloknnNinxs.RData")
load("modeloknnAbuelxs.RData")

# Define UI for application that draws a histogram
ui <- fluidPage(
  
  # Application title
  titlePanel("Características del niño"),
  
  # Sidebar with a slider input for number of bins 
  sidebarLayout(
    sidebarPanel(
      # Select which Gender(s) to plot
      checkboxGroupInput(inputId = "GeneroN",
                         label = "Seleccionar genero:",
                         choices = c("Hombre" = "1", "Mujer" = "2"),
                         selected = "M"),
      sliderInput("distmrt",
                  "Años cumplidos:",
                  min = 0,
                  max = 120,
                  value = 30),
      sliderInput("canttiendas",
                  "Cantidad de tiendas:",
                  min = 0,
                  max = 10,
                  value = 1)
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
      textOutput("prediccion")
      # plotOutput("distPlot")
    )
  )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
  
  output$prediccion <- renderText({
    entrada <- data.frame(edad_casa=input$edadcasa,
                          dist_mrt=input$distmrt,
                          cant_tiendas=input$canttiendas)
    entrada_preprocesada <- scale(entrada, center = media_total,
                                  scale = desv_est_total)
    salida <- predict(modelo_knn_k4,newdata = entrada_preprocesada)
    return(salida)
    
  })
  
  # output$distPlot <- renderPlot({
  #     # generate bins based on input$bins from ui.R
  #     x    <- faithful[, 2]
  #     bins <- seq(min(x), max(x), length.out = input$bins + 1)
  # 
  #     # draw the histogram with the specified number of bins
  #     hist(x, breaks = bins, col = 'darkgray', border = 'white')
  # })
}

# Run the application 
shinyApp(ui = ui, server = server)
