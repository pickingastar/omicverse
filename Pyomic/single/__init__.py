r"""
single (A omic framework for single cell omic analysis)
"""

from ._cosg import cosg
from ._pySCSA import data_preprocess,cell_annotate,cell_anno_print,scanpy_lazy
from ._nocd import scnocd
from ._mofa import mofa,factor_exact,factor_correlation,get_weights
from ._scdrug import autoResolution,writeGEP,Drug_Response
from ._cpdb import cpdb_network_cal,cpdb_plot_network,cpdb_plot_interaction,cpdb_interaction_filtered
from ._scgsea import geneset_aucell,pathway_aucell,pathway_aucell_enrichment,pathway_enrichment,pathway_enrichment_plot