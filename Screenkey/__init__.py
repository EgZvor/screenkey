from collections import OrderedDict
import gettext
gettext.install('screenkey', unicode=True)

# Screenkey version
APP_NAME = "Screenkey"
APP_DESC = _("Screencast your keys")
APP_URL = 'https://www.thregr.org/~wavexx/software/screenkey/'
VERSION = '0.9'

SLOP_URL = 'https://github.com/naelstrof/slop'
ERROR_URL = 'https://www.thregr.org/~wavexx/software/screenkey/#troubleshooting'


# CLI/Interface options
POSITIONS = OrderedDict(zip(
    ('top', 'center', 'bottom', 'fixed'),
    (_('Top'), _('Center'), _('Bottom'), _('Fixed'))
))

TEXT_ALIGNMENTS = OrderedDict(zip(
    ('left', 'center', 'right'),
    (_('Left'), _('Center'), _('Right'))
))

FONT_SIZES = OrderedDict(zip(
    ('small', 'medium', 'large',),
    (_('Small'), _('Medium'), _('Large'),)
))

KEY_MODES = OrderedDict(zip(
    ('composed', 'translated', 'keysyms', 'raw',),
    (_('Composed'), _('Translated'), _('Keysyms'), _('Raw'),)
))

BAK_MODES = OrderedDict(zip(
    ('normal', 'baked', 'full',),
    (_('Normal'), _('Baked'), _('Full'),)
))

MODS_MODES = OrderedDict(zip(
    ('normal', 'emacs', 'mac', 'win', 'tux',),
    (_('Normal'), _('Emacs'), _('Mac'), _('Windows'), _('Linux'),)
))

class Options(dict):
    def __getattr__(self, k):
        return self[k]

    def __setattr__(self, k, v):
        self[k] = v
