#!/bin/bash
runph --user-defined-extension=pysp.plugins.phhistoryextension --max-iterations=50 --default-rho=2002
python ../plot_history.py ph_history.json 
