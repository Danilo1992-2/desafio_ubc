from app.commands.processar_arquivo import processar_arquivo
import pandas as pd



def teste_processar_arquivo():
    df_teste: pd.DataFrame = pd.DataFrame([{
                            "nome nao formatado":"Nome_teste",
                            "idadé":11,
                            "seriâ":6,
                            "nota media":7.2,
                            "endereço":"456 Oak St",
                            "nome do pai":"Bob Smith",
                            "nome da Mae":"Alice Smith",
                            "data De_nascimento":"2012-08-21T00:00:00Z"},
    {                            "nome nao formatado":"Nome_teste",
                            "idadé":11,
                            "seriâ":6,
                            "nota media":7.2,
                            "endereço":"456 Oak St",
                            "nome do pai":"Bob Smith",
                            "nome da Mae":"Alice Smith",
                            "data De_nascimento":"2012-08-21T00:00:00Z"},
    {                            "nome nao formatado":"Nome_teste",
                            "idadé":11,
                            "seriâ":6,
                            "nota media":7.2,
                            "endereço":"456 Oak St",
                            "nome do pai":"Bob Smith",
                            "nome da Mae":"Alice Smith",
                            "data De_nascimento":"2012-08-21T00:00:00Z"}

        ]
        
    )
    processar_arquivo(df_teste)
