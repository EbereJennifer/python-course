import main_demo  # innerhalb main_demo: __name__ hat Wert "main_demo"

# print(__name__)

def main():
    print("Das ist unsere zweite main-funktion heute")


if __name__ == "__main__":
    main()
    # main_demo.main()  man könnte auch andere main Funktion aufrufen, ist aber nicht empfolen

print(__name__)
