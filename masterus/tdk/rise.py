import logging
import os
import pathlib

import dotenv
import numpy as np

# import plotly.express as px
from flask import Flask, jsonify, render_template, request, send_file, send_from_directory, session
from icecream import ic

from flask_session import Session
from masterus.tdk import prime

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)

# np.random.seed(22)

logger = logging.getLogger(__name__)

dotenv.load_dotenv()

app = Flask(
    __name__,
    template_folder="build",
    static_folder="build",
    root_path=pathlib.Path(os.getcwd()) / "masterus",
)
app.secret_key = "masterus"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

logger.info("NEW INSTANCE is created")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    if path != "" and os.path.exists(app.static_folder + "/" + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")


app.add_url_rule("/ping", methods=["GET"], view_func=prime.ping)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777)
