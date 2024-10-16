from flask import Flask
from flask import render_template
import logging
import logging.handlers
from pythonjsonlogger import jsonlogger

app = Flask(__name__)

# Logger
app_logger = logging.getLogger(__name__)

# Disable werkzeug logger to hide startup and HTTP requests
werkzeug_logger = logging.getLogger("werkzeug")
werkzeug_logger.disabled = True

# Basic format and config
logger_format = "%(asctime)s: %(levelname)s - PID=%(process)d | %(message)s"
logging.basicConfig(filename='log', level=logging.DEBUG, format=logger_format)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/debug")
def log_debug():
    app_logger.debug("Log Debug")
    return "";

@app.route("/info")
def log_info():
    app_logger.info("Log Info")
    return "";

@app.route("/warning")
def log_warning():
    app_logger.warning("Log Warning")
    return "";

@app.route("/error")
def log_error():
    app_logger.error("Log Error")
    return "";




