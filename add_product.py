from sport import app, db, Product, User


def add_products():
    if not User.query.first():
        user = User(username="admin")
        user.set_password("admin123")
        db.session.add(user)

    db.session.commit()
    print("База данных создана!")


if __name__ == '__main__':
    add_products()