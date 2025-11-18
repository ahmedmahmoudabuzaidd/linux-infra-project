![Linux Infrastructure Banner](https://as2.ftcdn.net/v2/jpg/03/96/98/33/1000_F_396983381_AcuGFHQbNn7d9eercXFpOecN7d7B5F66.jpg)

# Linux Infrastructure Project 🐧💻

**Host Python App:** Frontend → Backend → Database → Monitoring (Zabbix)

End-to-end Linux infrastructure project with **5 VMs**:

- **Frontend VM** → Frontend code + Nginx (serves static + proxies API)  
- **Backend VM** → Backend code + Gunicorn + Nginx  
- **DB VM** → MariaDB/MySQL with dedicated user, secured configuration  
- **Zabbix VM** → Complete monitoring setup  
- **Backup VM** → Automated backup scripts  

---

## 🛠️ Tech Stack & Tools

![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black&style=for-the-badge) 
![Python](https://img.shields.io/badge/Python-306998?logo=python&logoColor=white&style=for-the-badge) 
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white&style=for-the-badge) 
![Nginx](https://img.shields.io/badge/Nginx-009639?logo=nginx&logoColor=white&style=for-the-badge) 
![MariaDB](https://img.shields.io/badge/MariaDB-003545?logo=mariadb&logoColor=white&style=for-the-badge) 
![Zabbix](https://img.shields.io/badge/Zabbix-1C62B9?logo=zabbix&logoColor=white&style=for-the-badge) 
![UFW](https://img.shields.io/badge/UFW-007ACC?style=for-the-badge) 
![Bash](https://img.shields.io/badge/Bash-4EAA25?logo=gnu-bash&logoColor=white&style=for-the-badge) 
![Gunicorn](https://img.shields.io/badge/Gunicorn-000000?logo=python&logoColor=white&style=for-the-badge) 

---

## ✅ Best Practices Applied

<details>
<summary>🔹 Database VM (`db-vm`)</summary>

- Runs MariaDB/MySQL with dedicated DB user (no root for apps)  
- Firewall restricts access to backend VM only  
- `bind-address = 0.0.0.0` for controlled external access  

</details>

<details>
<summary>🔹 Backend VM (`backend-vm`)</summary>

- Flask app served via Gunicorn (multi-worker)  
- Managed by systemd for reliability  
- Nginx reverse proxy in front of Gunicorn  
- Firewall allows only frontend VM traffic  
- Uses DNS names (no hardcoded IPs)  

</details>

<details>
<summary>🔹 Frontend VM (`frontend-vm`)</summary>

- Nginx serves static files (HTML, JS, CSS)  
- Proxies API requests (`/api/`) to backend VM  
- Clean JS code (no hardcoded backend IPs)  

</details>

<details>
<summary>🔹 Zabbix VM (`zabbix-vm`)</summary>

- Full monitoring setup included in `zabbix/` folder  
- Monitors CPU, RAM, Disk, Nginx, Gunicorn, DB, and network  
- Animated GIF for live monitoring dashboard:

![Monitoring GIF](https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif)  

</details>

<details>
<summary>🔹 Backup VM (`backup-vm`)</summary>

- Automated backup scripts  
- Secured backups stored on dedicated storage  
- Logs and cronjobs to ensure scheduled backups  

</details>

<details>
<summary>🔹 Networking & Security</summary>

- DNS names for all VMs (`frontend-vm`, `backend-vm`, `db-vm`, `zabbix-vm`)  
- UFW firewall rules per role (minimum exposure)  
- Tested DNS resolution between VMs  

</details>

---

## ⚡ Project Status

| Component | Status |
|-----------|--------|
| Frontend  | ✅ Working |
| Backend   | ✅ Working |
| DB        | ✅ Working |
| Zabbix    | ✅ Working |
| Backup    | ✅ Working |

---

## 📁 Project Structure


├─ frontend/

├─ backend/

├─ database/

├─ backup/

├─ zabbix/

└─ Guidebook (Step-by-Step Manual).pdf
