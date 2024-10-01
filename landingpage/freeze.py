from flask_frozen import Freezer
from index import app

# app.config['FREEZER_BASE_URL'] = 'https://web.uni-miskolc.hu/~matpi/jmathpi/'
app.config['FREEZER_RELATIVE_URLS'] = True


freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
