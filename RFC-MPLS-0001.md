# RFC MPLS-0001

## Modular Project License System (MPLS) v1.0

**Category:** Standards Track
**Status:** Final
**Version:** 1.0
**Updated:** 2026-01-10
**Author:** MPLS Working Group

---

## Abstract

This document specifies the **Modular Project License System (MPLS)**, a composable licensing framework that enables software projects to define usage rights, distribution rules, and monetization terms by selecting standardized legal clauses rather than rewriting entire licenses.

MPLS is designed to be **SPDX-compatible**, **legally precise**, **machine-readable**, and **automation-friendly**, while supporting modern licensing needs including non-commercial use, dual licensing, donationware, and open-source models.

---

## 1. Terminology

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHOULD**, **MAY**, and **OPTIONAL** in this document are to be interpreted as described in RFC 2119.

* **Software**: Any source code, binary, model, artifact, or derivative work covered by this license.
* **Licensor**: The copyright holder or entity granting rights.
* **Licensee**: Any individual or entity using the Software.
* **Clause**: A self-contained legal permission or restriction.
* **Profile**: A predefined set of clauses forming a complete license.

---

## 2. Design Goals

MPLS is designed to satisfy the following goals:

1. **Modularity** – Licenses are composed from reusable clauses.
2. **Minimalism** – Only explicitly enabled permissions apply.
3. **Clarity** – No implicit or assumed rights.
4. **SPDX Compatibility** – All licenses MUST have valid SPDX identifiers.
5. **Automation** – Licenses MUST be generatable programmatically.
6. **Monetization Support** – Payment terms are first-class citizens.

---

## 3. License Architecture

An MPLS license consists of:

1. A **base system identifier**
2. A **unique SPDX license identifier**
3. A **finite list of enabled clauses**
4. The **legal text** corresponding to each enabled clause
5. Warranty and liability disclaimers

Any right **not explicitly granted** by an enabled clause **MUST be considered prohibited**.

---

## 4. SPDX Identification

### 4.1 Base Identifier

All MPLS licenses SHALL use the SPDX custom license namespace:

```
LicenseRef-MPLS
```

### 4.2 Derived Identifiers

Derived licenses SHALL follow this pattern:

```
LicenseRef-MPLS-<PROFILE>-<VERSION>
```

Examples:

```
LicenseRef-MPLS-NC-1
LicenseRef-MPLS-DUAL-1
LicenseRef-MPLS-OSS-MIT
LicenseRef-MPLS-OSS-GPL
```

### 4.3 Clause Identifiers

Clause-level identifiers MAY be used internally:

```
LicenseRef-MPLS-Clause-U1
LicenseRef-MPLS-Clause-D4
```

---

## 5. Clause Categories

MPLS defines the following clause categories:

* **Usage**
* **Payment**
* **Distribution & Modification**
* **Source Code Disclosure**
* **Attribution & Branding**
* **Warranty & Liability**

Each clause MUST be independent and MUST NOT contradict another clause within the same license.

---

## 6. Normative Clause Definitions

### 6.1 Usage Clauses

* **U1** — Personal Use Permitted
* **U2** — Educational Use Permitted
* **U3** — Commercial Use Prohibited
* **U4** — Commercial Use Permitted

### 6.2 Payment Clauses

* **P0** — No Payment Required
* **P1** — One-Time License Fee Required
* **P2** — Subscription License Required
* **P3** — Donationware (Voluntary)

### 6.3 Distribution & Modification Clauses

* **D1** — Redistribution Prohibited
* **D2** — Redistribution Permitted
* **D3** — Modification Permitted
* **D4** — Copyleft Requirement

### 6.4 Source Code Clauses

* **S1** — Source Disclosure Not Required
* **S2** — Source Disclosure Required on Distribution

### 6.5 Attribution & Branding Clauses

* **A1** — Attribution Required
* **A2** — Attribution Optional
* **A3** — Trademark Use Prohibited

### 6.6 Warranty & Liability Clauses (Mandatory)

* **W1** — No Warranty
* **W2** — No Liability

All MPLS licenses **MUST include W1 and W2**.

---

## 7. License Profiles (Normative)

### 7.1 MPLS-NC-1 (Non-Commercial)

```
SPDX-License-Identifier: LicenseRef-MPLS-NC-1
Clauses: U1, U2, U3, P0, D1, S1, A1, W1, W2
```

### 7.2 MPLS-DUAL-1 (Dual License)

```
SPDX-License-Identifier: LicenseRef-MPLS-DUAL-1
Clauses: U1, U2, U3, U4, P1, D2, S1, A1, W1, W2
```

### 7.3 MPLS-DON-1 (Donationware)

```
SPDX-License-Identifier: LicenseRef-MPLS-DON-1
Clauses: U1, U2, U4, P3, D2, S1, A1, W1, W2
```

### 7.4 MPLS-OSS-MIT (Permissive)

```
SPDX-License-Identifier: LicenseRef-MPLS-OSS-MIT
Clauses: U1, U2, U4, P0, D2, D3, S1, A1, W1, W2
```

### 7.5 MPLS-OSS-GPL (Copyleft)

```
SPDX-License-Identifier: LicenseRef-MPLS-OSS-GPL
Clauses: U1, U2, U4, P0, D2, D3, D4, S2, A1, W1, W2
```

---

## 8. License Generation

An MPLS license MAY be generated using automated tooling.

Generated licenses MUST:

* Include the SPDX identifier
* Enumerate enabled clauses
* Include the full legal text of each clause
* Preserve ordering and clarity

---

## 9. Compatibility Considerations

* MPLS-OSS-MIT is MIT-compatible
* MPLS-OSS-GPL is GPL-compatible
* MPLS licenses MAY be dual-licensed with standard OSI licenses
* Clause conflicts MUST be rejected by generators

---

## 10. Security & Legal Considerations

MPLS does not grant patent rights unless explicitly stated.
Licensors are responsible for ensuring compliance with local laws and export controls.

---

## 11. Versioning & Governance

* MPLS follows **semantic versioning**
* Clause meanings MUST NOT change within a major version
* New clauses MAY be added in minor versions
* MPLS v1.x licenses remain valid indefinitely

---

## 12. License of This Specification

This specification is released under:

```
SPDX-License-Identifier: LicenseRef-MPLS-OSS-MIT
```

---

## Status of This RFC

**This document is final and frozen as MPLS v1.0.**

No backward-incompatible changes are permitted within the v1.x series.


