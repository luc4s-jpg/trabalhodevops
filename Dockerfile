# Imagem base leve do Python
FROM python:3.11-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas os arquivos necessários inicialmente (para cache otimizado)
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação
COPY . .

# Expõe a porta da API (default do uvicorn)
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
