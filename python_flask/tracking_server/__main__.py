#!/usr/bin/env python3

import connexion

from tracking_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Tracking API'}, pythonic_params=True)
    app.run(port=8765)


if __name__ == '__main__':
    main()
