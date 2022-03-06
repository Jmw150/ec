# Entry point into the list domain for dreamcoder. Just contains default arguments

# This is used for backwards compatibility with old EC that used batch training on multiple files
try:
    import binutil  # required to import from dreamcoder modules
except ModuleNotFoundError:
    import bin.binutil  # alt import if called as module

from dreamcoder.domains.list.main import main, list_options
from dreamcoder.dreamcoder import commandlineArguments
from dreamcoder.utilities import numberOfCPUs # detecting the number of CPUs


if __name__ == "__main__":
    args = commandlineArguments(
        enumerationTimeout=10,
        activation="tanh",
        iterations=10,
        recognitionTimeout=3600,
        a=3,
        maximumFrontier=10,
        topK=2,
        pseudoCounts=30.0,
        helmholtzRatio=0.5,
        structurePenalty=1.0,
        CPUs=numberOfCPUs(),
        extras=list_options,
    )
    main(args)
