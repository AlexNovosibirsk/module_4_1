
def divide(first, second):
    if second == 0:
        return "Ошибка"
    return first / second


def main():
    print("Main") # если запускать fake_math.py как current file, то эта функция сработает


if __name__ == "__main__":
    main()


print("from module_4_1")  # строка будет вызвана и при импорте тоже
