C:\Users\ronal_000\PycharmProjects\projetos\iotpy


mydata = input ("digite o nome do dataset \n")
var1 = input ("digite o valor da primeira variavel \n")
var2 = input ('digite o valor d asegunda variavel \n')

print(" ubidots -t A1E-0DjPaKAdlqg8BkUXMIJSQpWhjXCmiU -d ",mydata," set '{\"variableOne\":",var1,", \"variableTwo\":",var2,"}' ")