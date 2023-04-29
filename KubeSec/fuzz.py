import traceback
from typing import Any, List

import numpy as np

from parser import checkIfValidHelm
from parser import keyMiner
from parser import getKeyRecursively
from parser import getValuesRecursively
from parser import getValsFromKey


def fuzz(method, fuzzed_arguments: List[Any]):
    for arguments in fuzzed_arguments:
        try:
            rslt = method(*arguments)
        except Exception as exc:
            print(f"FUZZ: {method.__name__} FAILED")
            traceback.print_exc()
        else:
            print(f"FUZZ: {method.__name__} PASSED ({rslt})")


if __name__ == "__main__":
    fuzzTargets = [
        (
            checkIfValidHelm, [
                (None, None),
                (5, 2),
                (17.0, 24.0),
                ([], {}),
                ("no-filename", "yes"),
            ]
        ),
        (
            keyMiner, [
                (None, None),
                ("bad", "arguments"),
                ([], {}),
                (float("inf"), float("inf")),
                (float("-inf"), float("inf")),
                (1j, 1),
                (np.NAN, np.NAN)
            ]
        ),
        (
            getKeyRecursively, [
                ([]),
                (None, 5),
                (None, 2.0),
                (None, "non-iterable"),
                (None, [None, None, None]),
                (None, []),
                (None, np.zeros((6, 70))),
            ]
        ),
        (
            getValuesRecursively, [
                (None,),
                (7,),
                (2.0,),
                ([],),
                ({},),
                ("good-model-name",),
            ]
        ),
        (
            getValsFromKey, [
                (4, 2, None,),
                (None, None, 0,),
                ("doesnt", "matter", 5.0,),
                (float("-inf"), float("inf"), [],),
                ([], [], {},),
                ([], [], "bad-name",),
            ]
        )
    ]
    for method, fuzzed_arguments in fuzzTargets:
        fuzz(method, fuzzed_arguments)
