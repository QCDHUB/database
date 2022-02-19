# Unpolarized single hadron production data in <i>pp</i> collisions

## data tables

| index | data                     | normalization | collision | paper in             | data recorded in | collaboration |
| ----- | -----                    | -----         | -----     | -----                | -----            | -----         |
| 20001 | [HEP Data][link.10001.d] | no            | `pp`      | [2020][link.10001.p] | 2015             | ALICE         |
| 20002 | [HEP Data][link.10002.d] | yes           | `pp`      | [2021][link.10002.p] | 2015             | ALICE         |

<br/>

1. file `sigma_inelastic.npy` stores the [nucleon-nucleon inelastic cross section][link.sigma_inelastic] <i>&sigma;<sub>NN</sub></i>[^1]
2. dataset starting number
    - <b>1</b>: <i>&pi;</i> <sup>&pm;</sup> production
    - <b>2</b>: <i>K</i> <sup>&pm;</sup> production

[^1]: See table II for more details.

[link.10001.d]: https://www.hepdata.net/record/ins1759506
[link.10002.d]: https://www.hepdata.net/record/ins1797443

[link.10001.p]: https://link.aps.org/doi/10.1103/PhysRevC.101.044907 'DOI'
[link.10002.p]: https://link.springer.com/10.1140/epjc/s10052-020-08690-5 'DOI'

[link.sigma_inelastic]: https://link.aps.org/doi/10.1103/PhysRevC.97.054910 'DOI'

## observables

- d<sup>2</sup><i>N</i> / (<i>N</i> <sub>inel</sub> d<i>p<sub>T</sub></i> d<i>y</i>)

## headers

- `col`: collaboration
- `particles-in`: `pp` for proton proton collision and `ppb` for proton anti proton collision
- `particle-out`: detected hadron, `pi+-` for <i>&pi;</i> <sup>&pm;</sup> and `K+-` for <i>K</i> <sup>&pm;</sup>
- `RS`: center-of-mass energy in GeV
- `pt-min`: minimum <i>p<sub>T</sub></i> in GeV
- `pt-max`: maximum <i>p<sub>T</sub></i> in GeV
- `pT`: average <i>p<sub>T</sub></i> in GeV
- `eta-abs-min`: minimum |<i>&eta;</i>|
- `eta-abs-max`: maximum |<i>&eta;</i>|
- `eta-min`: minimum <i>&eta;</i>
- `eta-max`: maximum <i>&eta;</i>
- `obs`: observable
    - `count/inel` for d<sup>2</sup><i>N</i> / (<i>N</i> <sub>inel</sub> d<i>p<sub>T</sub></i> d<i>y</i>)
- `unit`: unit of <b>theoretical calculation</b>, `pb` for pico-barn, `nb` for nano-barn and `mb` for milli-barn[^2]
- `value`: experimental values of the observable

[^2]: Values of `units` have to be the same for the whole dataset, because the numeric unit conversion factor is only based on the first entry.

## uncertainties and corrections

When any type of uncertainty has a positive and negative values that are different in magnitude, only the one with larger magnitude will be used[^3].

- `_c` means "correlated" and and `_u` means "uncorrelated"
- `%` means the uncertainty, normalization or any other type of correction is a percentage
- `norm` is reserved for normalization

[^3]: This is to make sure that we do not underestimate uncertainties.
