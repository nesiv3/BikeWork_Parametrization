import redis
import os
from dotenv import load_dotenv

load_dotenv()

def get_redis_client():
    if not hasattr(get_redis_client, "_client"):
        REDIS_HOST = os.getenv("REDIS_URL")
        REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
        REDIS_USERNAME = os.getenv("REDIS_NAME", "").strip()
        REDIS_PASSWORD = os.getenv("REDIS_PASS", "").strip()
        pool = redis.ConnectionPool(
            host=REDIS_HOST,
            port=REDIS_PORT,
            username=REDIS_USERNAME,
            password=REDIS_PASSWORD,
            decode_responses=True,
            max_connections=10  # Ajusta según tus necesidades
        )
        get_redis_client._client = redis.Redis(connection_pool=pool)
    return get_redis_client._client

redis_client = get_redis_client()

