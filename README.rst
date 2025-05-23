========================
A View on Molecular Complexity from the GDB Chemical Space 
========================


.. image:: https://img.shields.io/pypi/v/gdb_molecular_complexity.svg
        :target: https://pypi.python.org/pypi/gdb_molecular_complexity

.. image:: https://readthedocs.org/projects/gdb-molecular-complexity/badge/?version=latest
        :target: https://gdb-molecular-complexity.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

Thank you for your interest in this repository, which complements the publication 
"`A View on Molecular Complexity from the GDB Chemical Space <https://pubs.acs.org/doi/10.1021/acs.jcim.5c00334>`_".

.. image:: https://github.com/Ye-Buehler/Molecular_Complexity/blob/main/docs/mc.jpg
   :alt: GA
   :align: center
   :width: 400px

* MC1 = 1 – FDV; FDV = fraction of divalent nodes in the molecular graph
* MC2 = NDV, with NDV = number of non-divalent nodes, not counting those in (C=O) belonging to (C=O)X groups, X = N, O


Codes for All Ten Metrics Used in the Paper (Located in `Molecular_Complexity/notebook/`)
========================================================================================

.. code-block:: text

    Molecular Complexity/
    └── notebook/
        ├── MC1_MC2_calculation.ipynb
        └── Other_8_metrics.ipynb

Description and References
==========================

(1) Metrics in this work:
--------

- **MC1**: Fraction of non-divalent nodes in the molecular graph [Buehler2025]_  
- **MC2**: Number of non-divalent nodes excluding C=O groups in N-(C=O) and O-(C=O) substructures [Buehler2025]_

.. [Buehler2025] Buehler, Y.; Reymond, J.-L. *A View on Molecular Complexity from the GDB Chemical Space*. 
   J. Chem. Inf. Model. **2025**. https://doi.org/10.1021/acs.jcim.5c00334

(2) Other complexity metrics:
--------

- **FCFP4**: Number of on-bits in a binary 2048-bit FCFP4 fingerprint [Schuffenhauer2006]_.

- **DataWarrior**: Determines all distinct substructures for every bond count up to seven bonds. The maximum value is used to calculate the fractal complexity using the Minkowski–Bouligand (box-counting) dimension concept [Sander2015]_ [Korff2019]_.

- **Böttcher**: Shannon entropy using additive atom contributions considering valence electrons, atom environment, chirality, and molecular symmetry [Boettcher2016]_.

- **Proudfoot**: Shannon entropy using additive atom contributions considering atomic number, the number of connections, and paths up to length 2 [Proudfoot2017]_.

- **SPS**: Sum of heavy atom contributions considering hybridization, stereochemistry, non-aromaticity, and the number of heavy-atom neighbors [Krzyzanowski2023]_.

- **nSPS**: SPS normalized to heavy atom count [Krzyzanowski2023]_.


.. [Schuffenhauer2006]
   Schuffenhauer, A.; Brown, N.; Selzer, P.; Ertl, P.; Jacoby, E.
   *Relationships between Molecular Complexity, Biological Activity, and Structural Diversity*.
   J. Chem. Inf. Model. **2006**, *46*(2), 525–535.
   https://doi.org/10.1021/ci0503558

.. [Sander2015]
   Sander, T.; Freyss, J.; von Korff, M.; Rufener, C.
   *DataWarrior: An Open-Source Program for Chemistry Aware Data Visualization and Analysis*.
   J. Chem. Inf. Model. **2015**, *55*(2), 460–473.
   https://doi.org/10.1021/ci500588j

.. [Korff2019]
   von Korff, M.; Sander, T.
   *Molecular Complexity Calculated by Fractal Dimension*.
   Sci. Rep. **2019**, *9*(1), 967.
   https://doi.org/10.1038/s41598-018-37253-8

.. [Boettcher2016]
   Böttcher, T.
   *An Additive Definition of Molecular Complexity*.
   J. Chem. Inf. Model. **2016**, *56*(3), 462–470.
   https://doi.org/10.1021/acs.jcim.5b00723

.. [Proudfoot2017]
   Proudfoot, J. R.
   *A Path Based Approach to Assessing Molecular Complexity*.
   Bioorg. Med. Chem. Lett. **2017**, *27*(9), 2014–2017.
   https://doi.org/10.1016/j.bmcl.2017.03.008

.. [Krzyzanowski2023]
   Krzyzanowski, A.; Pahl, A.; Grigalunas, M.; Waldmann, H.
   *Spacial Score—A Comprehensive Topological Indicator for Small-Molecule Complexity*.
   J. Med. Chem. **2023**, *66*(18), 12739–12750.
   https://doi.org/10.1021/acs.jmedchem.3c00689


(3) Synthesizability:
--------

- **SAscore**: Presence of fragments frequently encountered in PubChem molecules combined with a complexity penalty considering ring types, stereochemistry, and molecule size [Ertl2009]_.

- **SCS**: Machine-learned score derived from 12 million reactions in Reaxys, predicting the number of synthesis steps from common starting materials using an ECFP4 fingerprint. Maximum score is 5 [Coley2018]_.

.. [Ertl2009] Ertl, P.; Schuffenhauer, A. *Estimation of Synthetic Accessibility Score of Drug-like Molecules Based on Molecular Complexity and Fragment Contributions*. J. Cheminformatics **2009**, *1*(1), 8. https://doi.org/10.1186/1758-2946-1-8

.. [Coley2018] Coley, C. W.; Rogers, L.; Green, W. H.; Jensen, K. F. *SCScore: Synthetic Complexity Learned from a Reaction Corpus*. J. Chem. Inf. Model. **2018**, *58*(2), 252–261. https://doi.org/10.1021/acs.jcim.7b00622


License
--------

* Free software: MIT license


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
