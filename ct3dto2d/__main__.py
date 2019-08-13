import sys,os
from argparse import ArgumentParser
import logging
import warnings

from rttypes.volume import Volume, FrameOfReference
from pydicom.dicomio import dcmread

warnings.filterwarnings('ignore', category=UserWarning, module='pydicom', lineno=313)
logger = logging.getLogger(__name__)

def load_ctdata_from_NM(f):
    """load ct data from NM modality dicom and produce rttypes.volume.Volume"""
    dcm = dcmread(f)
    arr = dcm.pixel_array
    rescale_slope = dcm.get('RescaleSlope')
    rescale_int   = dcm.get('RescaleIntercept')
    arr = arr*rescale_slope + rescale_int
    logger.debug('array shape: {!s}'.format(arr.shape))
    logger.debug('array type: {!s}'.format(arr.dtype))
    logger.debug('array min/max: {:0.2f}/{:0.2f}'.format(arr.min(), arr.max()))
    detinfo = dcm.get('DetectorInformationSequence')[0]
    start = [float(x) for x in detinfo.get('ImagePositionPatient')]
    orient = [float(x) for x in detinfo.get('ImageOrientationPatient')]
    assert orient == [0,0,0,0,0,0]
    logger.debug('start: {!s}'.format(start))
    spacing = [float(x) for x in dcm.get('PixelSpacing')] + [float(dcm.get('SliceThickness'))]
    logger.debug('spacing: {!s}'.format(spacing))
    frame = FrameOfReference(start=start, spacing=spacing, size=arr.shape[::-1])
    logger.debug(str(frame))
    vol = Volume.fromArray(arr, frame)
    vol.modality = 'CT'
    return vol

def convert_dicom(infile, outdir):
    """entrypoint for conversion process"""
    # load data
    logger.info('Loading 3D DICOM Volume from "{!s}"'.format(infile))
    vol = load_ctdata_from_NM(infile)
    logger.debug(str(vol))

    # save data
    logger.info('Saving 2D DICOM Sequence to "{!s}"'.format(outdir))
    vol.toDicom(outdir)

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = ArgumentParser()
    parser.add_argument('infile', type=str, help='input CT image')
    parser.add_argument('-o', '--out', type=str, help='output directory')
    parser.add_argument('-L', '--loglevel', type=str, default='INFO', choices=list(logging._nameToLevel.keys()), help='set the logging level')
    args = parser.parse_args()

    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.setLevel(logging._nameToLevel[args.loglevel])

    # run conversion and save output
    infile = args.infile
    outfile = args.out
    convert_dicom(infile, outfile)

if __name__ == '__main__':
    main()
