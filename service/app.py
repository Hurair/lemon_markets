import connexion
from swagger_ui_bundle import swagger_ui_3_path


def create_app():
    """
    Connexion is based on Flask , so it creates a FlaskApp
    :return: connexion.App
    """
    options = {
        'swagger_path': swagger_ui_3_path,
        'swagger_url': 'docs',
    }
    app = connexion.App(__name__, options=options, specification_dir='api/spec/')
    app.add_api('api.yaml')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
