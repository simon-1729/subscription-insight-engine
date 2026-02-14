# Subscription Insight Engine

### AI-powered decision support service that analyzes customer subscription behaviour and generates risk insights such as churn probability, usage anomalies, and retention recommendations.

### This service is part of a distributed microservices platform that uses event-driven architecture to process subscription usage events and produce AI-driven insights.


````bash
pip install -r requirements.txt
````


````bash
uvicorn app.main:app --reload
````

#### Check service is up!
http://localhost:8000/docs