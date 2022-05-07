import logging

def get_logger() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
 
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
       
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    
    logger.addHandler(ch)
    
    return logger

def func() -> None:
    logger = get_logger()
    logger.info("This is a log message")
    
if __name__ == "__main__":
    func()
