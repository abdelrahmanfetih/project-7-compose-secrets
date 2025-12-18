import os
import time
import redis

# Read configuration from environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
SLEEP_SECONDS = float(os.getenv("SLEEP_SECONDS", "1"))

# Required secret
APP_SECRET = os.getenv("APP_SECRET")
if not APP_SECRET:
    raise SystemExit("APP_SECRET is missing! Set it in .env (do not commit it).")

# Connect to Redis
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

print("App started successfully. Secret is set.")

while True:
    r.incr("counter")
    print("Counter:", r.get("counter").decode())
    time.sleep(SLEEP_SECONDS)
