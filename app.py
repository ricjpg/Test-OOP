from classes import DbMongo
from dotenv import load_dotenv
import pprint


def main():
    printer = pprint.PrettyPrinter()
    client, db = DbMongo.getDB()



    client.close()


if __name__ == "__main__":
    load_dotenv()
    main()

