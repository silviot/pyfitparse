from pyfitparse.model import FitFile


def parse_fit_data(data):
    ":param data: is a string with the fit file content"
    return FitFile(records=())