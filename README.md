# SentinelHub

SentinelHub is a security monitoring dashboard that demonstrates how synthetic security events can be generated, processed, and displayed through a simple web application.

## Features

- Flask backend API
- Security health-check endpoint
- Synthetic security-event generator
- Security events API
- Web-based monitoring dashboard
- Automated backend tests
- CORS support for frontend communication

## Project Structure

```text
sentinelhub/
├── backend/
│ ├── __init__.py
│ ├── app.py
│ ├── generate_events.py
│ ├── requirements.txt
│ └── routes.py
├── data/
│ └── events.json
├── docs/
│ ├── .gitkeep
│ └── architecture.md
├── frontend/
│ ├── index.html
│ ├── script.js
│ └── style.css
├── tests/
│ └── test_app.py
└── README.md
