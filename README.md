# Subscription Insight Engine

#### AI-powered decision support service that analyzes customer subscription behaviour and generates risk insights such as churn probability, usage anomalies, and retention recommendations.

#### This service is part of a distributed microservices platform that uses event-driven architecture to process subscription usage events and produce AI-driven insights.

---
### Tech Stack:
#### uvicorn - ASGI (Asynchronous Server Gateway Interface)
#### FastAPI - Web Framework
#### Pydantic - REST Validation, DTO json mapping.


---
Requires Python 3.11+
###  Create virtual environment
````bash

python -m venv venv
````

###  Activate virtual environment (mac)
````bash
source venv/bin/activate
````

###  Install dependencies
````bash
pip install -r requirements.txt
````

###  Run the application
````bash
uvicorn app.main:app --reload
````

### Check service is up!
http://localhost:8000/docs