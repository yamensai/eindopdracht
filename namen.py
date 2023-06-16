from faker import Faker
from classes import User

fake = Faker()

users = []
for i in range(1, 101):
    name = fake.first_name()
    surname = fake.last_name()
    user = User(id=i, name=name, surname=surname)
    users.append(user)

# Print the generated users
for user in users:
    print("User ID:", user.id)
    print("User Name:", user.name)
    print("User Surname:", user.surname)
    print() 