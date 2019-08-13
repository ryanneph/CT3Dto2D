# CT3Dto2D
This is a simple utility that converts a single dicom file into a set of dicom files. Why do we want to do this? Most CT datasets are represented as a folder of 2D axial slices of the full volume. Sometimes, we encounter a single 3D volume packed into a single dicom file instead, which doesn't play nicely with many dicom viewers/tools.

## Installation
This package should be installed into your default python environment (or a virtualenv if you prefer), using the command:
```
pip install git+https://github.com/ryanneph/CT3Dto2D.git
```

## Module
This module provides a function: `convert_dicom` which can be imported into 3rd party code and used directly for automation. To do so, first install this module as described above, then in your python script you can follow the example below:
```python
from ct3dto2d import convert_dicom

if __name__ == '__main__':
	input_file = '<PATH TO 3D DICOM FILE>'
	output_dir = '<OUTPUT DIRECTORY FOR 2D SLICES>'
	convert_dicom(input_file, output_dir)
```

## Command Line Script
This module also provides a command line tool which can be run with the command:
```
ct3dto2d "<INPUT_FILE>" --out "<OUTPUT_DIRECTORY>"
```
