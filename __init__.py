from .SVD_Aspect_Ratio import NODE_CLASS_MAPPINGS as NODE_CLASS_MAPPINGS_AR, NODE_DISPLAY_NAME_MAPPINGS as NODE_DISPLAY_NAME_MAPPINGS_AR
from .SVD_Styler import NODE_CLASS_MAPPINGS as NODE_CLASS_MAPPINGS_ST, NODE_DISPLAY_NAME_MAPPINGS as NODE_DISPLAY_NAME_MAPPINGS_ST
from .SVD_Advanced import NODE_CLASS_MAPPINGS as NODE_CLASS_MAPPINGS_AD, NODE_DISPLAY_NAME_MAPPINGS as NODE_DISPLAY_NAME_MAPPINGS_AD

NODE_CLASS_MAPPINGS = {**NODE_CLASS_MAPPINGS_AR, **NODE_CLASS_MAPPINGS_ST, **NODE_CLASS_MAPPINGS_AD}
NODE_DISPLAY_NAME_MAPPINGS = {**NODE_DISPLAY_NAME_MAPPINGS_AR, **NODE_DISPLAY_NAME_MAPPINGS_ST, **NODE_DISPLAY_NAME_MAPPINGS_AD}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

