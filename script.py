from datetime import datetime, timedelta

feriados = ['12/02/2024','13/02/2024','14/02/2024',
'19/03/2024','25/03/2024','29/03/2024','21/04/2024',
'01/05/2024','30/05/2024','15/08/2024','07/09/2024',
'12/10/2024','02/11/2024','15/11/2024','24/12/2024',
'25/12/2024', '26/12/2024','27/12/2024','28/12/2024',
'29/12/2024','30/12/2024','31/12/2024','01/01/2025']

def calcular_data_futura(data_inicio, semanas):

    data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y')
    # Adicionando o número de semanas especificado à data atual
    data_futura = data_inicio + timedelta(weeks=semanas)

    return data_futura.strftime("%d/%m/%Y")

# Usando a função para calcular 11 semanas a partir de hoje
termino_planejamento = calcular_data_futura('02/03/2024',12)
print("Última aula de Planejamento e Estratégia é:", termino_planejamento)
termino_copy = calcular_data_futura(termino_planejamento,10)
print("Última aula de Copywriting é:", termino_copy)
termino_design = calcular_data_futura(termino_copy,13)
print("Última aula de Design e Video é:", termino_design)
termino_trafego = calcular_data_futura(termino_design,13)
print("Última aula de Tráfego e Performance é:", termino_trafego)

