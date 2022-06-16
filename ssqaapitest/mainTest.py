from ssqaapitest.src.utilities.jsonUtility import JsonUtility
import logging as logger

if __name__ == '__main__':
    jsonR = JsonUtility('TSD_ConsumerService')
    logger.debug(jsonR.read_Json('Test.json'))
    