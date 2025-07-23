import argparse
import pytest
from pathlib import Path
import os, sys

sys.path.append(str(Path(__file__).parent.parent.resolve()))

from . import run_neg, run_pos
import os, sys

import logger

logger = logger.set_logger(os.path.basename(__file__))

def run(config) :
    run_neg.preprocessing(config)
    run_pos.preprocessing(config)