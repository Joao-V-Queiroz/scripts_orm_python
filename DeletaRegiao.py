import sqlalchemy as sa
import sqlalchemy.orm as sa_orm
import pandas as pd
import ocorrencias as oco

# Conexão com o banco de dados
engine = sa.create_engine("sqlite:///BD//ocorrencia.db") # Conexão com o banco de dados
metaData = sa.MetaData()
metaData.reflect(engine)

# Obtendo a tabela Município
tbMunicipio = metaData.tables[oco.Municipio.__tablename__]

# Atualizando a região
deleteRegiao = sa.delete(tbMunicipio).where(tbMunicipio.c.regiao == "Rio de Janeiro")

# Executando a atualização corretamente
with engine.connect() as conn:
    try:
        conn.execute(deleteRegiao)
        conn.commit()  # Confirma a transação no banco
        print("Região deletada com sucesso!")
    except Exception as e:
        print(f"Erro ao deletar a região: {e}")