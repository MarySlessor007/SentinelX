# SentinelX v1.0

A lightweight Security Operations Center (SOC) monitoring platform built with Python that detects SSH brute-force attacks, enriches alerts using the MITRE ATT&CK framework, stores incidents in SQLite, and visualizes security events through a Flask-based dashboard.

---

## Dashboard

![SentinelX Dashboard](images/dashboard.png)

---

## Architecture

![Architecture](images/architecture.png)

---

## Features

* Parse Linux SSH authentication logs.
* Detect SSH brute-force attacks from repeated failed login attempts.
* Enrich alerts with MITRE ATT&CK technique mappings (T1110 – Brute Force).
* Store incidents in a SQLite database.
* Display alerts in a Flask-based SOC dashboard.
* Modular project structure for future detection rules.

---

## Technologies Used

* Python
* Flask
* SQLite
* HTML/CSS
* Git & GitHub
* MITRE ATT&CK Framework

---

## Project Structure

```text
SentinelX/
│
├── app/
├── database/
├── engine/
├── intelligence/
├── parser/
├── sample_logs/
├── web/
├── images/
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YourUsername/SentinelX.git
cd SentinelX
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Detection Engine

```bash
python -m app.main
```

---

## Running the Dashboard

```bash
python -m web.app
```

Open:

```text
http://127.0.0.1:5000
```

---

## Example Detection Output

![Detection Output](images/detection_terminal.png)

---

## MITRE ATT&CK Mapping

| Detection       | Technique           | Tactic            |
| --------------- | ------------------- | ----------------- |
| SSH Brute Force | T1110 – Brute Force | Credential Access |

---

## Future Improvements

* Additional attack detection rules
* Threat intelligence enrichment
* Interactive dashboards and filtering
* REST API for alerts
* Docker deployment
* Automated testing

---

## License

This project is licensed under the MIT License.
