from mlir.ir import Context, Module, Location, InsertionPoint
from mlir.dialects import func


def test1_context():
    with Context():
        # IR construction using `ctx` as context.

        # For example, parsing an MLIR module from string requires the context.
        module = Module.parse("builtin.module {}")
        print(module)


def test2_createop():
    with Context():
        with Location.unknown():
            module = Module.create()
            with InsertionPoint(module.body):
                func.FuncOp("main", ([], []))
            print(module)


def test3_numpy():
    """
    The function is to test whether a native Python library,
    specifically, NumPy, works well in the environment
    """
    import numpy as np

    print(np.__version__)


if __name__ == "__main__":
    test1_context()
    test2_createop()
