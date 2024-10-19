from flask_frozen import Freezer
from main import app  # Certifique-se de que 'main' é o nome do seu módulo principal

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
