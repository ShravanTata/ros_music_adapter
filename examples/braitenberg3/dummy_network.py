#!/usr/bin/python

import nest
import numpy as np

from nest import raster_plot as rplt
import matplotlib.pylab as plt
import seaborn as sbn

sbn.set_palette("deep", desat=.6)
sbn.set_context(rc={"figure.figsize": (8, 4)})

nest.ResetKernel()
nest.set_verbosity("M_FATAL")
#nest.SetKernelStatus({'resolution': 0.1})
#nest.SetKernelStatus({'print_time': True})


NUM_ENC_NEURONS = 2 
run_time = 1000000. 

proxy_in = nest.Create('music_event_in_proxy', NUM_ENC_NEURONS)
nest.SetStatus(proxy_in, [{'port_name': 'in', 'music_channel': c} for c in range(NUM_ENC_NEURONS)])
nest.SetAcceptableLatency('in', .1)

proxy_out = nest.Create('music_event_out_proxy')
nest.SetStatus(proxy_out, {'port_name': 'out'})

parrot = nest.Create("parrot_neuron", NUM_ENC_NEURONS)

nest.Connect(proxy_in, parrot, 'one_to_one')
for i in range(NUM_ENC_NEURONS):
    nest.Connect([parrot[i]], proxy_out, 'all_to_all', {'music_channel': i})


nest.Simulate(run_time)




