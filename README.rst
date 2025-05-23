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


All Ten Metrics used in the paper
--------

    Molecular Complexity
    ├──notebook
    │   └── MC1_MC2_calculation.ipynb
    │   └── Other_8_metrics.ipynb

Metrics in this work
--------

* MC1	Fraction of non-divalent nodes in the molecular graph	
* MC2	Number of non-divalent nodes not considering C=O groups in N-(C=O) and O-(C=O) substructures	
--> A View on Molecular Complexity from the GDB Chemical Space Ye Buehler and Jean-Louis Reymond, J. Chem. Inf. Model., 2025, doi/10.1021/acs.jcim.5c00334

Other complexity metrics
--------

* FCFP4	Number of on-bits in a binary 2048-bit FCFP4 fingerprint	
--> Schuffenhauer, A.; Brown, N.; Selzer, P.; Ertl, P.; Jacoby, E. Relationships between Molecular Complexity, Biological Activity, and Structural Diversity. J. Chem. Inf. Model. 2006, 46 (2), 525–535. https://doi.org/10.1021/ci0503558.

* Data Warrior	Determines all distinct substructures for every bond count up to seven bonds, and the maximum value is used to calculate the fractal complexity using the Minkowski–Bouligand (box-counting) dimension concept
--> Sander, T.; Freyss, J.; von Korff, M.; Rufener, C. DataWarrior: An Open-Source Program For Chemistry Aware Data Visualization And Analysis. J Chem Inf Model 2015, 55 (2), 460–473. https://doi.org/10.1021/ci500588j.
--> von Korff, M.; Sander, T. Molecular Complexity Calculated by Fractal Dimension. Sci. Rep. 2019, 9 (1), 967. https://doi.org/10.1038/s41598-018-37253-8.

* Böttcher	Shannon entropy using additive atom contributions considering valence electrons, atom environment, chirality and molecular symmetry
--> Böttcher, T. An Additive Definition of Molecular Complexity. J. Chem. Inf. Model. 2016, 56 (3), 462–470. https://doi.org/10.1021/acs.jcim.5b00723.

* Proudfoot	Shannon entropy using additive atom contributions considering atomic number, the number of connections and paths up to length 2. 	
--> Proudfoot, J. R. A Path Based Approach to Assessing Molecular Complexity. Bioorg. Med. Chem. Lett. 2017, 27 (9), 2014–2017. https://doi.org/10.1016/j.bmcl.2017.03.008.

* SPS	Sum of heavy atom contributions considering hybridization, stereochemistry, non-aromaticity, and the number of heavy-atom neighbors	
* nSPS	SPS normalized to heavy atom count	
--> Krzyzanowski, A.; Pahl, A.; Grigalunas, M.; Waldmann, H. Spacial Score─A Comprehensive Topological Indicator for Small-Molecule Complexity. J. Med. Chem. 2023, 66 (18), 12739–12750. https://doi.org/10.1021/acs.jmedchem.3c00689.

Synthesizability
--------

* SAscore	Presence of fragments frequently encountered in PubChem molecules combined with a complexity penalty considering ring types, stereochemistry and molecule size
--> Ertl, P.; Schuffenhauer, A. Estimation of Synthetic Accessibility Score of Drug-like Molecules Based on Molecular Complexity and Fragment Contributions. J. Cheminformatics 2009, 1 (1), 8. https://doi.org/10.1186/1758-2946-1-8.

* SCS	Machine-learned score from 12 million reaction in Reaxys predicting the number of steps required for synthesis from common starting material from the ECFP4 fingerprint as input, with maximum value 5	
--> Coley, C. W.; Rogers, L.; Green, W. H.; Jensen, K. F. SCScore: Synthetic Complexity Learned from a Reaction Corpus. J. Chem. Inf. Model. 2018, 58 (2), 252–261. https://doi.org/10.1021/acs.jcim.7b00622.


* Free software: MIT license
* Documentation: https://gdb-molecular-complexity.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
