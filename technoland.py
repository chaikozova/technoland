import os
from logging.handlers import RotatingFileHandler

from flask import Flask, render_template, Config, logging

app = Flask(__name__)


class Config(object):
    # ...
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    def create_app(config_class=Config):
        # ...
        if not app.debug and not app.testing:
            # ...

            if app.config['LOG_TO_STDOUT']:
                stream_handler = logging.StreamHandler()
                stream_handler.setLevel(logging.INFO)
                app.logger.addHandler(stream_handler)
            else:
                if not os.path.exists('logs'):
                    os.mkdir('logs')
                file_handler = RotatingFileHandler('logs/microblog.log',
                                                   maxBytes=10240, backupCount=10)
                file_handler.setFormatter(logging.Formatter(
                    '%(asctime)s %(levelname)s: %(message)s '
                    '[in %(pathname)s:%(lineno)d]'))
                file_handler.setLevel(logging.INFO)
                app.logger.addHandler(file_handler)

            app.logger.setLevel(logging.INFO)
            app.logger.info('Microblog startup')

        return app


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

