# from app.models import db, Magazine, News, Publications

# def seed_magazines(app):
#     with app.app_context():
#         # Очистка таблиц, связанных с журналами
#         db.session.query(News).delete()  # Очищаем таблицу News
#         db.session.query(Publications).delete()  # Очищаем таблицу Publications
#         db.session.query(Magazine).delete()  # Очищаем таблицу Magazine
#         db.session.commit()

#         # Добавляем тестовые журналы
#         magazine1 = Magazine(name="Журнал 1")
#         magazine2 = Magazine(name="Журнал 2")
#         magazine3 = Magazine(name="Журнал 3")

#         db.session.add(magazine1)
#         db.session.add(magazine2)
#         db.session.add(magazine3)
#         db.session.commit()
#         print("Тестовые журналы успешно добавлены в базу данных!")

# # if __name__ == "__main__":
# #     seed_magazines()