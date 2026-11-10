import redis
from fastapi import APIRouter
from typing import Any
redis_instance = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True,
    legacy_responses=False,
    max_connections=20,
    socket_connect_timeout=2,
    socket_timeout=1,
)
router = APIRouter(
    prefix='/redis',
    tags=['Redis']
)

@router.post(path="/set-cache")
async def set_cache(cache_key: str, cache_value: str, ttl: int = 3600):
    """_summary_

    Args:
        cache_key (str): _description_
        value (any): _description_
        ttl (int): **expiry time in seconds**

    Returns:
        _type_: _description_
    """
    return redis_instance.set(name=cache_key, value=cache_value, ex=ttl)

@router.post("/set-hash-cache")
async def set_hashed_cache(cache_key: str, data: dict[str, Any], ttl: int = 3600):
    """Sets the specified fields to their respective values in the hash stored at key.

    Args:
        cache_key (str): _Unique cache key_
        data (dict[str, any]): _Key value mapping_
        ttl (int): Expiry time

    Returns:
        _type_: _description_
    """
    return redis_instance.hset(cache_key, mapping=data, ttl=ttl)