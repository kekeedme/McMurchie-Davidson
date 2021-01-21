import numpy as np
from mmd.molecule import Molecule
from mmd.postscf import PostSCF

def test_cisd():

    water = """
    0 1
    O    0.000000      -0.075791844    0.000000
    H    0.866811829    0.601435779    0.000000
    H   -0.866811829    0.601435779    0.000000
    """
    
    # init molecule and build integrals
    mol = Molecule(geometry=water,basis='sto-3g')
    
    # do the SCF
    mol.RHF()

    # now do FCI
    PostSCF(mol).CISD() 
    
    # G16 reference SCF energy
    assert np.allclose(-74.9420799245,mol.energy.real)
    
    # G16 reference CISD energy
    assert np.allclose(-75.011223006,mol.ecisd.real)
