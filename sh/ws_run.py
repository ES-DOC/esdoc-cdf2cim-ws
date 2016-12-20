# -*- coding: utf-8 -*-

"""
.. module:: run_web_service.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Runs cdf2cim web-service.

.. moduleauthor:: Mark A. Greenslade <momipsl@ipsl.jussieu.fr>

"""
import sys
import cdf2cim_ws


def _main():
    """Main entry point.

    """
    # Run web service.
    try:
        cdf2cim_ws.run()

    # Handle unexpected exceptions.
    except Exception as err:
        # Simple log to stdout.
        print err

        # Ensure that web-service is stopped.
        try:
            cdf2cim_ws.stop()
        except:
            pass

    # Signal exit.
    finally:
        sys.exit()


# Main entry point.
if __name__ == '__main__':
    _main()
