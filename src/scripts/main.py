import sys
sys.path.insert(0, '../src')

# Main function
from canva import TangramCanvas


def main():
    print("[Main]")
    canvas = TangramCanvas()
    canvas.start()


# Launch main function
if __name__ == "__main__":
    main()
