from instabot import Bot # módulo que utiliza funções que existiam na API do Instagram que foi fechada em 2016
import os # módulo que permite interagir com o sistema operacional
import shutil # módulo que permite interagir com arquivos e diretórios
import json # módulo para aquivos json
from variaveis import * # importa variaveis globais
from os import path # importa a função path do módulo os


# PRIMEIRA PARTE
def login_instagram(): # função que faz login na conta do instagram
    with open('credenciais.json') as arquivo_dados: #abre arquivo com usuário e senha do perfil do insta
        dados = json.loads(arquivo_dados.read()) # lê arquivo json
        usuario = dados['username'] #procura username no arquivo json
        senha = dados['password']# procura senha no arquivo json
        bot.login(username = usuario, #utiliza as variáveis para logar
           password = senha)

#QUARTA PARTE
def deleta_pasta_config(): # função que deleta a pasta 'config' que o instabot cria
    if path.exists(CAMINHO): #checa se a pasta existe
        shutil.rmtree(CAMINHO) #remove a pasta

# TERCEIRA PARTE
def checagem_imagens():
    pasta_arquivos = CAMINHO_IMAGENS # caminho da pasta das imagens que vão ser feito o upload
    func_remove = 'REMOVE_ME' #atribui a uma variavel a string a ser procurada
    for nome_arquivo in os.listdir(pasta_arquivos): # itera sobre a pasta de imagens
        if func_remove in nome_arquivo: #procura arquivos com o a string func_remove
            arquivo = os.path.join(pasta_arquivos, nome_arquivo) #concatena o arquivo com o caminho
            tira_remove = arquivo.replace('REMOVE_ME', '') # retira o atributo remove_me criado pelo bot das imagens que foram postadas
            os.rename(arquivo,tira_remove) # renomeia


# SEGUNDA PARTE
def upload_fotos():
    pasta_arquivos = CAMINHO_IMAGENS # caminho da pasta das imagens que vão ser feito o upload
    for nome_arquivo in os.listdir(pasta_arquivos): # itera sobre a pasta de imagens
        arquivo = os.path.join(pasta_arquivos, nome_arquivo) # une os componentes do caminho de um arquivo para obter a localização de cada arquivo presente na pasta e iterar sobre eles
        nome_arquivo = nome_arquivo.replace('.jpg', '') # substitui o jpg na string que representa o nome do arquivo
        nome_arquivo = nome_arquivo.replace('-', ' ') # substitui o hífen na string que representa o nome do arquivo
        if os.path.isfile(arquivo):# checa se o arquivo apontado pelo os.path.join existe
            bot.upload_photo(arquivo, # bot faz upload do arquivo com a legenda
                caption =nome_arquivo)


deleta_pasta_config() # chama função que deleta a config
checagem_imagens() # chama a função que retira REMOVE_ME
bot = Bot() # chama a função bot do instabot
login_instagram() # chama a função de login do instagram
upload_fotos()# chama a função que faz upload de fotos
