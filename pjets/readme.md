# Polarized single jet production data <br> from RHIC

## data tables

| index | data                   | normalization | collision | algorithm                 | paper in             | data recorded in | collaboration |
| ----- | -----                  | -----         | -----     | -----                     | -----                | -----            | -----         |
| 20001 | [drupal][link.20001.d] | no            | `pp`      | cone                      | [2006][link.20001.p] | 2003 and 2004    | STAR          |
| 20002 | [drupal][link.20002.d] | yes           | `pp`      | cone                      | [2012][link.20002.p] | 2005             | STAR          |
| 20003 | [drupal][link.20003.d] | yes           | `pp`      | cone                      | [2012][link.20003.p] | 2006             | STAR          |
| 20004 | [drupal][link.20004.d] | yes           | `pp`      | anti-<i>k<sub>T</sub></i> | [2015][link.20004.p] | 2009             | STAR          |
| 20005 | [phenix][link.20005.d] | yes           | `pp`      | cone                      | [2011][link.20005.p] | 2005             | PHENIX        |
| 20006 | [drupal][link.20006.d] | yes           | `pp`      | anti-<i>k<sub>T</sub></i> | [2019][link.20006.p] | 2012             | STAR          |
| 20007 | [drupal][link.20007.d] | yes           | `pp`      | anti-<i>k<sub>T</sub></i> | [2021][link.20007.p] | 2015             | STAR          |
| 20008 | [drupal][link.20008.d] | yes           | `pp`      | anti-<i>k<sub>T</sub></i> | [2021][link.20008.p] | 2013             | STAR          |

<br>

1. dataset 20099 is used for testing the separation of "positive" and "negative" <i>&Delta; g</i> solutions

[link.20001.d]: https://drupal.star.bnl.gov/STAR/files/starpublications/68/data.html
[link.20002.d]: https://drupal.star.bnl.gov/STAR/files/starpublications/188/data.html
[link.20003.d]: https://drupal.star.bnl.gov/STAR/files/starpublications/188/data.html
[link.20004.d]: https://drupal.star.bnl.gov/STAR/files/starpublications/217/data.html
[link.20005.d]: https://www.phenix.bnl.gov/phenix/WWW/info/data/ppg093_data.html
[link.20006.d]: https://drupal.star.bnl.gov/STAR/files/starpublications/310/data.html
[link.20007.d]: https://drupal.star.bnl.gov/STAR/publications/longitudinal-double-spin-asymmetry-inclusive-jet-and-dijet-production-polarized-proton-
[link.20008.d]: https://drupal.star.bnl.gov/STAR/publications

[link.20001.p]: https://doi.org/10.1103/PhysRevLett.97.252001 'DOI'
[link.20002.p]: https://doi.org/10.1103/PhysRevD.86.032006 'DOI'
[link.20003.p]: https://doi.org/10.1103/PhysRevD.86.032006 'DOI'
[link.20004.p]: https://doi.org/10.1103/PhysRevLett.115.092002 'DOI'
[link.20005.p]: https://doi.org/10.1103/PhysRevD.84.012006 'DOI'
[link.20006.p]: https://doi.org/10.1103/PhysRevD.100.052005 'DOI'
[link.20007.p]: https://doi.org/10.1103/PhysRevD.103.L091103 'DOI'
[link.20008.p]: https://arxiv.org/abs/2110.11020 'arXiv'

## observables

- <i>A<sub>LL</sub></i>

## headers

- `idx`: indices
- `col`: collaboration
- `particles-in`: `pp` for proton proton collision and `ppb` for proton anti proton collision
- `RS`: center-of-mass energy in GeV
- `pt-min`: minimum <i>p<sub>T</sub></i> in GeV
- `pt-max`: maximum <i>p<sub>T</sub></i> in GeV
- `pT`: average <i>p<sub>T</sub></i> in GeV
- `tau`: $\frac{2 p_t}{\sqrt{s}}$
- `eta-abs-min`: minimum |<i>&eta;</i>|
- `eta-abs-max`: maximum |<i>&eta;</i>|
- `eta-min`: minimum <i>&eta;</i>
- `eta-max`: maximum <i>&eta;</i>
- `cone-radius`: radius used in Jet algorithm
- `obs`: observable[^1]
- `units`: `pb` for pico-barn and `nb` for nano-barn[^2]
- `value`: experimental values of observable

[^1]: `<` and `>` can only be used as a pair to represent averaging

[^2]: Values of `units` have to be the same for the whole dataset, because the numeric unit conversion factor is only based on the first entry.


## uncertainties and corrections

When any type of uncertainty has a positive and negative values that are different in magnitude, only the one with larger magnitude will be used[^3].

- `_c` means "correlated" and and `_u` means "uncorrelated"
- `%` means the uncertainty, normalization or any other type of correction is a percentage
- `norm` is reserved for normalization
- `parton-to-hadron` is the correction from parton level calculation to hadron level, it is 1 plus a relative correction

[^3]: This is to make sure that we do not underestimate uncertainties.

## STAR 2019 paper on 2012 data
According to the paper, part of the systematic uncertainties in STAR 2012 data (2019 paper) are uncorrelated.
