import sqlalchemy as sa
import sqlalchemy.orm as sa_orm

engine = sa.create_engine("sqlite:///BD//ocorrencia.db") # Conexão com o banco de dados
base = sa_orm.declarative_base() # Base de dados

#tabela DP 
class Departamento(base):
	__tablename__ = "tbDP" # Nome da tabela
	id = sa.Column(sa.INTEGER, primary_key=True, index = True) # ID do departamento
	nome = sa.Column(sa.VARCHAR(100), nullable=False) # Nome do departamento
	endereco = sa.Column(sa.VARCHAR(255), nullable=False) # Endereço do departamento

#tabela Responsavel Pelo DP
class ResponsavelDP(base): 
	__tablename__ = "tbResponsavelDP" # Nome da tabela
	id = sa.Column(sa.INTEGER, primary_key=True, index = True) # ID do responsável pelo departamento
	id_tbDP = sa.Column(sa.INTEGER, sa.ForeignKey("tbDP.id", ondelete="NO ACTION", onupdate="CASCADE")) # ID do departamento
	delegado = sa.Column(sa.VARCHAR(100), nullable=False) # Nome do delegado

#Tabela Municipio
class Municipio(base):
	__tablename__ = "tbMunicipio" # Nome da tabela
	id = sa.Column(sa.INTEGER, primary_key=True, index = True) # ID do município ou código IBGE
	municipio = sa.Column(sa.VARCHAR(100), nullable=False) # Nome do município
	regiao = sa.Column(sa.VARCHAR(25), nullable=False) # Nome da região

#Tabela Ocorrencia
class Ocorrencia(base):
	__tablename__ = "tbOcorrencia" # Nome da tabela
	id = sa.Column(sa.INTEGER, primary_key=True, index = True) # ID da ocorrência
	id_tbDP = sa.Column(sa.INTEGER, sa.ForeignKey("tbDP.id", ondelete="NO ACTION", onupdate="CASCADE")) # ID do departamento
	id_tbMunicipio = sa.Column(sa.INTEGER, sa.ForeignKey("tbMunicipio.id", ondelete="NO ACTION", onupdate="CASCADE")) # ID do município
	ano = sa.Column(sa.CHAR(4), nullable=False) # Ano da ocorrência
	mes = sa.Column(sa.VARCHAR(2), nullable=False) # Mês da ocorrência
	ocorrencia = sa.Column(sa.VARCHAR(100), nullable=False) # Descrição da ocorrência
	quantidade = sa.Column(sa.INTEGER, nullable=False) # Quantidade de ocorrências

try:
	base.metadata.create_all(engine) # Criação das tabelas no banco de dados
	print("Tabelas criadas com sucesso!")
except Exception as e:
	print(f"Erro ao criar tabelas: {e}")
finally:
	engine.dispose()