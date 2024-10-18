from os import environ as env
import multiprocessing

HOST = "127.0.0.1"
PORT = int(env.get("PORT", 5000))
DEBUG_MODE = int(env.get("DEBUG_MODE", 0))

# Gunicorn config
bind = ":" + str(PORT)
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()