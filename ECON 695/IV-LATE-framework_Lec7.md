
### 🎯 Core Learning Objectives for Lecture 7 (Local Average Treatment Effects)
These are the *key results, assumptions, and derivations* that your professor expects you to understand cold.

---

#### **1️⃣ The setup: when and why we use IV–LATE**

We’re in a world with **imperfect compliance** or **endogeneity**, where the treatment $D_i$ is *not* random, but there’s an instrument $Z_i$ that is.  
Formally, the model is:

$$
Y_i = \alpha_0 + \alpha_1 D_i + u_i
$$
$$
D_i = \pi_0 + \pi_1 Z_i + \varepsilon_i
$$

with $Z_i$ satisfying:
- $\text{Cov}(Z_i, u_i) = 0$ (exogeneity)
- $\text{Cov}(Z_i, D_i) \neq 0$ (relevance)

If treatment effects are heterogeneous ($Y_i(1) - Y_i(0)$ varies across $i$), the IV no longer estimates the ATE — it estimates the **LATE (Local Average Treatment Effect)** for **compliers**.

---

#### **2️⃣ Key IV relationships to memorize**

- **First stage:**
  $$
  D_i = \pi_0 + \pi_1 Z_i + \varepsilon_i
  \quad\Rightarrow\quad
  \pi_1 = E[D_i|Z_i=1] - E[D_i|Z_i=0] = \Pr(\text{compliers})
  $$

- **Reduced form:**
  $$
  Y_i = \delta_0 + \delta_1 Z_i + \nu_i
  \quad\Rightarrow\quad
  \delta_1 = E[Y_i|Z_i=1] - E[Y_i|Z_i=0] = E[Y_i(1)-Y_i(0)|\text{compliers}] \times \Pr(\text{compliers})
  $$

- **IV (2SLS or Wald estimator):**
  $$
  \hat{\alpha}_1^{IV} = \frac{\delta_1}{\pi_1}
  = E[Y_i(1) - Y_i(0)\mid \text{compliers}]
  $$

That last equation is the **LATE theorem** —  
the IV slope equals the *average treatment effect for compliers*.

---

#### **3️⃣ The assumptions underlying LATE**

1. **Random assignment:** $(Y_i(0), Y_i(1), D_i(0), D_i(1)) \perp Z_i$  
   → ensures the groups (treatment vs. control) differ only by the instrument.

2. **Exclusion restriction:** $Z_i$ affects $Y_i$ only through $D_i$.  
   → $Y_i(d, z) = Y_i(d)$.

3. **Monotonicity:** $D_i(1) \ge D_i(0)$ for all $i$.  
   → No *defiers* (no one does the opposite of their assignment).

---

#### **4️⃣ The four compliance types**

Based on potential treatment states $(D_i(0), D_i(1))$:

| Type | Behavior | Description |
|------|-----------|--------------|
| **Always takers** | (1, 1) | Always take treatment |
| **Never takers** | (0, 0) | Never take treatment |
| **Compliers** | (0, 1) | Take treatment *only if offered* |
| **Defiers** | (1, 0) | Take treatment *only if not offered* (ruled out by monotonicity) |

---

#### **5️⃣ How the pieces fit together numerically**

| Model            | Coefficient              | Interpretation                          |       |                                  |
| ---------------- | ------------------------ | --------------------------------------- | ----- | -------------------------------- |
| **First stage**  | $\pi_1 = E[D             | Z=1] - E[D                              | Z=0]$ | Fraction of *compliers*          |
| **Reduced form** | $\delta_1 = E[Y          | Z=1] - E[Y                              | Z=0]$ | Effect of the *offer* on outcome |
| **IV (2SLS)**    | $\frac{\delta_1}{\pi_1}$ | Average causal effect among *compliers* |       |                                  |

---

#### **6️⃣ What to write on your formula sheet**

You’ll want the following minimal, high-yield block:

$$
\begin{aligned}
\text{First Stage: } & D_i = \pi_0 + \pi_1 Z_i + \varepsilon_i, \quad \pi_1 = E[D|Z=1] - E[D|Z=0] = \Pr(\text{Compliers}) \\
\text{Reduced Form: } & Y_i = \delta_0 + \delta_1 Z_i + \nu_i, \quad \delta_1 = E[Y|Z=1] - E[Y|Z=0] = E[\Delta Y_i | C]\Pr(C) \\
\text{IV Estimate: } & \hat{\alpha}_1^{IV} = \frac{\delta_1}{\pi_1} = E[Y_i(1) - Y_i(0) | \text{Compliers}] = \text{LATE} \\
\text{Assumptions: } & (1) \text{Random Assignment} \quad (2) \text{Exclusion Restriction} \quad (3) \text{Monotonicity}
\end{aligned}
$$

---

#### **7️⃣ How this links back to Question 2 of PS6**

In PS6 Q2, you’ll be asked to:

- Compute $E[D|Z=1] - E[D|Z=0]$ (first stage)
- Compute $E[Y|Z=1] - E[Y|Z=0]$ (reduced form)
- Divide the two to get the IV estimate → the **LATE**

