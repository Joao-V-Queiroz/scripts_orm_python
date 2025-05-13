import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ocorrencias as oco
from sqlalchemy import or_

engine = sa.create_engine("sqlite:///BD//ocorrencia.db")
Session = orm.sessionmaker(bind=engine)
session = Session()

# Suponha que o Delegado da Delegacia de Roubos e Furtos de Veículos tenha te solicitado uma
# análise relacionada ao ranqueamento de todas as DPs, através da quantidade total de
# ocorrências relacionadas a Roubo e furto de Veículos, no Interior do Estado do RJ (é preciso
# verificar como o dado está cadastrado na tabela, para realizar o filtro!!!!).
# O resultado desse ranqueamento deve ser enviado em uma tabela, contendo as seguintes
# colunas:
# • DP
# • Total

qtdRouboFurtoVeiculos = pd.DataFrame(
	session.query(
		oco.Departamento.nome.label("DP"),
  		oco.Ocorrencia.ocorrencia.label("Ocorrência"),
		sa.func.sum(oco.Ocorrencia.quantidade).label("Total")
	).join(
		oco.Ocorrencia, 
		oco.Ocorrencia.id_tbDP == oco.Departamento.id
    ).join(
		oco.Municipio, 
		oco.Ocorrencia.id_tbMunicipio == oco.Municipio.id
    ).filter(
        oco.Municipio.regiao == "Interior",
        or_(
            oco.Ocorrencia.ocorrencia.like("%roubo_veiculo%"),
            oco.Ocorrencia.ocorrencia.like("%furto_veiculo%")
        )
    ).group_by(
		oco.Departamento.nome
	).order_by(
		sa.func.sum(oco.Ocorrencia.quantidade).desc()
	).all()
)

print(qtdRouboFurtoVeiculos)