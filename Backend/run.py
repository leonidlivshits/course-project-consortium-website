from app import create_app
from seed_all import seed_all
app = create_app()

def seed_test_scrypts():
    """Функция для запуска всех скриптов заполнения базы данных."""
    with app.app_context():
        seed_all(app)

if __name__ == '__main__':
    import sys
    if '--seed' in sys.argv:
        seed_test_scrypts()
    app.run(host='0.0.0.0', port=5000)