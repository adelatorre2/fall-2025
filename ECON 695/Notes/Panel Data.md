

# Panel Data — Quick Guide (Econ 695, Lecture 8)

> **Goal.** Understand how panel data helps recover causal effects when unobservables are time‐invariant, and how the *within* (fixed effects) estimator relates to *between* and pooled OLS estimates.

---

## TL;DR

- **Causal model:** $y_{it} = x_{it}'\beta + \alpha_i + \varepsilon_{it}$.
- If the bad stuff is **time-invariant** ($\alpha_i$), **demeaning** (or first-differencing when $T=2$) removes it.
- Three equivalent ways to get fixed effects (FE/**within**) estimates:
  1) **De-mean** by $i$,  
  2) **Add unit dummies** (FE),  
  3) **Control function / CRE**: include the unit mean $ \bar x_i $ as regressors.
- **Interpretation:** Within uses **within-unit variation over time**; Between uses **across-unit averages**.
- **Assumptions to keep straight:**  
  (A1) Time-invariant correlation: $E[(x_{it}-\bar x_i)\alpha_i]=0$.  
  (A2) Strict exogeneity for FE: $E[\varepsilon_{it}\mid x_{i1},\dots,x_{iT},\alpha_i]=0$.  
  (A3) Sufficient **within variation** in the regressor(s).

---

## 1) From causal model to bias (why panels help)

**Start from** $y_i = x_i'\beta + \nu_i$ (cross-section). If $E[x_i\nu_i]\neq 0$, pooled OLS is biased.

With panels, write for unit $i$ and time $t$:
$$
y_{it}=x_{it}'\beta+\underbrace{\alpha_i}_{\text{time-invariant}}+\varepsilon_{it}
$$
- Think **ability**, **baseline productivity**, **location fixed traits** in $\alpha_i$.
- We allow $E[x_{it}\alpha_i]\neq 0$ but assume $E[x_{it}\varepsilon_{it}]=0$.

### Key trick: remove $\alpha_i$

Compute **unit means**:
$$
\bar y_i=\frac1T\sum_t y_{it},\quad \bar x_i=\frac1T\sum_t x_{it},\quad \bar\varepsilon_i=\frac1T\sum_t \varepsilon_{it}
$$
Then subtract:
$$
\underbrace{y_{it}-\bar y_i}_{\widetilde y_{it}}
=\underbrace{(x_{it}-\bar x_i)'}_{\widetilde x_{it}'}\beta+
\underbrace{\varepsilon_{it}-\bar\varepsilon_i}_{\widetilde\varepsilon_{it}}
\tag{W}
$$
**Boom:** $\alpha_i$ drops out. OLS on (W) is the **within** estimator, $\hat\beta_W$.

> **Two-period check (first differences).** If $T=2$, demeaning equals differencing:
> $\; y_{i2}-y_{i1}=(x_{i2}-x_{i1})'\beta+(\varepsilon_{i2}-\varepsilon_{i1})$.

---

## 2) Three equivalent implementations

### (i) Demean-and-OLS
Run OLS with $\widetilde y_{it}$ on $\widetilde x_{it}$.

### (ii) Unit dummies (Fixed Effects regression)
Estimate
$$
y_{it}=x_{it}'\beta+\sum_{g=1}^{N}\theta_g\,\mathbb 1\{i=g\}+\varepsilon'_{it}.
$$
By Frisch–Waugh–Lovell (FWL), the $\beta$ you get equals $\hat\beta_W$.

### (iii) Control function / Correlated Random Effects (CRE)
Estimate
$$
y_{it}=x_{it}'\beta+\bar x_i'\gamma+\varepsilon''_{it}.
$$
FWL algebra (see §6 below) shows $\hat\beta$ here **equals** $\hat\beta_W$ for time-varying regressors.  
> ⚠️ If a regressor is **time-invariant** ($x_{kit}=x_{ki}$), it is collinear with $\bar x_{ki}$ and **drops out**—you can’t estimate its effect with FE.

---

## 3) Within vs Between vs Pooled OLS

- **Pooled OLS** (ignores groups) blends **within** and **between** variation and is biased when $E[x_{it}\alpha_i]\neq0$.
- **Between** regression uses group means: $\bar y_i=\bar x_i'\beta+\alpha_i+\bar\varepsilon_i$.
- There’s a decomposition (analogous to the Law of Total Variance): pooled covariance $=$ within $+$ between. Hence pooled OLS is a **weighted average** of $\hat\beta_W$ and the between estimator.

**When to use what**
- Interested in **how unit changes over time affect outcomes** → **Within/FE**.
- Interested in **cross-unit level differences** (e.g., city traits) → **Between** (but defend $E[\bar x_i \alpha_i]=0$ or model it).

---

## 4) Assumptions you’ll hear in lecture (and what they really mean)

1. **Strict exogeneity (for FE consistency):**  
   $E[\varepsilon_{it}\mid x_{i1},\dots,x_{iT},\alpha_i]=0$ for all $t$.  
   - Violated if current shocks feed back into future $x$ (e.g., $x_{i,t+1}$ reacts to $\varepsilon_{it}$).
1. **No perfect collinearity within $i$:** you need **within variation** in $x_{it}$.
2. **Clustered errors:** $\varepsilon_{it}$ often serially correlated within $i$. Use **cluster-robust** (by unit) SEs.

> **Dynamic panels caveat.** If you include lags of $y$ on the RHS, FE is biased when $T$ is small (Nickell bias). Different tools (IV/Arellano–Bond) are needed.

---

## 5) Worked mini–derivations (as she speeds up)

### 5.1 Bias in pooled OLS with time-invariant $\alpha_i$
Let $x_{it}=(1,z_{it})$. Pooled OLS slope has “bias” term
$$
\frac{\sum_{i,t}(z_{it}-\bar z)\alpha_i}{\sum_{i,t}(z_{it}-\bar z)^2}
=\frac{\sum_i(\bar z_i-\bar z)\alpha_i}{\sum_{i,t}(z_{it}-\bar z)^2}
\quad (\because \sum_t(z_{it}-\bar z_i)=0).`
$$
So the bias is driven solely by **between** correlation $(\bar z_i,\alpha_i)$. FE kills it.

### 5.2 FE = first differences when $T=2$
$$
\widetilde y_{it} = y_{it}-\bar y_i
=\left(y_{i2}-\frac{y_{i1}+y_{i2}}2,\; y_{i1}-\frac{y_{i1}+y_{i2}}2\right)
=\left(\tfrac12(y_{i2}-y_{i1}),\;-\tfrac12(y_{i2}-y_{i1})\right),
$$
and the same for $x$. Dropping one of the two rows gives the **FD** regression.

### 5.3 CRE equals FE for time-varying regressors (one regressor case)
Auxiliary regression: $z_{it}=\pi_1+\pi_2\bar z_i+\xi_{it}$.  
FOCs imply $\hat\pi_1=0,\hat\pi_2=1$ because $\sum_{i,t}(z_{it}-\bar z_i)\bar z_i=0$.  
FWL then yields
$$
\hat\beta_2=\frac{\sum_{i,t}(z_{it}-\bar z_i)y_{it}}{\sum_{i,t}(z_{it}-\bar z_i)^2}=\hat\beta_W.
$$

---

## 6) Example anchor — Twins and the return to education

Model: $y_{fi}=\beta_1+\beta_2 S_{fi}+\alpha_f+\varepsilon_{fi}$ (two twins $i=1,2$ per family $f$).  
- **Pooled OLS:** $\hat\beta\approx 0.08$ (higher—picks up ability).  
- **Within family (FE):** $\hat\beta_W\approx 0.068$ (lower—removes family ability $\alpha_f$).  
- **CRE/control function:** add $\bar S_f$ (mean schooling in the pair); coefficient on own $S_{fi}$ adjusts toward the FE value.

**Takeaway:** FE exploits *within-family* differences in schooling to purge ability bias.

---

## 7) What drops out under FE (and why that’s fine)

- **Time-invariant regressors** (gender, baseline cohort, geography at unit level) are absorbed by the unit FE and **cannot be identified**.  
- Their interactions with **time dummies** *can* be identified (e.g., “post × treated” in DiD).

---

## 8) Practical checklist for problem sets & code

1. Regress $y$ on $x$ with **unit and time fixed effects** when appropriate.
2. **Cluster SEs by unit**; add time clusters if staggered policies/data structure require.
3. Inspect **within variation**: if a regressor barely moves over time, $\hat\beta_W$ will be imprecise.
4. For $T=2$, consider **first differences**; for $T>2$, FE or CRE are equivalent for time-varying regressors.
5. Remember where we’re headed: FE is the building block for **DiD** and **event studies**.

---

### One-liners you can reuse
- “FE removes time-invariant omitted variables $\alpha_i$ by using within-unit variation.”
- “Pooled OLS conflates within and between variation; FE isolates the within piece.”
- “Strict exogeneity rules out feedback from shocks to future regressors.”

---

*Prepared for Obsidian: headings, equations, and callouts are Markdown/LaTeX friendly. Edit freely during lecture.*