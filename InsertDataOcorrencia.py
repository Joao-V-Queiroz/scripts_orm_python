#acessando o arquivo vendedor.csv
import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import ocorrencias as oc

#variável para armazenar o endereço
#OBS: NA SUA CASA, VOCÊ PRECISA ALTERAR PAR AO ENDEREÇO DO SEU COMPUTADOR!!!
endereco = "C:\\Users\\joaov\\OneDrive\\Documentos\\pucrs_pos_fullstack\\Banco de Dados Relacional\\Dados\\Exemplo\\"

#variáveis com o nome dos arquivos de dados
municipio = pd.read_csv(endereco + "municipio.csv",sep=",")

#Coleta os dados dos arquivos para dentro do Python
tbMunicipio = pd.DataFrame(municipio)

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
DadosMunicipio = tbMunicipio.to_dict(orient='records')

#Inserindo dados a partir de uma conexão com a engrenagem de BD
try:
    query = sa.text("INSERT INTO tbMunicipio (id, municipio, regiao) VALUES (:id, :municipio, :regiao)")
    conn.execute(query, DadosMunicipio)  # Insere todos os registros
    conn.commit()
    sessao.commit()
    print("Todos os registros foram inseridos com sucesso!")
except Exception as e:
    print(f"Erro ao inserir múltiplos registros: {e}")
    
#Encerrando as sessões abertas
sessao.close()
engine.dispose()
print("Módulo de inserção de dados finalizado!")