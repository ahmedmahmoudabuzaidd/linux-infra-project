# linux-infra-project

Host Python App: Frontend - Backend - DB - Monitoring

End-to-end Linux infrastructure project with 4 VMs:

Frontend VM → frontend code + Nginx (serves static + proxies API).

Backend VM → backend code + Gunicorn + Nginx.

DB VM → MariaDB/MySQL with dedicated user, secured configuration.

Zabbix VM → monitoring setup (in progress).

✅ Best Practices Applied
🔹 Database VM (db-vm)

Runs MariaDB/MySQL.

Uses a dedicated database user (no root for apps).

Firewall restricts access (only backend VM can connect).

bind-address = 0.0.0.0 for controlled external access.

🔹 Backend VM (backend-vm)

Runs Flask app via Gunicorn (multi-worker).

Managed with systemd service for reliability.

Nginx reverse proxy in front of Gunicorn.

Firewall allows only frontend VM traffic.

Uses DNS names (no hardcoded IPs).

🔹 Frontend VM (frontend-vm)

Nginx serves static files (HTML, JS, CSS).

Proxies API requests (/api/) to backend VM.

Uses DNS names for backend connection.

JavaScript code cleaned (no hardcoded backend IP).

🔹 Networking

All VMs use DNS names (frontend-vm, backend-vm, db-vm, zabbix-vm).

UFW firewall rules per role (minimum exposure).

Tested DNS resolution between VMs.

🔹 Production Readiness

Logs collected from Nginx, Gunicorn, MySQL.

Proper multi-layer separation:

Frontend → Backend → DB.

No direct DB access from frontend.

Secure least privilege configuration everywhere.

⚡ Project Status: Frontend, Backend, DB setup working. Zabbix monitoring setup in progress.
