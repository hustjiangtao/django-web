# -*- coding: utf-8 -*-
# -*- author: Jiangtao -*-

"""tinyfy by tinypng api for .png & .jpg files
# pipenv install tinyfy
"""


import logging
import traceback
import tinify

from django.conf import settings


tinify.key = settings.TINYFY_KEY


def buffer_tinyfy(source_data):
    """source_data=source.read()"""
    try:
        # Use the Tinify API client.
        result_data = tinify.from_buffer(source_data).to_buffer()
    except tinify.AccountError as e:
        # print("The error message is: %s" % e.message)
        # Verify your API key and account limit.
        logging.warning(traceback.format_exc())
    except tinify.ClientError as e:
        # Check your source image and request options.
        logging.warning(traceback.format_exc())
    except tinify.ServerError as e:
        # Temporary issue with the Tinify API.
        logging.warning(traceback.format_exc())
    except tinify.ConnectionError as e:
        # A network connection error occurred.
        logging.warning(traceback.format_exc())
    except Exception as e:
        # Something else went wrong, unrelated to the Tinify API.
        logging.warning(traceback.format_exc())
    else:
        compressions_this_month = tinify.compression_count
        logging.info("this month tinyfy: %s, left: %s", compressions_this_month, 500 - compressions_this_month)
        if compressions_this_month < 100:
            logging.warning("this month tinyfy: %s, left: %s", compressions_this_month, 500 - compressions_this_month)
        return result_data

    return source_data