The interpretation will mirror the smoking/birthweight and Head Start examples:
> “The IV estimate represents the average causal effect of the treatment among compliers — those whose treatment status changes as a result of the offer.”

---

##SHORTER VERSION


Perfect — here’s your **one-page, exam-ready IV–LATE Derivation Sheet**.  
It’s concise, uses notation consistent with your class, and includes formulas, intuition, and key assumptions — exactly what you’d want on your formula sheet or to review before tackling Problem 2 or any LATE question.  

---

## 🎯 **Instrumental Variables & Local Average Treatment Effect (LATE)**

### 🔹 Setup

We observe:
$$
Y_i = \text{outcome}, \quad D_i = \text{treatment}, \quad Z_i = \text{instrument (offer)}.
$$

We assume heterogeneous treatment effects:
$$
Y_i = Y_i(0) + (Y_i(1) - Y_i(0)) D_i.
$$

But $D_i$ may be endogenous → $E[u_i|D_i] \neq 0$.  
Instrument $Z_i$ affects $D_i$, not $Y_i$ directly.

---

### 🔹 Model System

$$
\begin{aligned}
\text{(First stage)} \quad & D_i = \pi_0 + \pi_1 Z_i + \varepsilon_i \\
\text{(Reduced form)} \quad & Y_i = \delta_0 + \delta_1 Z_i + \nu_i \\
\text{(Structural / 2SLS)} \quad & Y_i = \alpha_0 + \alpha_1 D_i + u_i
\end{aligned}
$$

---

### 🔹 Population Moments

$$
\begin{aligned}
E[D_i|Z_i=1] &= \text{Treatment mean (share treated when offered)} \\
E[D_i|Z_i=0] &= \text{Control mean (share treated when not offered)} \\
E[Y_i|Z_i=1] &= \text{Outcome mean among those offered} \\
E[Y_i|Z_i=0] &= \text{Outcome mean among those not offered.}
\end{aligned}
$$

---

### 🔹 Estimands and Interpretations

| Estimator              | Formula                                          | Interpretation                               |        |                                                               |
| ---------------------- | ------------------------------------------------ | -------------------------------------------- | ------ | ------------------------------------------------------------- |
| **First Stage**        | $\pi_1 = E[D]$                                   | $[Z=1] - E[D]$                               | Z=0] $ | Effect of offer on treatment take-up (≈ share of *compliers*) |
| **Reduced Form**       | $ \delta_1 = E[Y                                 | Z=1] - E[Y                                   | Z=0] $ | Effect of offer on outcome (Intent-to-Treat)                  |
| **IV / 2SLS Estimate** | $ \hat{\alpha}_1^{IV} = \frac{\delta_1}{\pi_1} $ | Effect of treatment among *compliers* = LATE |        |                                                               |

---

### 🔹 LATE Theorem (Imbens & Angrist, 1994)

If  
1️⃣ Random assignment: $(Y(1),Y(0),D(1),D(0)) \perp Z$  
2️⃣ Exclusion restriction: $Y_i(d,z)=Y_i(d)$  
3️⃣ Monotonicity: $D_i(1)\ge D_i(0)$ (no defiers)  

then  
$$
\boxed{ \hat{\alpha}_1^{IV} = \frac{E[Y|Z=1]-E[Y|Z=0]}{E[D|Z=1]-E[D|Z=0]} = E[Y(1)-Y(0)\mid \text{compliers}] }.
$$

---

### 🔹 Compliance Types

| Type | $(D_i(0),D_i(1))$ | Behavior |
|------|----------------------|-----------|
| **Compliers** | (0, 1) | Take treatment only if offered |
| **Always-takers** | (1, 1) | Always take treatment |
| **Never-takers** | (0, 0) | Never take treatment |
| **Defiers** | (1, 0) | Do opposite of assignment (ruled out) |

---

### 🔹 Intuition

- The **instrument** shifts who receives the treatment → isolates variation due to $Z_i$.  
- The **IV ratio** (reduced form / first stage) rescales the effect of the offer into the effect of actual treatment among those who comply.  
- Hence, IV = LATE → captures the *average causal effect for the subpopulation whose treatment status changes when $Z_i$ changes.*

---

### 🔹 Quick Reference Summary

$$
\begin{aligned}
\text{First Stage: } & D_i = \pi_0 + \pi_1 Z_i + \varepsilon_i, \quad \pi_1 = \Pr(\text{Compliers}) \\
\text{Reduced Form: } & Y_i = \delta_0 + \delta_1 Z_i + \nu_i, \quad \delta_1 = E[\Delta Y_i | C]\Pr(C) \\
\text{IV / 2SLS: } & \frac{\delta_1}{\pi_1} = E[Y_i(1) - Y_i(0) \mid \text{Compliers}] = \text{LATE.}
\end{aligned}
$$

---

Would you like me to make this same derivation into a LaTeX version formatted to drop straight into your midterm formula sheet (fits on ~½ page)?