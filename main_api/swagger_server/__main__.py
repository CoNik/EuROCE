#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from flask_cors import CORS
import os

def main():
    options = {"swagger_path": os.path.join(os.path.dirname(os.path.realpath(__file__)),"..","swagger-ui"), "swagger_ui_config": {"openapi_spec_url": "http://localhost:8080/api/swagger.json"}}
    app = connexion.App(__name__, specification_dir='./swagger/', options=options)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Fake News Hammer public API'})
    CORS(app.app)
    app.run(port=8080)


if __name__ == '__main__':
    main()
