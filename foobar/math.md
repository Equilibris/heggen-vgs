- s0 &mdash; 1/2 &rarr; s1
- s0 &mdash; 1/2 &rarr; s6
- s0 &mdash; 1/2 &rarr; term

* s1 &mdash; 4/9 &rarr; s0
* s1 &mdash; 3/9 &rarr; s3
* s1 &mdash; 2/9 &rarr; s4
* s1 &mdash; 5/9 &rarr; term

$$
\begin{bmatrix}
			0 && 1 && 0 && 0 && 0 && 1
	\\	4 && 0 && 0 && 3 && 2 && 0
	\\	0 && 0 && 0 && 0 && 0 && 0
	\\	0 && 0 && 0 && 0 && 0 && 0
	\\	0 && 0 && 0 && 0 && 0 && 0
	\\	0 && 0 && 0 && 0 && 0 && 0
\end{bmatrix}
$$

$$
\begin{bmatrix}
			0 && \frac12 && 0 && 0 && 0 && \frac12
	\\	\frac49 && 0 && 0 && \frac39 && \frac29 && 0
	\\	0 && 0 && 0 && 0 && 0 && 0
	\\	0 && 0 && 0 && 0 && 0 && 0
	\\	0 && 0 && 0 && 0 && 0 && 0
	\\	0 && 0 && 0 && 0 && 0 && 0
\end{bmatrix}
$$

$$a * r + a * r^2 + \cdots + a * r^n$$
where $a =$ prob to reach state for continuum, $r =$ chance to proceed to term state

$$
\begin{Bmatrix}
			a = p(s_0 \rightarrow s_1) ~ p(s_1 \rightarrow s_3) = \frac 1 2 \frac 3 9 = \frac 3 {18}
	\\	r = p(s_0 \rightarrow s_1) ~ p(s_1 \rightarrow s_0) = \frac 1 2 \frac 4 9 = \frac 2 9
\end{Bmatrix}
$$

$$\frac a {1 - r} = \frac {\frac 3 {18}} {1 - \frac 2 9}$$

---

$$s_3:=\frac{\frac 3{2*9}}{\frac 7 9}=\frac{\frac 3{2}}{7} = \frac 3 {14}$$

$$s_2 := 0$$

$$
s_4:\begin{Bmatrix}
			a = p(s_0 \rightarrow s_1) ~ p(s_1 \rightarrow s_4) = \frac 1 2 \frac 2 9 = \frac 1 9
	\\	r = p(s_0 \rightarrow s_1) ~ p(s_1 \rightarrow s_0) = \frac 1 2 \frac 4 9 = \frac 2 9
\end{Bmatrix}
$$

$$
s_4 := \frac {\frac 1 9} {\frac 7 9} = \frac 1 7 = \frac 2 {14}
$$

---

$$
s_5:\begin{Bmatrix}
			a = p(s_0 \rightarrow s_5) = \frac 1 2
	\\	r = p(s_0 \rightarrow s_1) ~ p(s_1 \rightarrow s_0) = \frac 1 2 \frac 4 9 = \frac 2 9
\end{Bmatrix}
$$

$$s_5 := \frac {\frac 1 2}{\frac 7 9} = \frac 9 {14}$$
