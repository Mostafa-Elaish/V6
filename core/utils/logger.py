import logging, os
def get_logger(name='jarvis'):
    os.makedirs('data/logs', exist_ok=True)
    logging.basicConfig(filename='data/logs/jarvis.log', level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s')
    return logging.getLogger(name)
