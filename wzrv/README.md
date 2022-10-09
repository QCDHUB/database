This repo contains data on unpolarized and polarized lepton production in p + p or p + pb collisions from Tevatron, LHC, and RHIC.

Example process:  p + p --> W<sup>-</sup> --> e<sup>-</sup> + &nu;

# Unpolarized Datasets

## Notes

* These datasets involve spin-averaged PDFs
* Observables: (always differental in eta and integrated over pT) 
  * Asym:  Asymmetry of cross-sections: (W<sup>+</sup> - W<sup>-</sup>)/(W<sup>+</sup> - W<sup>-</sup>)
  * Sig:   Absolute cross-section for W<sup>+</sup> and/or W<sup>-</sup>
  * RW:    Ratio of W<sup>+</sup> to W<sup>-</sup> cross-section
* Datasets with observable "Sig" have normalization uncertainties
* Tables under "Other tables" may not be correct
* The following uncertainties are considered correlated bin-to-bin in eta:
  * Energy tuning
  * Beam energy
  * Recoil modeling
  * Background modeling
  * Unfolding 
  * Generator
  * MC modeling
  * Signal Yield
  * QCD shape
* The following uncertainties are considered uncorrelated bin-to-bin in eta:
  * Electron identification
  * Charge misidentification
  * Positron/electron efficiency
  * QCD +/-
* Only datasets that are fully inclusive (CMS, LHCb, STAR) are currently included
* Tevatron and ATLAS also include cuts on the neutrino transverse momentum
* Asymmetries are used instead of cross sections when the choice is given

## Tables used in current analyses

| index | ref                    | particles | obs      | RS (TeV)  | pT min (GeV) |  experiment
| :--:  | :--:                   | :--       | :--:     | :--:      | :--:         |  :--:      
| 2010  | [link][ref2010]        | p + p     | Asym     | 8.00      | 25           |  CMS       
| 2011  | [link][ref2011]        | p + p     | Asym     | 7.00      | 25           |  CMS       
| 2012  | [link][ref2012]        | p + p     | Asym     | 7.00      | 35           |  CMS       
| 2013  | [link][ref2013-2014]   | p + p     | Asym     | 7.00      | 25           |  CMS       
| 2014  | [link][ref2013-2014]   | p + p     | Asym     | 7.00      | 25           |  CMS       
| 2016  | [link][ref2016]        | p + p     | Asym     | 7.00      | 20           |  LHCb      
| 2017  | [link][ref2017]        | p + p     | Asym     | 8.00      | 20           |  LHCb      
| 2020  | [link][ref2020]        | p + p     | RW       | 0.51      | 25           |  STAR      

## Tables not yet included

| index | ref                    | particles | obs      | RS (TeV)  | pT min (GeV) |  experiment
| :--:  | :--:                   | :--       | :--:     | :--:      | :--:         |  :--:      
| 2021  | [link][ref2021]        | p + p     | Asym     | 13.00     | 26           |  CMS       

## Non-inclusive data tables
| index | ref                    | particles | obs      | RS (TeV)  | pT min (GeV) |  experiment
| :--:  | :--:                   | :--       | :--:     | :--:      | :--:         |  :--:      
| 2000  | [link][ref2000]        | p + pb    | Asym     | 1.96      | 25           |  D0        
| 2003  | [link][ref2003]        | p + pb    | Asym     | 1.96      | 25           |  CDF       
| 2006  | [link][ref2006]        | p + pb    | Asym     | 1.96      | 25           |  D0        
| 2007  | [link][ref2007]        | p + p     | Asym     | 8.00      | 25           |  ATLAS      
| 2008  | [link][ref2008]        | p + p     | Asym     | 7.00      | 25           |  ATLAS     
| 2009  | [link][ref2009]        | p + p     | Asym     | 7.00      | 20           |  ATLAS     

## Cross-section tables

| index    | ref                    | particles | obs       | RS (TeV)  | pT min (GeV) |  experiment
| :--:     | :--:                   | :--       | :--:      | :--:      | :--:         |  :--:      
| 2007sig  | [link][ref2007]        | p + p     | Sig       | 8.00      | 25           |  ATLAS     
| 2008sig  | [link][ref2008]        | p + p     | Sig       | 7.00      | 25           |  ATLAS     
| 2009sig  | [link][ref2009]        | p + p     | Sig       | 7.00      | 20           |  ATLAS     
| 2010sig  | [link][ref2010]        | p + p     | Sig       | 8.00      | 25           |  CMS       
| 2016sig  | [link][ref2016]        | p + p     | Sig       | 7.00      | 20           |  LHCb      
| 2017sig  | [link][ref2017]        | p + p     | Sig       | 8.00      | 20           |  LHCb      
                                                                                                  
# Polarized Datasets                                                       
                                                                           
## Notes                                                                   
                                                                           
* These datasets involve helicity PDFs and spin-averaged PDFs              
* Observables: (always differental in eta and integrated over pT)          
  * SSA: Single-spin asymmetry
  * DSA: Double-spin asymmetry
* Tables outside of ones currently used may not be correct
* Double spin asymmetries have not been implemented in the code

## Tables used in current analyses

| index | ref                    | particles | obs       | RS (TeV)  | pT cut (GeV) | experiment   | 
| :--:  | :--:                   | :--       | :--:      | :--:      | :--:         | :--:         | 
| 1000  | [link][ref1000]        | p + p     | SSA(W)    | 0.51      | 25           | STAR         | 
| 1020  | [link][ref1020]        | p + p     | SSA(W+Z)  | 0.51      | 30           | PHENIX       | 
| 1021  | [link][ref1021]        | p + p     | SSA(W+Z)  | 0.51      | 16           | PHENIX       | 

## Double spin asymmetries

| index | ref                    | particles | obs       | RS (TeV)  | pT cut (GeV) | experiment   | 
| :--:  | :--:                   | :--       | :--:      | :--:      | :--:         | :--:         | 
| 1010  | [link][ref1000]        | p + p     | DSA(W)    | 0.51      | 25           | STAR         | 

[ref1000]:      https://inspirehep.net/record/1708793 
[ref1020]:      https://inspirehep.net/literature/1365091
[ref1021]:      https://inspirehep.net/literature/1667398
[ref2000]:      https://inspirehep.net/record/1333394 
[ref2003]:      https://inspirehep.net/record/674676
[ref2006]:      https://inspirehep.net/literature/1253555
[ref2007]:      https://inspirehep.net/literature/1729240
[ref2008]:      https://inspirehep.net/literature/1502620
[ref2009]:      https://inspirehep.net/literature/928289
[ref2010]:      https://inspirehep.net/literature/1426517
[ref2011]:      https://inspirehep.net/literature/1273570
[ref2012]:      https://inspirehep.net/literature/1118047
[ref2013-2014]: https://inspirehep.net/literature/892975
[ref2016]:      https://inspirehep.net/literature/1311488
[ref2017]:      https://inspirehep.net/literature/1406555
[ref2020]:      https://inspirehep.net/literature/1829350
[ref2021]:      https://inspirehep.net/literature/1810913











