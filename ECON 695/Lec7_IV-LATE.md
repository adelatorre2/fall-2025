prompt
```
kay we need to do problem set 6 which is review for midterm 2 and I really need to do well. One of the thing my professor told me to study is the IV//LATE model and in perticular:

  

The second stage, why in the reduced form you get the product of the fractional compliers times the local average treatment effects, which is the median treatment effects among the compliers.

00:11

and the IV-estimate, basically the ratio of the reduced form and the first stage, give you the local average treatment effect.

00:17

make sure you can prove that without the help with the cheat sheet. You could put out the cheat sheet, but because of course I'm not going to test you that directly, there are going to be variation of that.

00:29

[I might for instance change] one assumption [of that model]

00:32

and see how does that change your first stage, how does that change your reduced forms.

00:36

So that's what I mean. You can't just copy paste the exact same model, but you should be able to

00:43

kind of understand how we get there.

  

My question is where does that come form and how do i study that?!?!
```

That key result your professor emphasized — that in the IV/LATE model the *reduced form* equals the product of the fraction of compliers and their *local average treatment effect*, and that dividing by the *first stage* gives the LATE — comes directly from the potential outcomes derivation in Lecture 7 on IV–LATE.

Here’s the logic broken down clearly:

---

### 1. The setup

We start with an instrument $Z_i$ (e.g., an encouragement to take treatment), a treatment $D_i$, and an outcome $Y_i$.  
Each unit has potential outcomes:
$$
Y_i(1), Y_i(0) \quad \text{and} \quad D_i(1), D_i(0)
$$
corresponding to whether they receive the treatment or not, given instrument values 1 or 0.

---

### 2. Four groups under the monotonicity assumption
Based on $(D_i(0), D_i(1))$:

| Group | Behavior | Share |
|--------|-----------|--------|
| **Never-takers (NT)** | $(0,0)$ | $\Pr(NT)$ |
| **Always-takers (AT)** | $(1,1)$ | $\Pr(AT)$ |
| **Compliers (C)** | $(0,1)$ | $\Pr(C)$ |
| **Defiers (D)** | $(1,0)$ | $\Pr(D) = 0$ under monotonicity |

---

### 3. Expected outcomes by instrument group
Under random assignment and the exclusion restriction $Y_i(d,z) = Y_i(d)$, we have:

$$
E[Y_i|Z_i=1] = E[Y_i(0)|NT]\Pr(NT) + E[Y_i(1)|C]\Pr(C) + E[Y_i(1)|AT]\Pr(AT)
$$
$$
E[Y_i|Z_i=0] = E[Y_i(0)|NT]\Pr(NT) + E[Y_i(0)|C]\Pr(C) + E[Y_i(1)|AT]\Pr(AT)
$$

---

### 4. The reduced form difference
Subtracting gives the **reduced form** (impact of the instrument on the outcome):

$$
\omega_1 = E[Y_i|Z_i=1] - E[Y_i|Z_i=0] = \Pr(C) \cdot E[Y_i(1) - Y_i(0) \mid C]
$$

So the reduced form is the **fraction of compliers times the average treatment effect for compliers**

---

### 5. The first stage difference
Similarly, the **first stage** (effect of instrument on treatment) is:

$$
\epsilon_1 = E[D_i|Z_i=1] - E[D_i|Z_i=0] = \Pr(C)
$$

---

### 6. The IV ratio (the LATE)
Taking the ratio of the reduced form to the first stage:

$$
\frac{\omega_1}{\epsilon_1}
= \frac{\Pr(C) \cdot E[Y_i(1) - Y_i(0) \mid C]}{\Pr(C)}
= E[Y_i(1) - Y_i(0) \mid C]
$$

This is the **Local Average Treatment Effect (LATE)** — the *average causal effect among compliers*, the subgroup whose treatment status is actually changed by the instrument 

---

### 7. How to study this for your midterm

To really internalize this:
1. **Memorize the three IV assumptions**:
   - Random assignment of $Z_i$
   - Exclusion restriction $Y_i(d,z) = Y_i(d)$
   - Monotonicity (no defiers)
2. **Understand what changes if one fails** — e.g., if monotonicity fails, defiers add a negative term to the reduced form.
3. **Be able to re-derive steps 3–6** quickly on paper.
4. **Practice explaining intuition**:
   - The *reduced form* is the effect of encouragement on the outcome.
   - The *first stage* is the effect of encouragement on treatment.
   - Their ratio isolates the causal effect *only for those who respond* (the compliers).

---

Would you like me to create a compact 1-page LaTeX study sheet summarizing this derivation (with the formulas cleanly formatted and labeled for practice before your midterm)? It would help you reproduce this proof from scratch in under 3 minutes.