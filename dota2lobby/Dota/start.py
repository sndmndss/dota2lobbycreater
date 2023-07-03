import logging
import main
logging.basicConfig(format='[%(asctime)s] %(levelname)s %(name)s: %(message)s', level=logging.DEBUG)

if __name__ == '__main__':
    main.init()