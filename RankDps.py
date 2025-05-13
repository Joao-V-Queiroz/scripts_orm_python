import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ocorrencias as oco

engine = sa.create_engine("sqlite:///BD//ocorrencia.db")
Session = orm.sessionmaker(bind=engine)
session = Session()

# Suponha que o Secretário de Estado de Polícia Civil te solicitou para apresentar um
# ranqueamento de todas as Delegacias de Polícia, localizadas no Interior, através da
# quantidade de ocorrências.

# Query para obter o ranqueamento das Delegacias de Polícia no Interior
dataQuery = pd.DataFrame(
    session.query(
        oco.Departamento.nome.label("DP"),
        sa.func.sum(oco.Ocorrencia.quantidade).label("Quantidade de Ocorrências")    
    ).join(
        oco.Ocorrencia,
        oco.Ocorrencia.id_tbDP == oco.Departamento.id # Associa a tabela de ocorrências com a tabela de departamentos
    ).join(
        oco.Municipio,
        oco.Ocorrencia.id_tbMunicipio == oco.Municipio.id # Associa a tabela de ocorrências com a tabela de municípios
    ).filter(
        oco.Municipio.regiao == "Interior"
    ).group_by(
        oco.Departamento.nome
    ).order_by(
        sa.func.sum(oco.Ocorrencia.quantidade).desc()
    ).all()
)
# Aqui a indentação do print
print(dataQuery)