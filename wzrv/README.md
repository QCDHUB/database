This repo contains data on unpolarized and polarized lepton production in p + p or p + pb collisions from Tevatron, LHC, and RHIC.

Example process:  p + p --> W<sup>-</sup> --> e<sup>-</sup> + &nu;

# Unpolarized Datasets

## Notes

* These datasets involve spin-averaged PDFs
* Observables: (always differental in eta and integrated over pT) 
  * Asym:  Asymmetry of cross-sections: (W<sup>+</sup> - W<sup>-</sup>)/(W<sup>+</sup> - W<sup>-</sup>)
  * Sig:   Absolute cross-section for W<sup>+</sup> and/or W<sup>-</sup>
  * RW:    Ratio of W<sup>+</sup> to W<sup>-</sup> cross-section
* 2015 is the same as 2008, with systematic errors treated as correlated instead of uncorrelated

## Tables used in current analyses

| index | ref                    | particles | obs      | RS (TeV)  | pT cut (GeV) | experiment   | normalization 
| :--:  | :--:                   | :--       | :--:     | :--:      | :--:         | :--:         | :--:
| 2000  | [link][ref2000]        | p + pb    | Asym     | 1.96      | 25           | D0           | 
| 2003  | [link][ref2003]        | p + pb    | Asym     | 1.96      | 25           | CDF          | 
| 2006  | [link][ref2006]        | p + pb    | Asym     | 1.96      | 25           | D0           | 
| 2007  | [link][ref2007]        | p + p     | Sig      | 8.00      | 25           | ATLAS        | Yes 
| 2008  | [link][ref2008/2015]   | p + p     | Sig      | 7.00      | 25           | ATLAS        | 
| 2009  | [link][ref2009]        | p + p     | Sig      | 7.00      | 20           | ATLAS        | Yes
| 2010  | [link][ref2010]        | p + p     | Sig      | 8.00      | 25           | CMS          | Yes
| 2011  | [link][ref2011]        | p + p     | Asym     | 7.00      | 25           | CMS          | 
| 2012  | [link][ref2012]        | p + p     | Asym     | 7.00      | 35           | CMS          | 
| 2013  | [link][ref2013-2014]   | p + p     | Asym     | 7.00      | 25           | CMS          | 
| 2014  | [link][ref2013-2014]   | p + p     | Asym     | 7.00      | 25           | CMS          | 
| 2018  | [link][ref2016]        | p + p     | Sig      | 7.00      | 20           | LHCb         | Yes 
| 2019  | [link][ref2017]        | p + p     | Sig      | 8.00      | 20           | LHCb         | Yes
| 2020  | [link][ref2020]        | p + p     | RW       | 0.51      | 25           | STAR         |

## Other tables

| index | ref                    | particles | obs       | RS (TeV)  | pT cut (GeV) | experiment   | 
| :--:  | :--:                   | :--       | :--:      | :--:      | :--:         | :--:         | 
| 2015  | [link][ref2008/2015]   | p + p     | Sig       | 7.00      | 25           | ATLAS        | Yes
| 2016  | [link][ref2016]        | p + p     | Asym      | 7.00      | 20           | LHCb         | 
| 2017  | [link][ref2017]        | p + p     | Asym      | 8.00      | 20           | LHCb         |
 
# Polarized Datasets

## Notes

* These datasets involve helicity PDFs and spin-averaged PDFs
* Observables: (always differental in eta and integrated over pT) 
  * SSA: Single-spin asymmetry
  * DSA: Double-spin asymmetry

## Tables used in current analyses

| index | ref                    | particles | obs      | RS (TeV)  | pT cut (GeV) | experiment   | 
| :--:  | :--:                   | :--       | :--:     | :--:      | :--:         | :--:         | 
| 1000  | [link][ref1000-1001]   | p + p     | SSA(W)   | 0.51      | 25           | STAR         | 
| 1001  | [link][ref1000-1001]   | p + p     | SSA(W)   | 0.51      | 25           | STAR         | 

## Other tables

| index | ref                    | particles | obs       | RS (TeV)  | pT cut (GeV) | experiment   | 
| :--:  | :--:                   | :--       | :--:      | :--:      | :--:         | :--:         | 
| 1010  | [link][ref1000-1001]   | p + p     | DSA(W)    | 0.51      | 25           | STAR         | 
| 1011  | [link][ref1000-1001]   | p + p     | DSA(W)    | 0.51      | 25           | STAR         | 
| 1020  | [link][ref1020-1021]   | p + p     | SSA(W+Z)  | 0.51      | 25           | PHENIX       | 
| 1021  | [link][ref1020-1021]   | p + p     | SSA(W+Z)  | 0.51      | 25           | PHENIX       | 
| 1022  | [link][ref1022-1023]   | p + p     | SSA(W+Z)  | 0.51      | 16           | PHENIX       | 
| 1023  | [link][ref1022-1023]   | p + p     | SSA(W+Z)  | 0.51      | 16           | PHENIX       | 




[ref1000-1001]: https://inspirehep.net/record/1708793 
[ref1020-1021]: https://inspirehep.net/literature/1365091
[ref1022-1023]: https://inspirehep.net/literature/1667398
[ref2000]:      https://inspirehep.net/record/1333394 
[ref2003]:      https://inspirehep.net/record/674676
[ref2006]:      https://inspirehep.net/literature/1253555
[ref2007]:      https://inspirehep.net/literature/1729240
[ref2008/2015]: https://inspirehep.net/literature/1502620
[ref2009]:      https://inspirehep.net/literature/928289
[ref2010]:      https://inspirehep.net/literature/1426517
[ref2011]:      https://inspirehep.net/literature/1273570
[ref2012]:      https://inspirehep.net/literature/1118047
[ref2013-2014]: https://inspirehep.net/literature/892975
[ref2016]:      https://inspirehep.net/literature/1311488
[ref2017]:      https://inspirehep.net/literature/1406555
[ref2020]:      https://inspirehep.net/literature/1829350











