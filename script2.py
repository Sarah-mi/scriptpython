from datetime import datetime, timedelta

feriados = ['18/02/2023', '20/02/2023', '21/02/2023','25/03/2023', 
            '07/04/2023','21/04/2023', '01/05/2023', '08/06/2023',
            '07/07/2023','12/10/2023', '02/11/2023', '15/11/2023',
            '22/12/2023', '23/12/2023', '25/12/2023', '26/12/2023',
            '27/12/2023', '28/12/2023', '29/12/2023', '30/12/2023',
            '01/01/2024', '12/02/2024', '13/02/2024', '14/02/2024',
            '19/03/2024', '25/03/2024', '29/03/2024', '21/04/2024',
            '01/05/2024', '30/05/2024', '15/08/2024', '07/09/2024',
            '12/10/2024', '02/11/2024', '15/11/2024', '24/12/2024',
            '25/12/2024', '26/12/2024', '27/12/2024', '28/12/2024',
            '29/12/2024', '30/12/2024', '31/12/2024', '01/01/2025', 
            '01/03/2025', '03/03/2025', '04/03/2025','19/03/2025', 
            '25/03/2025', '18/04/2025', '19/04/2025', '21/04/2025', 
            '01/05/2025', '19/06/2025', '15/11/2025','24/12/2025', 
            '25/12/2025', '26/12/2025', '27/12/2025', '28/12/2025', 
            '29/12/2025', '30/12/2025', '31/12/2025', '01/01/2026',
            ]

def calcular_data_futura(data_inicio, semanas, feriados=[]):
    data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y')
    data_futura = data_inicio + timedelta(weeks=semanas)
    
    # Considerar feriados
    while data_futura.strftime('%d/%m/%Y') in feriados:
        data_futura += timedelta(days=1)

    return data_futura.strftime("%d/%m/%Y")

def calcular_datas_turmas(turmas):
    datas_turmas = {}

    for turma, modulos in turmas.items():
        datas_modulos = {}
        data_atual = None

        for modulo, (data_inicio, semanas) in modulos.items():
            if data_atual:
                data_inicio = calcular_data_futura(data_atual, 1)
            data_termino = calcular_data_futura(data_inicio, semanas, feriados)
            datas_modulos[modulo] = (data_inicio, data_termino)
            data_atual = data_termino

        datas_turmas[turma] = datas_modulos

    return datas_turmas

# Exemplo de entrada com módulos para cada turma
turmas = {
    'MD19': {
        'Planejamento': ('20/02/2024', 12),
        'Copywriting': ('', 10),
        'Design': ('', 13),
        'Tráfego': ('', 13)
    },
    
    
    # Adicione mais turmas conforme necessário
}

datas_turmas = calcular_datas_turmas(turmas)

for turma, modulos in datas_turmas.items():
    print(f"\nTurma {turma}:")
    for modulo, (inicio, termino) in modulos.items():
        print(f"  - Módulo {modulo}: Início - {inicio}, Término - {termino}, Apresentação Final - {termino}")
