```bash
# 0. Navegar até o diretório do projeto (change to project directory)
cd /caminho/para/data-science-from-scratch
# cd (mudar diretório)

# 1. Ativar o ambiente virtual (activate the virtual environment)
# • Windows (cmd.exe):
.\.venv\Scripts\activate.bat     # activate.bat = script de ativação

# 2. (Opcional) Atualizar o pip (upgrade pip)
python -m pip install --upgrade pip  
# python -m pip = usa o pip do .venv
# --upgrade pip = atualiza o instalador de pacotes

# 3. Instalar ou atualizar dependências (install/update dependencies)
pip install -r requirements.txt   # -r requirements.txt = instalar tudo que está na lista
# ou para adicionar um pacote novo:
pip install nome_do_pacote        # installs a single package / instala pacote específico

# 4. Atualizar o arquivo de requisitos (update requirements.txt)
pip freeze > requirements.txt     # freeze = gerar lista de pacotes (+versões)

# 5. Desativar o ambiente virtual (deactivate the virtual environment)
deactivate                        # deactivate = retornar ao Python global
```