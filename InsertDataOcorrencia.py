import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as sa_orm
import ocorrencias as oc

endereco = "C:\\Users\\joaov\\OneDrive\\Documentos\\pucrs_pos_fullstack\\Banco de Dados Relacional\\Dados\\Exemplo\\"

# Lendo dados de arquivos
municipio = pd.read_csv(endereco + "municipio.csv", sep=",")

# Transformando os dados em um DataFrame
tbMunicipio = pd.DataFrame(municipio)

#Criando a engrenagem de conexão com o BD
engine = sa.create_engine("sqlite:///BD/ocorrencia.db")

#Criando um conexão variável de conexão com o BD
conn = engine.connect()

#Variável de definição de metadados, para identificar que estrutura será atualizada
metaData = sa.MetaData()
Sessao = sa_orm.sessionmaker(bind=engine) #Bind é um argumento que remete a vincular
session = Sessao()

#######################
# MUNICÍPIO 
#######################
#Algoritmo para inserção de dados, utilziando o DataFrame tbMunicipio
#Transforma os dados em uma lista, correlacionando os registros/linhas/tuplas, através do método dicionário (to_dict)
dadosMunicipio = tbMunicipio.to_dict(orient="records")
#Variável que representa a tabela que se deseja inserir os dados e, um metadados.
tabelaMunicipio = sa.Table(oc.Municipio.__tablename__, metaData, autoload_with=engine)
try:
    conn.execute(tabelaMunicipio.insert(), dadosMunicipio)
    session.commit()
except ValueError: 
    ValueError()    

print("tbMunicipio criada!")    