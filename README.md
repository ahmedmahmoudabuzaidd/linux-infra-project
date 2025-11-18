![Linux Infrastructure Banner](https://as2.ftcdn.net/v2/jpg/03/96/98/33/1000_F_396983381_AcuGFHQbNn7d9eercXFpOecN7d7B5F66.jpg)

# Linux Infrastructure Project 🖥️🐧

**Host Python App:** Frontend → Backend → DB → Monitoring (Zabbix)

End-to-end Linux infrastructure project with **5 VMs**:

- **Frontend VM** → Frontend code + Nginx (serves static + proxies API)  
- **Backend VM** → Backend code + Gunicorn + Nginx  
- **DB VM** → MariaDB/MySQL with dedicated user, secured configuration  
- **Zabbix VM** → Full monitoring setup (Zabbix folder included)  
- **Backup VM** → Data backup scripts and automation  

---

## ✅ Best Practices Applied

### Database VM (`db-vm`)
- Runs MariaDB/MySQL with dedicated DB user (no root for apps)  
- Firewall restricts access to backend VM only  
- `bind-address=0.0.0.0` for controlled external access  

### Backend VM (`backend-vm`)
- Flask app via Gunicorn (multi-worker)  
- Managed by systemd for reliability  
- Nginx reverse proxy in front of Gunicorn  
- Firewall allows only frontend VM traffic  
- Uses DNS names (no hardcoded IPs)  

### Frontend VM (`frontend-vm`)
- Nginx serves static files (HTML, JS, CSS)  
- Proxies API requests (`/api/`) to backend VM  
- Clean JS code (no hardcoded backend IPs)  

### Networking
- DNS names for all VMs (`frontend-vm`, `backend-vm`, `db-vm`, `zabbix-vm`)  
- UFW firewall rules per role (minimum exposure)  
- Tested DNS resolution between VMs  

### Zabbix VM (`zabbix-vm`)
- Complete Zabbix setup included in `zabbix/` folder  
- Monitors CPU, RAM, Disk, Nginx, Gunicorn, DB, and network health  

### Production Readiness
- Logs collected from Nginx, Gunicorn, MySQL  
- Proper multi-layer separation: Frontend → Backend → DB  
- No direct DB access from frontend  
- Least privilege configuration everywhere  

⚡ **Project Status:** Frontend, Backend, DB, and Zabbix monitoring fully implemented

---

## 🛠️ Tech Stack & Tools

- **Web & App:** Nginx, Flask, Gunicorn  
- **Database:** MariaDB/MySQL  
- **Monitoring:** Zabbix (complete folder included)  
- **Automation & Networking:** Linux CLI, Bash scripts, DNS setup, UFW firewall  
- **Programming:** Python, HTML, CSS, JS  

---

## 📁 Project Structure

