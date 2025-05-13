import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ocorrencias as oco

engine = sa.create_engine("sqlite:///BD//ocorrencia.db")
Session = orm.sessionmaker(bind=engine)
session = Session()
 
# Suponha que o Governador do Estado do RJ tenha te ligado e solicitado uma análise
# relacionada ao ranqueamento de todos os municípios, através da quantidade total de
# ocorrências relacionadas a Roubo de Veículos (é preciso verificar como o dado está cadastrado
# na tabela, para realizar o filtro!!!!)
qtdRouboVeiculos = pd.DataFrame(
	session.query(
		oco.Municipio.municipio.label("Municipio"),
        oco.Municipio.regiao.label("Regiao"),
        oco.Ocorrencia.ocorrencia.label("Ocorrência"),
        sa.func.sum(oco.Ocorrencia.quantidade).label("Quantidade de Ocorrências")
	).join(
		oco.Ocorrencia,
        oco.Ocorrencia.id_tbMunicipio == oco.Municipio.id 
	).where(
		oco.Ocorrencia.ocorrencia.like("%roubo_veiculo%")
	).group_by(
		oco.Municipio.municipio,
		oco.Municipio.regiao
	).order_by(
		sa.func.sum(oco.Ocorrencia.quantidade).desc()
	).all()
)

print(qtdRouboVeiculos)