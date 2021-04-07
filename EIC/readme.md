EIC kinematic templates.  Data Index:

- 1000: X, Q2, RS values for EIC on A_PV (electron, hadron), A_parallel (Apa), and A_perp (Ape) (proton) (lum=100 fb-1)
- 1001: X, Q2, RS values for EIC on A_PV (electron, hadron), A_parallel (Apa), and A_perp (Ape) (deuteron/helium) (lum=10 fb-1)
- 2000: X, Q2, RS, and uncertanty values for EIC on NC e-p lum=10 fb-1 reduced cross-section (optimistic)
- 2001: X, Q2, RS, and uncertanty values for EIC on NC e-p lum=10 fb-1 reduced cross-section (pessimistic)
- 2010: X, Q2, RS, and uncertanty values for EIC on CC e-p lum=10 fb-1 reduced cross-section (optimistic)
- 2011: X, Q2, RS, and uncertanty values for EIC on CC e-p lum=10 fb-1 reduced cross-section (pessimistic)
- 2100: X, Q2, RS, and uncertanty values for EIC on NC e-p lum=100fb-1reduced cross-section (optimistic)
- 2101: X, Q2, RS, and uncertanty values for EIC on NC e-p lum=100fb-1reduced cross-section (pessimistic)
- 2110: X, Q2, RS, and uncertanty values for EIC on CC e-p lum=100fb-1reduced cross-section (optimistic)
- 2111: X, Q2, RS, and uncertanty values for EIC on CC e-p lum=100fb-1reduced cross-section (pessimistic)

<br>

| index |  process | target   | obs      | experiment     | uncertainty       | parameterization  | comment           |
| :--:  |  :--:    | :--:     | :--:     | :--:           | :--:              | :--:              | :--:              |
| 81001 |  pdis    | proton   | A_ll     | JAM4EIC        | pessimistic       | valence           | high case |
| 81002 |  pdis    | proton   | A_ll     | JAM4EIC        | pessimistic       | valence           | mid case  |
| 81003 |  pdis    | proton   | A_ll     | JAM4EIC        | pessimistic       | valence           | low case  |
| 82001 |  pdis    | deoteron | A_ll     | JAM4EIC        | pessimistic       | valence           | high case |
| 82002 |  pdis    | deoteron | A_ll     | JAM4EIC        | pessimistic       | valence           | mid case  |
| 82003 |  pdis    | deoteron | A_ll     | JAM4EIC        | pessimistic       | valence           | low case  |
| 83001 |  pdis    | helium   | A_ll     | JAM4EIC        | pessimistic       | valence           | high case |
| 83002 |  pdis    | helium   | A_ll     | JAM4EIC        | pessimistic       | valence           | mid case  |
| 83003 |  pdis    | helium   | A_ll     | JAM4EIC        | pessimistic       | valence           | low case  |
| 90001 |  dis     | proton   | A_PV_e   | JAM4EIC        | optimistic        | ---               | 100 fb-1
| 90101 |  dis     | proton   | A_PV_e   | JAM4EIC        | moderate          | ---               | 100 fb-1
| 90002 |  dis     | deuteron | A_PV_e   | JAM4EIC        | optimistic        | ---               | 10  fb-1
| 90102 |  dis     | proton   | A_PV_e   | JAM4EIC        | moderate          | ---               | 100 fb-1
| 90003 |  dis     | deuteron | A_PV_e   | JAM4EIC        | optimistic        | ---               | 100 fb-1

<br>

For pseudo data of A_ll from proton, deuteron and helium beams

- All the pseudo data are in https://github.com/QCDHUB/analysis-all
- The "low case" means A_LL is one sigma smaller than its mean only in the unmeasured region.
- The "mid case" means A_LL is its central value
- The "high case" means A_LL is one sigma larger than its mean only in the unmeasured region.
- By unmeasured region we mean x Bjorken less than about 0.01.
- Spin dependent gluons that are negative, and spin dependent valence down quarks that are positive, are removed from baseline.
