import logging
import os
from pathlib import Path

import random_name
from flask import jsonify, render_template, request, send_file, session
from icecream import ic

logger = logging.getLogger(__name__)

cache_dir = Path(os.getcwd()) / ".cache"


def ping():
    response = [
        {
            "api": "http://10.110.195.2:7227",
            "title": "Кластеризатор",
            "description": ["May the odds be ever in your favor"],
        },
        {
            "api": "http://10.110.195.2:7227",
            "title": "Кластеризатор",
            "description": ["May the odds be ever in your favor"],
        },
        {
            "api": "http://10.110.195.2:7227",
            "title": "Кластеризатор",
            "description": ["May the odds be ever in your favor"],
        },
    ]
    return jsonify(response)


__all__ = ["ping"]
