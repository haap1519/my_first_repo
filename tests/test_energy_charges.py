import math
from my_code.energy_charges import energy_consump

from pathlib import Path
FILE_PATH = Path('data/WSP_nrg_consump.xlsx')


def test_energy_consump():
    assert math.isclose(410401.48, energy_consump(FILE_PATH))