import os

from dotenv import load_dotenv

load_dotenv()

IEX_TOKEN = os.getenv("IEX_TOKEN")


def printenvironment():
    print(f"The client id is: {IEX_TOKEN}.")


if __name__ == "__main__":
    printenvironment()
