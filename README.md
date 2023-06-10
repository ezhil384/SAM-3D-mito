# SAM-3D-mito
3D instance segmentation of mitochondria using SAM

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [To-Do](#to-do)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ezhil384/SAM-3D-mito.git
2. Change directory:
   ```bash
   cd SAM-3D-mito
3. Import the environment from the YAML file:
   ```bash
   conda env create -f environment.yaml
4. Create and activate a new virtual environment (optional before the above step):
   ```bash
   python -m venv env
   source env/bin/activate
   
## Usage

To run the 3D processing algorithm on SAM png predictions

1. Clone the repository:
   ```bash
   git clone https://github.com/donglaiw/imutil
2. Follow the steps for installation of imutils:
   ```bash
    cd imutil
    conda create -n imu python==3.7
    source activate imu
    conda install pip cython numpy
    pip install --editable .
    python setup.py build_ext --inplace
3. Run the python file for the creation of 3D instances (change the paths in the file):
   ```bash
    python tests/test_seg.py      
