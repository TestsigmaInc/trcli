import sys
import click
from trcli.cli import *
from trcli.cli import Environment
from click.core import Context

import trcli.api
import trcli.api.results_uploader
from trcli.readers.junit_xml import JunitParser

from xml.etree.ElementTree import ParseError
from junitparser import JUnitXmlError
import multiprocessing
from trcli.commands import *
import traceback

# Ensure proper handling of multiprocessing in frozen executables
if __name__ == "__main__":

    # Set multiprocessing start method
    multiprocessing.set_start_method('forkserver', force=True)

    # Execute CLI
    print("Executing CLI")
    cli()
    print("Completed Executing CLI")
