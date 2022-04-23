#carregando biblioteca
library(neuralnet)

#criando uma base de dados
dado.um =    c(30, 50, 30, 20, 20, 47, 78, 79)
dado.dois =  c(10, 24, 12, 11, 17, 16, 19, 55)
dado.saida = c(1, 1, 0, 0, 0, 1, 1, 0)

#convertendo em um data frame
df = data.frame(dado.um, dado.dois, dado.saida)
#viasualização dos dados
View(df)
#criação de uma rede neural (dados de saída em função de dados um e dados dois)
neural.net = neuralnet(dado.saida~dado.um+dado.dois, 
                       hidden = c(4, 2), data = df, act.fct = 'logistic', 
                       likelihood = TRUE, lifesign = 'full')
#separando um pedaço para teste
df.test = df[1:3,1:2]
#realizando uma predição
predicao = compute(neural.net, df.test)
#plotando a rede neural criada
plot(neural.net)
