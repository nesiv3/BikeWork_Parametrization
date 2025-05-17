import redis

redis_client = redis.Redis(
    host='redis-13803.c282.east-us-mz.azure.redns.redis-cloud.com',
    port=13803,
    decode_responses=True,
    username="BikeWork_APP",
    password="Mantenimiento123.*",
)

success = redis_client.set('foo', 'bar')
# True

result = redis_client.get('foo')
print(result)
# >>> bar