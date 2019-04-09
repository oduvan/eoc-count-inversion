from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "count_inversion"
    FUNCTION_NAMES = {
        "python_3": "count_inversion",
        "js_node": "countInversion"
    }
    ENV_COVERCODE = {
        ENV_NAME.PYTHON: '''def cover(f, data):
    return f(tuple(data))'''
    }