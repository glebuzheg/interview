import os

if os.environ.get('DYNO_RAM'):
    from .settings_production import *
else:
    from .settings_local import *