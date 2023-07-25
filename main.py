import logging
import logging.handlers
import os
from datetime import datetime
import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

if __name__ == "__main__":   
    logger.info(f"test message")
    logger.info(f"test message 2")
    
    #print out time
    time = datetime.now().strftime("%m-%d %H:%M:%S")
    print(time)
    print(f'::set-output name=time::{time}')#output variable value to GitHub action, old method will be deprecated.
    print(f'"time={time}" >> $GITHUB_OUTPUT')

    #print for testing artifacts
    print('this should show up in an artifact file')

    #write file out to be saved as artifact
    data = {'col 1':['A','B','C'],'col 2': [1, 2, 3]}
    df = pd.DataFrame(data)
    df.to_csv('test_artifact.csv')