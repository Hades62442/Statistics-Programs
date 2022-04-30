## basic design
1. determine which confidence interval
    - if proportion, p hat distr
    - if s unknown, and normally distributed, then t distr
    - else, z distr

## p distr
1. get p hat {p}
2. get a [100(1-a)%] {a}
3. show what z value to get [z of a/2]
4. get n {n}
5. find interval
    - p hat +- z value * (sqrt((p hat * q hat)/n)) {q}

## t distr
1. get n {n}
2. get a [100(1-a)%] {a}
3. show what t value to get [t of n-1, 1-a/2]
4. get t value {t}
5. get s {s}
6. get x bar {x}
7. find mean
    - mean = x bar +- t value * (s/sqrt(n)) {m}

## z distr
1. get a [100(1-a)%] {a}
2. show what z value to get [z of a/2]
3. get x bar {x}
4. get sigma {s}
5. get n {n}
6. find interval
    - x bar +- z value * (sigma/sqrt(n))

## vars used
1. p distr - p, a, z, n, q
2. t distr - n, a, t, s, x, m
3. z distr - a, z, x, s, n
4. other - v {type of distr}, c {value of part after +- in p,t distr}

## changes
- input percentage instead of a value, find a value, then show what z val to find {j}