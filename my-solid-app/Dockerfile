# Basis-Image verwenden
FROM node:16-alpine

# Arbeitsverzeichnis erstellen
WORKDIR /app

# Abhängigkeiten kopieren und installieren
COPY package.json package-lock.json ./
RUN npm install

# Quellcode kopieren
COPY . .

# Anwendung builden
RUN npm run build

# Port freigeben
EXPOSE 3000

# Starten des Produktionsservers
CMD ["npm", "run", "serve"]
