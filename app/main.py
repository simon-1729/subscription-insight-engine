import asyncio
from fastapi import FastAPI
from pydantic import BaseModel

from app.messaging.kafka.consumer import KafkaConsumerService
from app.config.settings import settings

app = FastAPI()

consumer = KafkaConsumerService(
    topic=settings.kafka_usage_topic,
    bootstrap_servers=settings.kafka_bootstrap_servers,
    group_id=settings.kafka_group_id
)

@app.on_event("startup")
async def startup_event():
    await consumer.start()
    async def handler(event):
        print("Received event:", event)

    asyncio.create_task(consumer.listen(handler))

@app.on_event("shutdown")
async def shutdown_event():
    await consumer.stop()
