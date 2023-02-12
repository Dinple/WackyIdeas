from ast import Assert
import os, io
import re
import math
from typing import Text, Tuple, overload
from absl import logging
from collections import namedtuple
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import traceback, sys
import random
import textwrap
import numpy as np
# from circuit_training.grouping import meta_netlist_data_structure as mnds
# from circuit_training.grouping import meta_netlist_convertor
# from circuit_training.grouping import meta_netlist_util
# Compile: cd Plc_client_v2 && python3 setup.py build_ext --inplace && cd ..
# Cython
from cython cimport view
from libcpp cimport bool
from libcpp.vector cimport vector
from libc.string cimport memset
cimport numpy as cnp
cnp.import_array()   # needed to initialize numpy-API


cdef class PlacementCost:
    # str as general purpose PyObject *
    cdef:
        public str netlist_file
        public float macro_macro_x_spacing
        public float macro_macro_y_spacing

    # meta information
    cdef:
        public meta_netlist
        str init_plc
        str project_name
        str block_name
        float width
        float height
        int grid_col
        int grid_row
        float hroutes_per_micron
        float vroutes_per_micron
        float smooth_range
        float overlap_thres
        float hrouting_alloc
        float vrouting_alloc
        float macro_horizontal_routing_allocation
        float macro_vertical_routing_allocation
        bool canvas_boundary_check
        float grid_width
        float grid_height
        dict node_fix
        dict node_placed

    # store module/component count
    cdef:
        int port_cnt
        int hard_macro_cnt
        int hard_macro_pin_cnt
        int soft_macro_cnt
        int soft_macro_pin_cnt
        int module_cnt

    # indices storage
    cdef:
        vector[int] port_indices
        vector[int] hard_macro_indices
        vector[int] hard_macro_pin_indices
        vector[int] soft_macro_indices
        vector[int] soft_macro_pin_indices
        vector[int] macro_indices

    # modules look-up table
    cdef:
        dict mod_name_to_indices
        dict macro_id_to_indices
        dict port_id_to_indices
        object modules_w_pins
        dict hard_macros_to_inpins
        dict soft_macros_to_inpins

    # store nets information
    cdef:
        int net_cnt
        dict nets

    # update flags
    cdef:
        bool FLAG_UPDATE_WIRELENGTH
        bool FLAG_UPDATE_DENSITY
        bool FLAG_UPDATE_CONGESTION
        bool FLAG_UPDATE_MACRO_ADJ
        bool FLAG_UPDATE_MACRO_AND_CLUSTERED_PORT_ADJ
        bool FLAG_UPDATE_NODE_MASK

    # density
    cdef:
        object grid_cells
        object grid_occupied

    # congestion
    cdef:
        object V_routing_cong
        object H_routing_cong
        object V_macro_routing_cong
        object H_macro_routing_cong
        float grid_v_routes
        float grid_h_routes
    
    # fd placer
    cdef:
        dict soft_macro_disp

    # miscellaneous
    cdef:
        list blockages
        list placed_macro
        bool use_incremental_cost
        object node_mask