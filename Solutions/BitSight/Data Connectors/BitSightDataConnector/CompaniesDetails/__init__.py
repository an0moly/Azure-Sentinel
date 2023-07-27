"""This __init__ file will be called once triggered is generated."""
import time
from ..SharedCode.logger import applogger
from .bitsight_companies import BitSight
import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    """Start the execution.

    Args:
        mytimer (func.TimerRequest): timer trigger
    """
    applogger.info("BitSight: Companies_Details: Start processing...")
    start = time.time()
    BitSight_obj = BitSight()
    BitSight_obj.get_bitsight_data_into_sentinel()
    end = time.time()
    applogger.info("BitSight: time taken for data ingestion is {} sec".format(int(end-start)))
    applogger.info("BitSight: Companies_Details: execution completed.")

    if mytimer.past_due:
        applogger.info("BitSight Connector: The timer is past due!")
