#acessando o arquivo vendedor.csv
import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ocorrencias as oc

#variável para armazenar o endereço
endereco = "C:\\Users\\joaov\\OneDrive\\Documentos\\pucrs_pos_fullstack\\Banco de Dados Relacional\\Dados\\Exemplo\\"

#variáveis com o nome dos arquivos de dados
municipio = pd.read_csv(endereco + "municipio.csv",sep=",")
departamento = pd.read_csv(endereco + "DP.csv",sep=",")
responsavelDP = pd.read_excel(endereco + "ResponsavelDP.xlsx",sheet_name="ResponsavelDP")
ocorrencia = pd.read_excel(endereco + "Ocorrencias.xlsx")
# print(ocorrencia.head()) 

#Coleta os dados dos arquivos para dentro do Python
tbMunicipio = pd.DataFrame(municipio)
tbDP = pd.DataFrame(departamento)
tbResponsavelDP = pd.DataFrame(responsavelDP)

#Criando a engrenagem de conexão com o BD
engine = sa.create_engine("sqlite:///BD//ocorrencia.db")

#testar a conexão com o banco de dados 
try:
    conn = engine.connect()
    print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar ao banco: {e}")


#Variável de definição de metadados, para identificar que estrutura será atualizada
metaData = sa.MetaData()

#iniciando um sessão com o banco de dados
Sessao = orm.sessionmaker(bind=engine) #Bind é um argumento que remete a vincular
sessao = Sessao()

#######################
# MUNICÍPIO 
#######################
#Algoritmo para inserção de dados, utilziando o DataFrame tbMunicipio
#Transforma os dados em uma lista, correlacionando os registros/linhas/tuplas, através do método dicionário (to_dict)
#DadosMunicipio = tbMunicipio.to_dict(orient='records')

#Inserindo dados a partir de uma conexão com a engrenagem de BD
# try:
#     query = sa.text("INSERT INTO tbMunicipio (id, municipio, regiao) VALUES (:id, :municipio, :regiao)")
#     conn.execute(query, DadosMunicipio)  # Insere todos os registros
#     conn.commit()
#     sessao.commit()
#     print("Todos os registros de município foram inseridos com sucesso!")
# except Exception as e:
#     print(f"Erro ao inserir múltiplos registros em tbMunicipio: {e}")
    
#######################
# DEPARTAMENTO 
#######################
#Algoritmo para inserção de dados, utilziando o DataFrame tbDP
#Transforma os dados em uma lista, correlacionando os registros/linhas/tuplas, através do método dicionário (to_dict)    
#DadosDepartamento = tbDP.to_dict(orient='records')

#Inserindo dados a partir de uma conexão com a engrenagem de BD
# try:
#     query = sa.text("INSERT INTO tbDP (id, nome, endereco) VALUES (:id, :nome, :endereco)")
#     conn.execute(query, DadosDepartamento)  # Insere todos os registros
#     conn.commit()
#     sessao.commit()
#     print("Todos os registros de departamento foram inseridos com sucesso!")
# except Exception as e:
#     print(f"Erro ao inserir múltiplos registros em tbDP: {e}")
    
#######################
# RESPONSÁVEL PELO DEPARTAMENTO 
#######################
#Algoritmo para inserção de dados, utilziando o DataFrame tbResponsavelDP
#Transforma os dados em uma lista, correlacionando os registros/linhas/tuplas, através do método dicionário (to_dict)       
# DadosResponsavelDP = tbResponsavelDP.to_dict(orient='records')
# try:
#     query = sa.text("INSERT INTO tbResponsavelDP (id, id_tbDP, delegado) VALUES (:id, :id_tbDP, :delegado)")
#     conn.execute(query, DadosResponsavelDP)  # Insere todos os registros
#     conn.commit()
#     sessao.commit()
#     print("Todos os registros de responsável pelo departamento foram inseridos com sucesso!")
# except Exception as e:
#     print(f"Erro ao inserir múltiplos registros em tbResponsavelDP: {e}")

#######################
# OCORRÊNCIA 
#######################
#Algoritmo para inserção de dados, utilziando o DataFrame tbOcorrencia
#Transforma os dados em uma lista, correlacionando os registros/linhas/tuplas, através do método dicionário (to_dict)       
DadosOcorrencia = ocorrencia.to_dict(orient='records')
try:
    query = sa.text("INSERT INTO tbOcorrencia (id, id_tbDP, id_tbMunicipio, ano, mes, ocorrencia, quantidade) VALUES (:id, :id_tbDP, :id_tbMunicipio, :ano, :mes, :ocorrencia, :quantidade)")
    conn.execute(query, DadosOcorrencia)  # Insere todos os registros
    conn.commit()
    sessao.commit()
    print("Todos os registros de ocorrência foram inseridos com sucesso!")
except Exception as e:
    print(f"Erro ao inserir múltiplos registros em tbOcorrencia: {e}")
        
#Encerrando as sessões abertas
sessao.close()
engine.dispose()
print("Módulo de inserção de dados finalizado!")