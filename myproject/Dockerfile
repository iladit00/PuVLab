# Basis-Image verwenden
FROM python:3.10-slim

# Setzen des Arbeitsverzeichnisses im Container
WORKDIR /app

# System-Abhängigkeiten installieren
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Kopieren der Anforderungen (requirements.txt)
COPY requirements.txt /app/

# Installieren der Python-Abhängigkeiten
RUN pip install --upgrade pip && pip install -r requirements.txt

# Kopieren des gesamten Projekts in das Arbeitsverzeichnis
COPY . /app/

# Setzen der Umgebungsvariablen
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Migrationsbefehl ausführen und statische Dateien sammeln
RUN python manage.py collectstatic --noinput || echo "collectstatic failed, continuing anyway"

# Port freigeben
EXPOSE 8000

# Starten des Django Development Servers
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
