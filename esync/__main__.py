import sys

import logbook
import yaml

from . import app

log = logbook.Logger(__name__)


def main():
    logbook.StreamHandler(sys.stdout, level='WARNING').push_application()
    logbook.FileHandler('esync.log', level='DEBUG').push_application()
    config = yaml.load(open('esync.yaml'))
    log.debug('loaded config: {}', config)

    a = app.App(config)
    for path in a.scan():
        a.add(path)
    a.commit()


if __name__ == '__main__':
    main()
