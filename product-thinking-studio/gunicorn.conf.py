"""
Gunicorn configuration for Render.com free tier
Optimized for 512MB RAM limit
"""
import multiprocessing
import os

# Bind to port specified by environment or default to 10000
bind = f"0.0.0.0:{os.getenv('PORT', '10000')}"

# Workers: 1 worker for free tier to conserve memory
workers = 1

# Worker class - sync is more stable for free tier
worker_class = "sync"

# Threads per worker - helps handle concurrent requests with less memory
threads = 2

# Timeout settings - prevent workers from hanging
timeout = 120
keepalive = 5

# Graceful timeout for worker shutdown
graceful_timeout = 30

# Max requests before worker restart (helps with memory leaks)
max_requests = 1000
max_requests_jitter = 100

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Preload app to save memory
preload_app = True

# Worker tmp directory - use /tmp for free tier
worker_tmp_dir = "/dev/shm" if os.path.exists("/dev/shm") else "/tmp"

# Prevent workers from being killed too quickly
worker_connections = 1000

def on_starting(server):
    """Called just before the master process is initialized."""
    print("Starting Gunicorn server...")

def on_reload(server):
    """Called to recycle workers during a reload via SIGHUP."""
    print("Reloading Gunicorn server...")

def when_ready(server):
    """Called just after the server is started."""
    print("Gunicorn server is ready. Spawning workers...")

def worker_int(worker):
    """Called when worker receives SIGINT or SIGQUIT signal"""
    print(f"Worker {worker.pid} interrupted")

def worker_abort(worker):
    """Called when a worker is killed"""
    print(f"Worker {worker.pid} aborted")
