CLAUSES = {
    "U1": "Permission is granted to use this Software for personal, private, and non-commercial purposes.",
    "U2": "Permission is granted to use this Software for educational, academic, and research purposes, provided no commercial benefit is derived.",
    "U3": "Commercial use of this Software is strictly prohibited without an explicit commercial license.",
    "U4": "Commercial use of this Software is permitted, subject to compliance with applicable payment and licensing terms.",
    "P0": "No payment is required for use of this Software under the permitted terms.",
    "P1": "Commercial use requires a one-time license fee as defined by the Licensor.",
    "P2": "Commercial use requires an active subscription license maintained in good standing.",
    "P3": "Use of this Software is permitted without payment; voluntary donations are encouraged but not required.",
    "D1": "Redistribution of this Software, in original or modified form, is prohibited.",
    "D2": "Redistribution of this Software is permitted, provided this license is included in full.",
    "D3": "Modification of this Software is permitted.",
    "D4": "Any distributed modification must be licensed under the same terms as this Software.",
    "S1": "Distribution of source code is not required.",
    "S2": "Source code must be made available when distributing this Software or derivative works.",
    "A1": "The original copyright notice and attribution must be retained.",
    "A2": "Attribution is appreciated but not required.",
    "A3": "Use of the Licensor’s name, trademarks, or branding is prohibited without permission.",
    "W1": "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND.",
    "W2": "IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY."
}

def generate_license(spdx_id, clause_ids):
    body = "\n\n".join(CLAUSES[c] for c in clause_ids)
    return f"""SPDX-License-Identifier: {spdx_id}

Modular Project License System (MPLS)

Enabled Clauses:
{", ".join(clause_ids)}

{body}
"""

if __name__ == "__main__":
    print(generate_license(
        "LicenseRef-MPLS-DUAL-1",
        ["U1","U2","U3","U4","P1","D2","S1","A1","W1","W2"]
    ))
