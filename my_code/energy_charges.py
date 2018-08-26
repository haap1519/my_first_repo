import pandas as pd


def energy_consump(file_path):
    """Returns the sum of energy consumption."""
    data=pd.read_excel(file_path)
    return data.Energy.sum()
