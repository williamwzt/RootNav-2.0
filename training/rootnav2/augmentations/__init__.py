import logging
from rootnav2.augmentations.augmentations import *
print ('Augmentations are on')
logger = logging.getLogger('rootnav2')

key2aug = {'gamma': AdjustGamma,
           'hue': AdjustHue,
           'brightness': AdjustBrightness,
           'saturation': AdjustSaturation,
           'contrast': AdjustContrast,
           'rcrop': RandomCrop,
           'hflip': RandomHorizontallyFlip,
           'vflip': RandomVerticallyFlip,
           'scale': Scale,
           'rsize': RandomSized,
           'rsizecrop': RandomSizedCrop,
           'rotate': RandomRotate,
           'translate': RandomTranslate,
           'ccrop': CenterCrop,}

def get_composed_augmentations(aug_dict):
    if aug_dict is None:
        logger.info("Using No Augmentations")
        return None

    augmentations = []
    for aug_key, aug_param in aug_dict.items():
        augmentations.append(key2aug[aug_key](aug_param))
        logger.info("Using {} aug with params {}".format(aug_key, aug_param))
    return Compose(augmentations)


