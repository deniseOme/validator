from __future__ import print_function, absolute_import
import argparse
import logging
import sys

from evsvalidator.helpers import file_or_resource, url_to_tmpfile
from evsvalidator.validator import validate


def main():
    logging.config.fileConfig(file_or_resource('logging.ini'),
                              disable_existing_loggers=False)
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description='OpenTargets evs validator')
    parser.add_argument('data_source_file', nargs='?', default='-',
                        help='The prefix to prepend default: STDIN')
    parser.add_argument("--schema", dest='schema',
                        help="set the schema file to use",
                        action='store')
    parser.add_argument("--log-level", dest='loglevel',
                        help="set the log level",
                        action='store', default='WARNING')
    args = parser.parse_args()

    if args.loglevel:
        try:
            root_logger = logging.getLogger()
            root_logger.setLevel(logging.getLevelName(args.loglevel))
            logger.setLevel(logging.getLevelName(args.loglevel))
        except Exception, e:
            root_logger.exception(e)

    if not args.schema:
        logger.error('A --schema <schemafile> has to be specified.')
        return 1
    
    if args.data_source_file == '-':
        validate(sys.stdin,args.schema)
    else:
        with url_to_tmpfile(args.data_source_file) as fh:
            validate(fh,args.schema)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())