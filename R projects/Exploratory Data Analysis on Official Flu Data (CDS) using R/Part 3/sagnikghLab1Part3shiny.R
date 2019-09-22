#install.packages("shinyWidgets")
#install.packages("shinythemes")
library(shiny)
library(shinyWidgets)
library(datasets)
library(shinythemes)


# App URL: https://sagnikgh-dic-lab1.shinyapps.io/FluHeatmap/


ui <- fluidPage(theme = shinytheme("superhero"),
                titlePanel("Data Intensive Computing: Lab 1: Part3"),
                
                sidebarLayout(
                  sidebarPanel(
                    helpText("Select Heatmap from below list"),
                    
                    selectInput("var", 
                                label = "Choose:",
                                choices = c("2018-19 Seasonal CDC HeatMap vs 2019 Jan 4th Weekly CDC HeatMap" = "cdc0",
                                            "2018-19 Seasonal CDC HeatMap vs Twitter(#flu, #illness, #disease, #Influenza)" = "cdc1",
                                            "2019 Jan 4th Week CDC HeatMap vs Twitter(#flu, #illness, #disease, #Influenza)" = "cdc2",
                                            "#Influenza vs #Fluseason" = "flu1",
                                            "#Flushot vs #Fluseason" = "flu2",
                                            "#Flushot vs #Influenza" = "flu3"),
                                selected = "Percent White")
                  ),
                  
                  #mainPanel(plotOutput("map"))
                  mainPanel(imageOutput("myImage"))
                  
                  
                  
                )
)                          

server <- function(input, output) {
  output$myImage <- renderImage({
    
    
    switch(input$var,
           "cdc0" = list(src = 'AverageVSLastweek.png', contentType = 'image/png', width = 840, height = 840),
           "cdc1" = list(src = 'CDCvsTwitter.png', contentType = 'image/png', width = 840, height = 840),
           "cdc2" = list(src = 'CDCvsTwitter(Last Week).png', contentType = 'image/png', width = 840, height = 840),
           "flu1" = list(src = 'InfluVSseason.png', contentType = 'image/png', width = 840, height = 840),
           "flu2" = list(src = 'shotVSseason.png', contentType = 'image/png', width = 840, height = 840),
           "flu3" = list(src = 'InfluenzaVSFlushot.png', contentType = 'image/png', width = 840, height = 840)
           
    )
    
    
    
  }, deleteFile = FALSE)
  
  
  
}                           



shinyApp(ui, server)
