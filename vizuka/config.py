"""
Here are the default parameters used in all the package
There are 1.path 2.filenames 3.learning parameters
"""
import os

#
# ALL DEFAULT PATH
#


def path_builder(base_path):
    folders = [
        os.path.join(base_path, relative) for relative in [
            'set/',
            'reduced/',
            'models/',
            'graph/',
            'cache/',
            'saved_clusters/',
        ]
    ]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
    return folders


# Build all path from one base
BASE_PATH = os.path.join(os.path.dirname(__file__), 'data/')

(
    DATA_PATH,
    REDUCED_DATA_PATH,
    MODEL_PATH,
    GRAPH_PATH,
    CACHE_PATH,
    SAVED_CLUSTERS_PATH,
) = path_builder(BASE_PATH)

#
# ALL DEFAULT FILENAME
#

# File containing data to be t-SNEed
INPUT_FILE_BASE_NAME = 'preprocessed_inputs_'
RAW_NAME = 'raw_data_'

# default RN for predictions
DEFAULT_PREDICTOR = 'predict_'

# PROJECTIONS DATA will have a named generated from the algo projector parameters

# A version is a string added to the end of each filename
VERSION = 'MNIST_example'

#
#  LEARNING PARAMETERS
#

# Dimension reduction default parameters :
DEFAULT_PROJECTOR = 'tsne'
PROJECTION_DEFAULT_PARAMS = {
    'tsne': {
        'perplexity': 50,
        'learning_rate': 1000,
        'n_iter': 12000,
    },
    'pca': {
        'nb_dimension': 2,
        'min_ratio_variance_explained': -1,
    },
}

NAME_VALUE_SEPARATOR = '@@'
PARAMETERS_SEPARATOR = '#'
