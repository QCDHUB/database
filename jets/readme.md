# unpolarized Jet data from Tevatron and RHIC

## data tables

| index | ref                      | normalization | collision | paper in                 | data recorded in         | collaboration |
| ----- | -----                    | -----         | -----     | -----                    | -----                    | -----         |
| 10001 | [HEP Data][link.10001.d] | yes           | `ppb`     | [2008][link.10001.p]     | run II from 2004 to 2005 | D0            |
| 10002 | [HEP Data][link.10002.d] | yes           | `ppb`     | [2007][link.10002.p]     | run II from 2002 to 2006 | CDF           |
| 10003 | [drupal][link.10003.d]   | yes           | `pp`      | [2006][link.10003.p]     | 2003 and 2004            | STAR MB       |
| 10004 | [drupal][link.10004.d]   | yes           | `pp`      | [2006][link.10004.p]     | 2003 and 2004            | STAR HT       |

<br/>

1. according to email exchanges with Bria Page (April 12, 2021), datasets 10003 and 10004 have normalization unceratinties of 8%

2. dataset [10092][link.10092.d] is the cone algorithm version of dataset 10002

3. dataset 19999 is a test dataset

[link.10001.d]: https://www.hepdata.net/record/ins779574
[link.10002.d]: https://www.hepdata.net/record/ins743342
[link.10003.d]: https://drupal.star.bnl.gov/STAR/files/starpublications/68/data.html
[link.10004.d]: https://drupal.star.bnl.gov/STAR/files/starpublications/68/data.html
[link.10092.d]: https://www.hepdata.net/record/ins790693

[link.10001.p]: http://dx.doi.org/10.1103/PhysRevLett.101.062001 'DOI'
[link.10002.p]: http://dx.doi.org/10.1103/PhysRevD.75.092006 'DOI'
[link.10003.p]: http://dx.doi.org/10.1103/PhysRevLett.97.252001 'DOI'
[link.10004.p]: http://dx.doi.org/10.1103/PhysRevLett.97.252001 'DOI'

## observables

- <math><mfrac><mi>d<sup>2</sup>&sigma;</mi><mi>d p<sub>T</sub> d y</mi></mfrac></i></math>
- <math><mfrac><mi>d<sup>2</sup>&sigma;</mi><mi>2 &pi; d p<sub>T</sub> d y</mi></mfrac></i></math>

## headers

- `idx`: indices
- `col`: collaboration
- `particles-in`: `pp` for proton proton collision and `ppb` for proton anti proton collision
- `RS`: $\sqrt{s}$ in GeV
- `pt-min`: minimum <i>p<sub>T</sub></i> in GeV
- `pt-max`: maximum <i>p<sub>T</sub></i> in GeV
- `pT`: average <i>p<sub>T</sub></i> in GeV
- `tau`: $\frac{2 p_t}{\sqrt{s}}$
- `eta-abs-min`: minimum |<i>&eta;</i>|
- `eta-abs-max`: maximum |<i>&eta;</i>|
- `eta-min`: minimum <i>&eta;</i>
- `eta-max`: maximum <i>&eta;</i>
- `cone-radius`: radius used in Jet algorithm
- `obs`: observable[observable]
- `units`: `pb` for pico barn and `nb` for nano barn[unit]
- `value`: experimental values of observable
- `plot-factor`: multiplier for separating <i>&eta;</i> bins in plots

[observable]: `<` and `>` can only be used in pairs to represent averaging.
[unit]: Values of `units` have to be the same for the whole dataset, because the numeric unit conversion factor is read in only based on the first entry.

## uncertainties and corrections

When either the systematic or statistical uncertainties have a positive and negative and are different in magnitude, only the one with a larger magnitude is written in the data file.

- `_c` means correlated and and `_u` means uncorrelated

- `%` means the uncertainty or normalization or other types of corrections is a percentage

- `norm` is reserved for normalization

- `parton-to-hadron` is the correction from parton level calculation to hadron level, it is 1 plus the relative correction

## CDF
- We have examined carefully CJ15, the correlated systematic uncertainties are added in quadrature.
    - `./fitpack/theory/altpfit15.f`
        1. subroutine `fildat` instance in line 1857
        2. special treatment for CDF data in line 1947
    - `./fitpack/util/minim15.f`
        1. subroutine `DATSCN` in line 250
        2. special treatment for CDF data in line 312
- CJ15 has a covariance matrix for CDF run I data.
- [Joseph Owens](mailto:owens@hep.fsu.edu) claimed that using the covariance matrix or adding everything in quadrature give same low <i>&chi;<sup>2</sup></i>.
- [Joseph Owens](mailto:owens@hep.fsu.edu) confirmed that for CDF run II data, CJ used the errors added in quadrature and the covariance matrix is for CDF run I data.
