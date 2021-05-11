This repo contains pp and pd (per nucleon) Drell-Yan cross section data from the E866 (NuSea) and E906 (SeaQuest) experiments at FNAL.

## Data collections and reviews:
* http://p25ext.lanl.gov/e866/papers/e866dyabs/E866_Drell-Yan_Cross_Sections/E866_Drell-Yan_Cross_Sections.html

## Observables

* M<sup>3</sup> dsig/dM dx<sub>F</sub>

## Columns:

- RS            = root(s) [GeV]
- Rtau          = root(tau) = root(sqrt(s/M<sup>2</sup>))
- x<sub>t</sub> = target x
- x<sub>b</sub> = beam x
- x<sub>F</sub> = x<sub>b</sub> - x<sub>t</sub>
- units         = nb GeV<sup>2</sup> or None 
- stat_u        = uncorrelated statistical uncertainty
- syst_u        = uncorrelated systematic uncertainty
- norm_c        = correlated normalization uncertainty

## Tables used in current analyses

| index | ref              | process | target | obs                                  | experiment    |
| :--:  | :--:             | :--:    | :--:   | :--:                                 | :--:          |
| 10001 | [link][ref10001] | DY      | pp     | M<sup>3</sup> dsig/dM dx<sub>F</sub> | Fermilab E866 |
| 10002 | [link][ref10001] | DY      | pd     | M<sup>3</sup> dsig/dM dx<sub>F</sub> | Fermilab E866 |
| 20001 | [link][ref20001] | DY      | pd/2pp | M<sup>3</sup> dsig/dM dx<sub>F</sub> | Fermilab E866 |
| 20002 | [link][ref20002] | DY      | pd/2pp | M<sup>3</sup> dsig/dM dx<sub>F</sub> | Fermilab E906 |

[ref10001]: https://inspirehep.net/record/554316
[ref20001]: https://inspirehep.net/literature/554316
[ref20002]: https://inspirehep.net/literature/1849683

### Notes
* SeaQuest data (20002) requires sum over acceptance matrix.  Values are stored in SQ_Acceptance.xlsx.





