import logging

logging.basicConfig(filename='logTest.log', level=logging.INFO)


def main():
    mathFail = 1 / 1
    logging.info("mathFail")


main()
