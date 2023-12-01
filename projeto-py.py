pip install pandas

import pandas as pd
from datetime import datetime
from datetime import timedelta

db_model = {
    "nome_paciente": [],
    "idade": [],
    "sexo": [],
    "enfermidade": [],
    "urgencia": [],
    "hora_chegada": [],
    "hora_max_atendimento": [],
    "dia_atendimento": []
}

df = pd.DataFrame(db_model)


def ordered_pacients():
    return df.sort_values(by=["dia_atendimento", "hora_max_atendimento"])

ordered_pacients()


def new_pacient():
    nome = str(input("Digite o nome do paciente:"))
    idade = str(input("Digite a idade do paciente:"))
    genero = str(input("Digite o genero do paciente:"))
    enfermidade = str(input("Digite a enfermidade do paciente:"))

    db_model["nome_paciente"].append(nome)
    db_model["idade"].append(idade)
    db_model["sexo"].append(genero)
    db_model["enfermidade"].append(enfermidade)

    if enfermidade == 'dor de cabeca':
        urgencia = 3
        db_model["urgencia"].append(urgencia)
    elif enfermidade == 'febre':
        urgencia = 2
        db_model["urgencia"].append(urgencia)
    elif enfermidade == 'hemorragia':
        urgencia = 1
        db_model["urgencia"].append(urgencia)
    else:
        urgencia = int(input('Qual o nivel da urgencia?'))
        db_model["urgencia"].append(urgencia)


    date_time = datetime.now()
    date = date_time.strftime('%d/%m/%Y - %H:%M')
    db_model["hora_chegada"].append(date)


    def handle_date_time(urgencia):
        uma_hora = timedelta(hours=1)
        trianta_min = timedelta(minutes=30)
        dez_min = timedelta(minutes=10)

        if urgencia == 3:
            new_date = date_time + uma_hora
        elif urgencia == 2:
            new_date = date_time + trianta_min
        elif urgencia == 1:
            new_date = date_time + dez_min
        elif urgencia == 0:
            new_date = date_time
        else:
            new_date = date_time + uma_hora

        return new_date
    
    new_time = handle_date_time(urgencia).strftime('%H:%M')
    db_model["hora_max_atendimento"].append(new_time)

    new_date = handle_date_time(urgencia).strftime('%d/%m/%Y')
    db_model["dia_atendimento"].append(new_date)
    
new_pacient()

df = pd.DataFrame(db_model)
ordered_pacients()


def delete_pacient():
    pacient_index = int(input('Digite o numero do paciente.'))
    df.drop([pacient_index], inplace=True)

delete_pacient()