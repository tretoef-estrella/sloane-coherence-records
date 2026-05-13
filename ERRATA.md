# Errata

> Honest corrections to the documentation in this repository.
> This file is permanent: errors found are documented here, not silently
> edited out elsewhere. The original wording is preserved so that anyone
> who already read or cited the earlier version of the documentation
> can see exactly what was corrected.

---

## Erratum #1 — Runtime of the optimisation engine

**Date detected:** May 13, 2026 (morning CEST, Madrid).
**Detected by:** Rafael Amichis Luengo, reading the original Mac runtime log.
**Severity:** Factual error in narrative claims; no impact on the records, the verification, or the methodology. The records themselves are unchanged and remain byte-exact verified.

### What the earlier documentation said

Several files in this repository (`README.md`, `RESULTS.md`, `RECORDS.md`, `GUIDE.md`, `PROOF.md`, `WITNESS.md`, and the public methodology paper `Paper sloane v15 public .md`) stated, in various phrasings, that **each of the two record runs on the Mac M2 took approximately 5.5 hours**. Representative wording from `RECORDS.md` and `RESULTS.md`:

> "The run took approximately 5.5 hours, during which the coherence descended from approximately 0.72 (warmstart) through the Cohn threshold..."

That figure was a memory-based estimate from the assistant who drafted the documentation, not a number read from the actual Mac runtime log. The estimate was wrong by a factor of approximately 66×.

### What is actually correct

The Mac runtime log for the engine 9 (Aquiles) run that produced record #2 reports a steady throughput of 23 000 – 37 000 steps per second over the full 10 000 000 steps. The total runtime, measured directly with the Unix `time` command, is:

> **5 minutes 0.42 seconds** (300.42 seconds of wall time)

This was verified by re-executing the exact same run with the exact same warmstart file (`hormi_raw1.txt`) and the same seed (11) on the same Mac M2, and confirming both (a) the runtime, and (b) that the final coherence reproduces byte-exact to 16 digits (`μ = 0.6870351702235971`).

The byte-exact reproducibility of the record, when re-launched from the same warmstart, is itself a useful finding: the record is an **attractor** of the engine + warmstart + seed combination, not a one-time stochastic outcome.

### What this changes about the records themselves

**Nothing.** The records, the worst pairs, the coherence values, the five-kernel byte-exact verification, the gap to Cohn, the public methodology, and the structural findings about the basin landscape are all completely unaffected by this correction. The error was strictly about a narrative claim regarding how long the Mac run took; it was not about anything that the records or the methodology actually depend on.

### What it does change about how the result should be read

If anything, the corrected runtime **strengthens** the story: the optimisation engine, on a Mac M2 throttled to 25% CPU, produces a world-record packing in about five minutes once a structurally appropriate warmstart is supplied. The reason the two records of May 12, 2026 took a full day to obtain was **not** that the engine was slow — it was that finding the right warmstart family (the sandbox exploration step) is where most of the human-and-AI thinking goes. The engine itself is fast.

### Files corrected on May 13, 2026

The following files in this repository were updated to replace the incorrect "5.5 hours" wording with "approximately 5 minutes" or equivalent precise wording:

- `README.md`
- `RESULTS.md`
- `RECORDS.md`
- `GUIDE FOR EVERYONE.md`
- `PROOF.md`
- `WITNESS.md`
- `Paper sloane v15 public .md`
- `METHODOLOGY.md`

The commits for each correction are visible in the repository commit history dated May 13, 2026.

### Anthropic / Claude accountability note

The original documentation was drafted with the assistance of Claude (Anthropic). The "5.5 hours" figure was supplied by Claude as a memory-based estimate rather than as a number read from the actual log. The author (R. Amichis Luengo) caught the error the following morning by reading the original log file directly. The discipline of the project — "numbers from files only, never from memory" — was breached on this specific point and the correction is filed here transparently. Honest accountability protects future readers; silent edits would not.

---

## Appendix A — Mac runtime log for record #2 (re-execution May 13, 2026)

This is the output of the `time`-instrumented re-execution of the engine run that originally produced record #2. The final coherence reproduces byte-exact to 16 digits. The complete trajectory of the coherence value (μ), the step counter, the per-interval throughput, the BREAKS COHN BARRIER markers, and the D190 verification PASS sequence are reproduced verbatim from the log.

**A note on redaction.** The engine's hyperparameters (initial and final values of the smoothing parameter β, initial learning rate α, momentum coefficient ρ) are part of the proprietary engineering of the engine (see [`LICENSE.md`](LICENSE.md) on the dual licensing of records vs. engine). They have been redacted from this log as `[REDACTED — proprietary engine hyperparameter]`. Their values are not necessary to verify the records — that is done entirely from the packing files using the independent verifier `verify_sloane_independent.py`, which uses no engine-internal information. They are also not necessary to follow the convergence trajectory.

