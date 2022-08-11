# Unpolarized single hadron production data in <i>pp</i> collisions

## data tables

| index       | data                     | CME (TeV) | normalization | collision | paper in             | data recorded in | collaboration |
| -----       | -----                    | -----     | -----         | -----     | -----                | -----            | -----         |
| 10001/20001 | [HEP Data][link.10001.d] | 2.76      | no            | <i>pp</i> | [2014][link.10001.p] | 2010 and 2011    | ALICE         |
| 10002/20002 | [HEP Data][link.10002.d] | 7         | no            | <i>pp</i> | [2019][link.10002.p] | 2010             | ALICE         |
| 10003/20003 | [HEP Data][link.10003.d] | 5.02      | no            | <i>pp</i> | [2020][link.10003.p] | 2015             | ALICE         |
| 10004/20004 | [HEP Data][link.10004.d] | 13        | no            | <i>pp</i> | [2020][link.10004.p] | 2016             | ALICE         |
| 10005/20005 | [HEP Data][link.10005.d] | 7         | yes           | <i>pp</i> | [2021][link.10005.p] | 2015             | ALICE         |
| 10006/20006 | [HEP Data][link.10005.d] | 13        | yes           | <i>pp</i> | [2021][link.10005.p] | 2015             | ALICE         |

<br/>

1. datasets start with:
    - <b>1</b> for &pi;<sup>&pm;</sup> production
    - <b>2</b> for <i>K</i><sup>&pm;</sup> production
2. datasets 10005 and 10006 (20005 and 20006 as well) are taken from the same paper
3. the observables in 10005 and 20005 are the ratio of the cross sections at 13 TeV to those at 7 TeV

[link.10001.d]: https://www.hepdata.net/record/ins1276299 'HEPData'
[link.10002.d]: https://www.hepdata.net/record/ins1684320 'HEPData'
[link.10003.d]: https://www.hepdata.net/record/ins1759506 'HEPData'
[link.10004.d]: https://www.hepdata.net/record/ins1784041 'HEPData'
[link.10005.d]: https://www.hepdata.net/record/ins1797443 'HEPData'

[link.10001.p]: https://doi.org/10.1016/j.physletb.2014.07.011 'DOI'
[link.10002.p]: https://doi.org/10.1103/PhysRevC.99.024906 'DOI'
[link.10003.p]: https://doi.org/10.1103/PhysRevC.101.044907 'DOI'
[link.10004.p]: https://doi.org/10.1140/epjc/s10052-020-8125-1 'DOI'
[link.10005.p]: https://doi.org/10.1140/epjc/s10052-020-08690-5 'DOI'

## observables

- d<sup>2</sup><i>N</i> / (<i>N</i> <sub>inel</sub> d<i>p<sub>T</sub></i> d<i>y</i>)
- d<sup>2</sup><i>N</i> / (2 &pi; <i>p<sub>T</sub></i> <i>N</i> <sub>inel</sub> d<i>p<sub>T</sub></i> d<i>y</i>)
- d<sup>2</sup><i>N</i> / (<i>N</i> <sub>vis</sub> d<i>p<sub>T</sub></i> d<i>y</i>)

where "inel" means inelastic cross section[^1] and "vis" means visible cross section[^2].

[^1]: See table II in the [reference][link.sigma_inelastic] for the values.
[^2]: See section 2 in the [reference][link.sigma_visible] for the values at 13 TeV.

[link.sigma_inelastic]: https://doi.org/10.1103/PhysRevC.97.054910 'DOI'
[link.sigma_visible]: https://cds.cern.ch/record/2160174

## headers

- `col`: collaboration
- `particles-in`: `pp` for proton proton collision and `ppb` for proton anti-proton collision
- `particle-out`: detected hadron, `pion_+-` for &pi;<sup>&pm;</sup> and `kaon_+-` for <i>K</i><sup>&pm;</sup>
- `RS`: center-of-mass energy in GeV
- `pt-min`: minimum <i>p<sub>T</sub></i> in GeV
- `pt-max`: maximum <i>p<sub>T</sub></i> in GeV
- `pT`: average <i>p<sub>T</sub></i> in GeV
- `eta-abs-min`: minimum |<i>&eta;</i>|
- `eta-abs-max`: maximum |<i>&eta;</i>|
- `eta-min`: minimum <i>&eta;</i>
- `eta-max`: maximum <i>&eta;</i>
- `obs`: observable
    - `dN/N_inel-dy-dpT` for d<sup>2</sup><i>N</i> / (<i>N</i> <sub>inel</sub> d<i>p<sub>T</sub></i> d<i>y</i>)
    - `dN/2-pi-pT-N_inel-dy-dpT` for d<sup>2</sup><i>N</i> / (2 &pi; <i>p<sub>T</sub></i> <i>N</i> <sub>inel</sub> d<i>p<sub>T</sub></i> d<i>y</i>)
    - `dN/N_vis-dy-dpT` for d<sup>2</sup><i>N</i> / (<i>N</i> <sub>vis</sub> d<i>p<sub>T</sub></i> d<i>y</i>)
- `unit`: unit of <b>theoretical calculation</b>[^3], `pb` for pico-barn, `nb` for nano-barn and `mb` for milli-barn[^4]
- `value`: experimental values of the observable

[^3]: <b>NOT</b> for experimental data! Actually these experiments usually provide events counts, which does not have a unit of "barn".
[^4]: Values of `units` have to be the same for the whole dataset, because the numeric unit conversion factor is only based on the first entry.

## uncertainties and corrections

When any type of uncertainty has a positive and negative values that are different in magnitude, only the one with larger magnitude will be used[^5].

- `_c` means "correlated" and and `_u` means "uncorrelated"
- `%` means the uncertainty, normalization or any other type of correction is a percentage
- `norm` is reserved for normalization

[^5]: Make sure that we do not underestimate uncertainties.
