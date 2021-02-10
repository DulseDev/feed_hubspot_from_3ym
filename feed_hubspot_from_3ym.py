import logging
import utils
from manager_3yourmind import requestsForQuote, quotes, orders

def feed_rfq(conn, cursor):
    logger = logging.getLogger()
    try:
        logging.info('Get requests for quote hub.dulse.fr')
        rfqs = requestsForQuote.get()
    except Exception as e:
        logging.error('Get requests for quote hub.dulse.fr: %s', str(e))
        raise e
    for rfq in rfqs:
        # TODO a coder
        if is_rfq_already_in_hubspot(rfq):
            continue
        try:
            # TODO a coder
            create_rfq_in_hubspot(rfq)
            # TODO a coder
            log_db_create_rfq_hubspot(rfq, conn, cursor)
        except Exception as e:
            log_db_create_rfq_hubspot(rfq, conn, cursor, error=str(e))
            logging.error('create request for quote in hubspot: %s', rfq['fullName'])

def feed_quote(conn, cursor):
    logger = logging.getLogger()
    try:
        logging.info('Get quotes hub.dulse.fr')
        quotes = quotes.get()
    except Exception as e:
        logging.error('Get quotes hub.dulse.fr: %s', str(e))
        raise e
    for quote in quotes:
        # TODO a coder
        if is_quote_already_in_hubspot(rfq):
            continue
        try:
            # TODO a coder
            create_quote_in_hubspot(rfq)
            # TODO a coder
            log_db_create_rfq_hubspot(rfq, conn, cursor)
        except Exception as e:
            log_db_create_rfq_hubspot(rfq, conn, cursor, error=str(e))
            logging.error('create quote in hubspot: %s', quote['fullName'])


if __name__ == '__main__':
    # log setup
    FORMAT = '%(asctime)-15s %(levelname)s: %(message)s'
    DATEFMT = '%d/%m/%Y %H:%M:%S'
    FILENAME = 'slice_new_quotes.log'
    logging.basicConfig(format=FORMAT,
            level=logging.INFO,
            datefmt=DATEFMT)
    logging.info('Start')
    try:
        conn, cursor = utils.get_conn_cursor()
    except Exception as e:
        logging.error('Get conn cursor dulse database: %s', str(e))
        sys.exit(1)
    try:
        logging.info('Feed requests for quote')
        feed_rfq(conn, cursor)
    except Exception as e:
        logging.error('Feed requests for quote: %s', str(e))
    try:
        logging.info('Feed quotes')
        # TODO a coder
        feed_quotes(conn, cursor)
    except Exception as e:
        logging.error('Feed quotes: %s', str(e))
    try:
        logging.info('Feed orders')
        # TODO a coder
        feed_orders(conn, cursor)
    except Exception as e:
        logging.error('Feed orders: %s', str(e))
    logging.info('Close conn cursor dulse database')
    cursor.close()
    conn.close()