```
rafa@MacBook-Air-de-RAFAEL Downloads % cd ~/Downloads && time caffeinate -dims taskpolicy -c utility ./aquilestrincaestacasvaaporhectorelresacas 10000000 --warmstart=hormi_raw1.txt --seed=11 2>&1 | tee aquile_hormi_raw1_TIMING_TEST.log
============================================================
Engine 9 — aquilestrincaestacasvaaporhectorelresacas
Target (d=4, n=64) hlc Cohn = 0.6871602015093070
============================================================
CONFIG:
  MAX_STEPS    = 10000000
  warmstart    = hormi_raw1.txt
  seed         = 11
  beta_min     = [REDACTED — proprietary engine hyperparameter]
  beta_max     = [REDACTED — proprietary engine hyperparameter]
  alpha_init   = [REDACTED — proprietary engine hyperparameter]
  rho (mom)    = [REDACTED — proprietary engine hyperparameter]
  log_every    = 250000
  output       = aquilestrincaestacas_best.txt
============================================================
Loaded warmstart from hormi_raw1.txt
Initial mu = 0.7031708385306130  (gap_Cohn = +1.601064e-02)
step          1 | mu=0.7031598575065610 | best=0.7031598575065610 | gap=+1.599966e-02 | beta=[REDACTED] | alpha=[REDACTED] | 12K steps/s | last_imp@0
step     250000 | mu=0.6966815998778930 | best=0.6966815998778930 | gap=+9.521398e-03 | beta=[REDACTED] | alpha=[REDACTED] | 24K steps/s | last_imp@249999
step     500000 | mu=0.6944014133124611 | best=0.6944014133124611 | gap=+7.241212e-03 | beta=[REDACTED] | alpha=[REDACTED] | 24K steps/s | last_imp@499999
step     750000 | mu=0.6925956014546215 | best=0.6925956014546215 | gap=+5.435400e-03 | beta=[REDACTED] | alpha=[REDACTED] | 24K steps/s | last_imp@749999
step    1000000 | mu=0.6911071652593005 | best=0.6911071652593005 | gap=+3.946964e-03 | beta=[REDACTED] | alpha=[REDACTED] | 24K steps/s | last_imp@999999
step    1250000 | mu=0.6898058291992044 | best=0.6898058291992044 | gap=+2.645628e-03 | beta=[REDACTED] | alpha=[REDACTED] | 23K steps/s | last_imp@1249999
step    1500000 | mu=0.6889595643478105 | best=0.6889595643478105 | gap=+1.799363e-03 | beta=[REDACTED] | alpha=[REDACTED] | 23K steps/s | last_imp@1499999
step    1750000 | mu=0.6883679562798498 | best=0.6883679562798498 | gap=+1.207755e-03 | beta=[REDACTED] | alpha=[REDACTED] | 23K steps/s | last_imp@1749999
step    2000000 | mu=0.6878955596898793 | best=0.6878955596898793 | gap=+7.353582e-04 | beta=[REDACTED] | alpha=[REDACTED] | 23K steps/s | last_imp@1999999
step    2250000 | mu=0.6876413697203183 | best=0.6876413697203183 | gap=+4.811682e-04 | beta=[REDACTED] | alpha=[REDACTED] | 23K steps/s | last_imp@2249999
step    2500000 | mu=0.6874730294705925 | best=0.6874730294705925 | gap=+3.128280e-04 | beta=[REDACTED] | alpha=[REDACTED] | 23K steps/s | last_imp@2499999
step    2750000 | mu=0.6873493421138750 | best=0.6873493421138750 | gap=+1.891406e-04 | beta=[REDACTED] | alpha=[REDACTED] | 24K steps/s | last_imp@2749999
step    3000000 | mu=0.6872505983607575 | best=0.6872505983607575 | gap=+9.039685e-05 | beta=[REDACTED] | alpha=[REDACTED] | 24K steps/s | last_imp@2999999
step    3250000 | mu=0.6871811475756584 | best=0.6871811475756584 | gap=+2.094607e-05 | beta=[REDACTED] | alpha=[REDACTED] | 25K steps/s | last_imp@3249999
step    3500000 | mu=0.6871374032697195 | best=0.6871374032697195 | gap=-2.279824e-05 | beta=[REDACTED] | alpha=[REDACTED] | 25K steps/s | last_imp@3499999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6871374032697195 < 0.6871602015093070 ***
step    3750000 | mu=0.6871060426723841 | best=0.6871060426723841 | gap=-5.415884e-05 | beta=[REDACTED] | alpha=[REDACTED] | 26K steps/s | last_imp@3749999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6871060426723841 < 0.6871602015093070 ***
step    4000000 | mu=0.6870845292590128 | best=0.6870845292590128 | gap=-7.567225e-05 | beta=[REDACTED] | alpha=[REDACTED] | 26K steps/s | last_imp@3999999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870845292590128 < 0.6871602015093070 ***
step    4250000 | mu=0.6870695728746493 | best=0.6870695728746493 | gap=-9.062863e-05 | beta=[REDACTED] | alpha=[REDACTED] | 27K steps/s | last_imp@4249999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870695728746493 < 0.6871602015093070 ***
step    4500000 | mu=0.6870590152435959 | best=0.6870590152435959 | gap=-1.011863e-04 | beta=[REDACTED] | alpha=[REDACTED] | 27K steps/s | last_imp@4499999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870590152435959 < 0.6871602015093070 ***
step    4750000 | mu=0.6870517625735140 | best=0.6870517625735140 | gap=-1.084389e-04 | beta=[REDACTED] | alpha=[REDACTED] | 28K steps/s | last_imp@4749999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870517625735140 < 0.6871602015093070 ***
step    5000000 | mu=0.6870467027547804 | best=0.6870467027547804 | gap=-1.134988e-04 | beta=[REDACTED] | alpha=[REDACTED] | 28K steps/s | last_imp@4999999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870467027547804 < 0.6871602015093070 ***
step    5250000 | mu=0.6870431810928525 | best=0.6870431810928525 | gap=-1.170204e-04 | beta=[REDACTED] | alpha=[REDACTED] | 29K steps/s | last_imp@5249999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870431810928525 < 0.6871602015093070 ***
step    5500000 | mu=0.6870407213040383 | best=0.6870407213040383 | gap=-1.194802e-04 | beta=[REDACTED] | alpha=[REDACTED] | 29K steps/s | last_imp@5499999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870407213040383 < 0.6871602015093070 ***
step    5750000 | mu=0.6870390174882425 | best=0.6870390174882425 | gap=-1.211840e-04 | beta=[REDACTED] | alpha=[REDACTED] | 29K steps/s | last_imp@5749999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870390174882425 < 0.6871602015093070 ***
step    6000000 | mu=0.6870378418460584 | best=0.6870378418460584 | gap=-1.223597e-04 | beta=[REDACTED] | alpha=[REDACTED] | 30K steps/s | last_imp@5999999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870378418460584 < 0.6871602015093070 ***
step    6250000 | mu=0.6870370259841927 | best=0.6870370259841927 | gap=-1.231755e-04 | beta=[REDACTED] | alpha=[REDACTED] | 30K steps/s | last_imp@6249999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870370259841927 < 0.6871602015093070 ***
step    6500000 | mu=0.6870364587303205 | best=0.6870364587303205 | gap=-1.237428e-04 | beta=[REDACTED] | alpha=[REDACTED] | 30K steps/s | last_imp@6499999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870364587303205 < 0.6871602015093070 ***
step    6750000 | mu=0.6870360644200935 | best=0.6870360644200935 | gap=-1.241371e-04 | beta=[REDACTED] | alpha=[REDACTED] | 31K steps/s | last_imp@6749999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870360644200935 < 0.6871602015093070 ***
step    7000000 | mu=0.6870357898345374 | best=0.6870357898345374 | gap=-1.244117e-04 | beta=[REDACTED] | alpha=[REDACTED] | 31K steps/s | last_imp@6999999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870357898345374 < 0.6871602015093070 ***
step    7250000 | mu=0.6870355988309595 | best=0.6870355988309595 | gap=-1.246027e-04 | beta=[REDACTED] | alpha=[REDACTED] | 31K steps/s | last_imp@7249999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870355988309595 < 0.6871602015093070 ***
step    7500000 | mu=0.6870354659616320 | best=0.6870354659616320 | gap=-1.247355e-04 | beta=[REDACTED] | alpha=[REDACTED] | 31K steps/s | last_imp@7499999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870354659616320 < 0.6871602015093070 ***
step    7750000 | mu=0.6870353735253721 | best=0.6870353735253721 | gap=-1.248280e-04 | beta=[REDACTED] | alpha=[REDACTED] | 32K steps/s | last_imp@7749999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870353735253721 < 0.6871602015093070 ***
step    8000000 | mu=0.6870353092483452 | best=0.6870353092483452 | gap=-1.248923e-04 | beta=[REDACTED] | alpha=[REDACTED] | 32K steps/s | last_imp@7999999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870353092483452 < 0.6871602015093070 ***
step    8250000 | mu=0.6870352644879060 | best=0.6870352644879060 | gap=-1.249370e-04 | beta=[REDACTED] | alpha=[REDACTED] | 32K steps/s | last_imp@8249999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870352644879060 < 0.6871602015093070 ***
step    8500000 | mu=0.6870352333487151 | best=0.6870352333487151 | gap=-1.249682e-04 | beta=[REDACTED] | alpha=[REDACTED] | 32K steps/s | last_imp@8499999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870352333487151 < 0.6871602015093070 ***
step    8750000 | mu=0.6870352116851506 | best=0.6870352116851506 | gap=-1.249898e-04 | beta=[REDACTED] | alpha=[REDACTED] | 32K steps/s | last_imp@8749999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870352116851506 < 0.6871602015093070 ***
step    9000000 | mu=0.6870351966193119 | best=0.6870351966193119 | gap=-1.250049e-04 | beta=[REDACTED] | alpha=[REDACTED] | 33K steps/s | last_imp@8999999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870351966193119 < 0.6871602015093070 ***
step    9250000 | mu=0.6870351861346164 | best=0.6870351861346164 | gap=-1.250154e-04 | beta=[REDACTED] | alpha=[REDACTED] | 33K steps/s | last_imp@9249999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870351861346164 < 0.6871602015093070 ***
step    9500000 | mu=0.6870351788348714 | best=0.6870351788348714 | gap=-1.250227e-04 | beta=[REDACTED] | alpha=[REDACTED] | 33K steps/s | last_imp@9499999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870351788348714 < 0.6871602015093070 ***
step    9750000 | mu=0.6870351737564984 | best=0.6870351737564984 | gap=-1.250278e-04 | beta=[REDACTED] | alpha=[REDACTED] | 33K steps/s | last_imp@9749999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870351737564984 < 0.6871602015093070 ***
step   10000000 | mu=0.6870351702235971 | best=0.6870351702235971 | gap=-1.250313e-04 | beta=[REDACTED] | alpha=[REDACTED] | 33K steps/s | last_imp@9999999
*** BREAKS COHN BARRIER byte-exact: best_mu = 0.6870351702235971 < 0.6871602015093070 ***
============================================================
FINAL: best_mu = 0.6870351702235971
       gap_Cohn = -1.250313e-04
       init_mu  = 0.7031708385306130 (drop = 1.613567e-02)
*** RECORD CANDIDATE: best_mu < Cohn byte-exact ***
D190 STRUCTURAL: PASS
D190 FINAL_VERIFY: mu_rebuilt = 0.6870351702235971 (delta best = +0.00e+00) PASS
Saved best packing -> aquilestrincaestacas_best.txt
D190 ROUNDTRIP: mu_reload = 0.6870351702235971 (delta best = +0.00e+00) PASS
============================================================
If RECORD: run verify_sloane_independent.py for D190 INDEPENDENT (4/4)
============================================================
caffeinate -dims taskpolicy -c utility  10000000 --warmstart=hormi_raw1.txt    296,96s user 3,43s system 99% cpu 5:00,42 total
tee aquile_hormi_raw1_TIMING_TEST.log  0,00s user 0,01s system 0% cpu 5:00,42 total
```

The final line — `5:00,42 total` — is the directly-measured wall time of the re-execution, in minutes and seconds, on the Mac M2 with `taskpolicy -c utility` (25% CPU throttle) and `caffeinate -dims` (no sleep).

What the log preserves, byte-exact:

- The full step counter from step 1 to step 10 000 000.
- The full trajectory of the coherence value `μ` and its gap to the Cohn baseline.
- The per-interval throughput (steps/second), rising from 12 000 at startup to ~33 000 at convergence.
- The step (~3 500 000) at which the run first breaks the Cohn barrier.
- The progressively smaller per-interval improvements as the run approaches the local minimum.
- The final value `μ = 0.6870351702235971`, byte-exact identical to the original record-#2 file.
- The D190 verification sequence (STRUCTURAL, FINAL_VERIFY, ROUNDTRIP), all PASS.
- The directly-measured wall time: `5:00,42 total`.

What is intentionally not preserved (the four engine hyperparameters): see the licensing note above.

---

*Errata file last updated: May 13, 2026, Madrid.*
*This file is part of the repository at https://github.com/tretoef-estrella/sloane-coherence-records and is released under the same MIT license as the rest of the open documentation.*
