from yacs.config import CfgNode as CN

_C = CN()

#Substrate feature extractor
_C.DRUG = CN()
_C.DRUG.NODE_IN_FEATS = 75
_C.DRUG.PADDING = True
_C.DRUG.HIDDEN_LAYERS = [128, 128, 128]
_C.DRUG.NODE_IN_EMBEDDING = 128


# Enzyme feature extractor
_C.PROTEIN = CN()
_C.PROTEIN.NAME = "ESM_MLP_650M"
_C.PROTEIN.IN_DIM = 1280
_C.PROTEIN.HIDDEN_DIM = 640
_C.PROTEIN.TARGET_DIM = 128

# MLP decoder
_C.DECODER = CN()
_C.DECODER.NAME = "MLP"
_C.DECODER.IN_DIM = 128
_C.DECODER.HIDDEN_DIM = 256
_C.DECODER.OUT_DIM = 64
_C.DECODER.BINARY = 1

# SOLVER
_C.SOLVER = CN()
_C.SOLVER.MAX_EPOCH = 100
_C.SOLVER.BATCH_SIZE = 64
_C.SOLVER.NUM_WORKERS = 0
_C.SOLVER.LR = 5e-5
_C.SOLVER.SEED = 42
_C.SOLVER.DATA = ""
_C.SOLVER.SAVE = ""

_C.RESULT = CN()
_C.RESULT.OUTPUT_DIR = './results'

_C.CCFM = CN()
_C.CCFM.DIM = 128
_C.CCFM.RATIO = 0.5

_C.BCFM = CN()
_C.BCFM.DIM = 128

_C.STAGE = CN()
_C.STAGE.CCFM = False
_C.STAGE.BCFM = False
_C.STAGE.NUM = 1

def get_cfg_defaults():
    return _C.clone()
