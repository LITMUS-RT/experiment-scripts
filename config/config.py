from __future__ import print_function
import itertools
from common import get_executable

'''Paths to binaries.'''
BINS = {'rtspin'    : get_executable('rtspin', 'liblitmus'),
        'release'   : get_executable('release_ts', 'liblitmus'),
        'ftcat'     : get_executable('ftcat', 'feather-trace-tools'),
        'ftsplit'   : get_executable('ft2csv', 'feather-trace-tools'),
        'ftsort'    : get_executable('ftsort', 'feather-trace-tools'),
        'st_trace'  : get_executable('st_trace', 'feather-trace-tools'),
        'trace-cmd' : get_executable('trace-cmd', 'rt-kernelshark'),
		# Optional, as sched_trace is not a publically supported repository
        'st_show'   : get_executable('st_show', 'sched_trace', True)}

'''Names of output files.'''
FILES = {'ft_data'    : 'ft.bin',
         'linux_data' : 'trace.dat',
         'sched_data' : 'st-{}.bin',
         'log_data'   : 'trace.slog',}

'''Default parameter names in params.py.'''
PARAMS = {'sched'  : 'scheduler',
          'dur'    : 'duration',
          'kernel' : 'uname',
          'cycles' : 'cpu-frequency'}

'''Default values for program parameters.'''
DEFAULTS = {'params_file' : 'params.py',
            'sched_file'  : 'sched.py',
            'exps_file'   : 'exps.py',
            'duration'    : 10,
            'spin'		  : 'rtspin',
            'cycles'      : 2000}

'''Default sched_trace events (this is all of them).'''
SCHED_EVENTS = range(501, 513)

'''Overhead events.'''
OVH_BASE_EVENTS  = ['SCHED', 'RELEASE', 'SCHED2', 'TICK', 'CXS']
OVH_ALL_EVENTS   = ["%s_%s" % (e, t) for (e,t) in
                    itertools.product(OVH_BASE_EVENTS, ["START","END"])]
OVH_ALL_EVENTS  += ['RELEASE_LATENCY']
# This event doesn't have a START and END
OVH_BASE_EVENTS += ['RELEASE_LATENCY']