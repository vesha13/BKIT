from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import faker



def main():
    fake = faker.Faker('ru_RU')
    r = Rectangle("синего", 20, 20)
    c = Circle("зеленого", 20)
    s = Square("красного", 20)
    print(r)
    print(c)
    print(s)

    print(fake.name())

if __name__ == "__main__":
    main()
