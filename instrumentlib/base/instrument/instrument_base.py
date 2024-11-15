'''___         _                          _   _    _ _
  |_ _|_ _  __| |_ _ _ _  _ _ __  ___ _ _| |_| |  (_) |__   InstrumentLib
   | || ' \(_-<  _| '_| || | '  \/ -_) ' \  _| |__| | '_ \  instrument_base.by
  |___|_||_/__/\__|_|  \_,_|_|_|_\___|_||_\__|____|_|_.__/  (C) 2024  Marc Van Riet et al.

  Licensed under the Apache License, Version 2.0. See http://www.apache.org/licenses/LICENSE-2.0
'''

import logging

class InstrumentBase():
    
    def __init__(self, name, **kwargs):
        
        self._name = name
        self._config = kwargs                       # TODO: make configparser object
        
        self.log = logging.getLogger("inst.%s" % name)

    @property
    def config(self):
        ''' Returns the section of a ConfigParser with settings for this instrument.
        '''
        return self._config
    
