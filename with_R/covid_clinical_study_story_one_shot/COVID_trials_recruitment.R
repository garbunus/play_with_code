library(tidyverse)
library(ggplot2)
library(readxl)
library(lubridate)
library(zoo)

#leitura da base de dados
df <- read_excel('cid_B34.xlsx')
#dando uma olhada nos tipos de dados que temos e seus resumos
summary(df)


df$mes <- month(df$HR_ATENDIMENTO)
df$ano <- year(df$HR_ATENDIMENTO)

#filtrando dados por CID específico e criando um dataframe
df_u <- df %>% subset(df$`CID Admissão...14` == "B342") %>% tibble()
#convertando datas para um formato mês/ano
df_u$peri <- zoo::as.yearmon(df_u$HR_ATENDIMENTO)

#criando marcadores no eixo X para as linhas verticais para o projeto A
datas_eventos_A   = as.Date(c('2021-09-01', '2021-12-01', '2022-02-01'))
datas_eventos_A   = zoo::as.yearmon(datas_eventos_A)

#criando marcadores no eixo X para as linhas verticais para o projeto B
datas_eventos_B   = as.Date(c('2021-10-01', '2021-11-01'))
datas_eventos_B   = zoo::as.yearmon(datas_eventos_B)

#Criando labels para as linhas verticais
labels_eventos_A  = c('PROJETO A inicio recrutamento', 'PROJETO A fim recrutamento ANTECIPADO', 'PROJETO A expectativa recrutamento')
labels_eventos_B  = c('PROJETO B ATIVAÇÃO','PROJETO B inicio recrutamento')

#agrupando por período (mes-ano) e contando ocorrências
df2 <- df_u %>% group_by(peri) %>% count()

#construção do grafico com GGPLOT 2
plotagem <- ggplot(df2, aes(x=peri, y=n)) +
            geom_line(color='gray', size=0.5, alpha=0.8) +
            geom_vline(xintercept=datas_eventos_A, linetype=4, color='red', size=1, alpha=0.7) +
            geom_vline(xintercept=datas_eventos_B, linetype=2, color='purple', size=1, alpha=0.7) +
            geom_text(data=df2, mapping=aes(x=peri, label=n)) +
            annotate(geom = "text",
                     label = labels_eventos_A,
                     x = datas_eventos_A,
                     y = c(400, 370, 400),
                     angle = 90, 
                     vjust = 1.5) +
            annotate(geom = "text",
                     label = labels_eventos_B,
                     x = datas_eventos_B,
                     y = c(400, 400),
                     angle = 90, 
                     vjust = 1.5) +
            labs(title = 'Casos de COVID-19 -  2021-2022', x = 'Mês e ano', y = 'Número de Casos') +
            theme_light() 

#plotando o gráfico
plotagem
