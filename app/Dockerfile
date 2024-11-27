# Use uma imagem base do Python
FROM python:3.10-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie os arquivos para dentro do container
COPY app/ /app/

# Instale as dependências
RUN pip install -r requirements.txt

# Exponha a porta 5000
EXPOSE 5000

# Comando para rodar o Flask
CMD ["python", "app.py"]
