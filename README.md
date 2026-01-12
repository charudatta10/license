# Modular Project License System (MPLS)

A **composable, SPDX-compatible licensing framework** that allows projects to define permissions, restrictions, and monetization models by **selecting clauses instead of rewriting licenses**.

MPLS is designed for:

* Personal / non-commercial projects
* Dual licensing (free + paid commercial)
* Donationware
* Open-source (MIT/GPL-style)
* AI, SaaS, libraries, research, and tooling

---

## Why MPLS?

Traditional licenses are **rigid**.
Modern projects need **flexibility**.

MPLS solves this by:

* Using **modular legal clauses**
* Supporting **monetization by design**
* Remaining **SPDX-compatible**
* Being **machine-readable & generator-friendly**

> **One base system. Infinite license combinations.**

---

## Core Principles

* **Modular** – Licenses are built from reusable clauses
* **Minimal** – Only explicitly enabled permissions apply
* **Clear** – No hidden rights, no ambiguity
* **Composable** – Mix non-commercial, paid, OSS, donation clauses
* **Automatable** – Generate licenses programmatically

---

## SPDX Compatibility

MPLS uses valid SPDX custom identifiers:

```
LicenseRef-MPLS
LicenseRef-MPLS-NC-1
LicenseRef-MPLS-DUAL-1
LicenseRef-MPLS-DON-1
LicenseRef-MPLS-OSS-MIT
LicenseRef-MPLS-OSS-GPL
```

Clause-level identifiers are also supported internally:

```
LicenseRef-MPLS-Clause-U1
LicenseRef-MPLS-Clause-P1
LicenseRef-MPLS-Clause-D4
```

---

## License Structure

Each MPLS license consists of:

1. **SPDX Identifier**
2. **Enabled Clause List**
3. **Legal Text for Each Clause**
4. **Warranty & Liability Disclaimer**

Any permission **not explicitly granted is prohibited**.

---

## Clause Categories

### Usage

* Personal
* Educational
* Commercial (allowed or prohibited)

### Payment

* Free
* One-time fee
* Subscription
* Donationware

### Distribution

* No redistribution
* Redistribution allowed
* Modification allowed
* Copyleft enforcement

### Source Code

* Closed distribution allowed
* Source disclosure required

### Attribution & Branding

* Attribution required or optional
* Trademark restrictions

### Warranty & Liability

* No warranty
* No liability

---

## Predefined License Profiles

### MPLS-NC-1 (Personal / Non-Commercial)

Free for personal and educational use.
Commercial use and redistribution are prohibited.

```
SPDX-License-Identifier: LicenseRef-MPLS-NC-1
Clauses: U1, U2, U3, P0, D1, S1, A1, W1, W2
```

---

### MPLS-DUAL-1 (Dual License)

Free for non-commercial use.
Commercial use requires a paid license.

```
SPDX-License-Identifier: LicenseRef-MPLS-DUAL-1
Clauses: U1, U2, U3, U4, P1, D2, S1, A1, W1, W2
```

---

### MPLS-DON-1 (Donationware)

Free to use with optional donations.

```
SPDX-License-Identifier: LicenseRef-MPLS-DON-1
Clauses: U1, U2, U4, P3, D2, S1, A1, W1, W2
```

---

### MPLS-OSS-MIT (Permissive Open Source)

Equivalent to MIT-style licensing.

```
SPDX-License-Identifier: LicenseRef-MPLS-OSS-MIT
Clauses: U1, U2, U4, P0, D2, D3, S1, A1, W1, W2
```

---

### MPLS-OSS-GPL (Copyleft Open Source)

Equivalent to GPL-style licensing.

```
SPDX-License-Identifier: LicenseRef-MPLS-OSS-GPL
Clauses: U1, U2, U4, P0, D2, D3, D4, S2, A1, W1, W2
```

---

## License Generator

A minimal Python-based generator is included.

### Example

```bash
python generate_license.py > LICENSE.md
```

### Generator Inputs

* SPDX Identifier
* Clause ID list

The generator outputs a **complete, legal-grade license file**.

---

## Recommended Repository Layout

```
/
├── LICENSE.md
├── README.md
├── generate_license.py
└── licenses/
    ├── MPLS-NC-1.md
    ├── MPLS-DUAL-1.md
    └── MPLS-OSS-MIT.md
```

---

## Best Practices

* Always include `SPDX-License-Identifier` at the top of files
* Clearly summarize the license in `README.md`
* Use predefined profiles where possible
* Avoid mixing contradictory clauses

---

## Disclaimer

MPLS is provided as a licensing framework.
You are responsible for ensuring compliance with local laws and regulations.



