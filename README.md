# My Shopping Application

This project is a distributed application featuring a Django backend and a Solid.js frontend. It demonstrates cloud-native development principles, Docker containerization, and Kubernetes orchestration.

## Technologies
- Django
- Solid.js
- Docker & Docker Compose
- Kubernetes

### 12-Factor Principles Applied

1. **Codebase**: Ein Git-Repository für die gesamte Anwendung.
2. **Dependencies**: Alle Abhängigkeiten sind in `requirements.txt` (Backend) und `package.json` (Frontend) klar definiert.
3. **Configuration**: Konfigurationen werden nicht im Code hartkodiert, sondern über Umgebungsvariablen und `.env` Dateien bereitgestellt.
4. **Backing Services**: Alle externen Dienste sind über Umgebungsvariablen definiert, keine festen URLs.
5. **Build, Release, Run**: Das Projekt wird in Docker-Containern ausgeführt, wodurch die Trennung von Build, Release und Run gewährleistet ist.
6. **Processes**: Die Anwendung läuft als stateless Prozesse in Containern.
7. **Port Binding**: Die Anwendung verwendet PORT-Umgebungsvariablen zum Binden der Ports.
8. **Concurrency**: Skalierbarkeit wird durch Kubernetes Deployments unterstützt.
9. **Disposability**: Container können jederzeit gestartet oder gestoppt werden.
10. **Dev/Prod Parity**: Die Entwicklungs- und Produktionsumgebung sind durch Docker und Kubernetes weitgehend identisch.
11. **Logs**: Logs werden in der Standardausgabe der Container gespeichert und können durch Docker oder Kubernetes gelesen werden.
12. **Admin Processes**: Verwaltungsaufgaben, wie z.B. Migrationen, werden manuell durch den Container durchgeführt.
