# ---------------------------
#   MinerU Global Dockerfile
# ---------------------------

FROM python:3.10-slim

WORKDIR /app

# Copia o repositório inteiro (não só /docker/global)
COPY ../../ /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    git wget curl build-essential libgl1 libglib2.0-0 \
 && rm -rf /var/lib/apt/lists/*

# Instala dependências Python do MinerU
RUN pip install --upgrade pip setuptools wheel
RUN pip install . --no-cache-dir

# Copia o script com o favicon
COPY app_with_favicon.py /app/app_with_favicon.py

# Variáveis de ambiente padrão
ENV MINERU_DEVICE_MODE=cpu
ENV MINERU_MODEL_SOURCE=local
ENV MINERU_FORMULA_ENABLE=true
ENV MINERU_TABLE_ENABLE=true

# Expõe a porta onde o app vai rodar
EXPOSE 30000

# Inicia o servidor FastAPI (app modificado com favicon)
CMD ["uvicorn", "app_with_favicon:app", "--host", "0.0.0.0", "--port", "30000"]
