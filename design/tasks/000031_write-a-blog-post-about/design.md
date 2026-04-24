# Design: Blog Post About Open Source Standards

## Overview

A standalone Markdown blog post explaining open source standards -- what they are, why they matter, and how developers can engage with them. The deliverable is a single `.md` file. No code repository changes needed.

## Structure

```
open-source-standards.md
├── Title + Introduction (why standards matter in software)
├── What Are Open Source Standards? (definition, open vs proprietary)
├── Standards That Shape the Internet
│   ├── HTTP and HTML (W3C, IETF)
│   ├── SQL (ISO/IEC, community implementations)
│   ├── OAuth 2.0 and OpenID Connect (IETF/OpenID Foundation)
│   ├── OpenAPI Specification (Linux Foundation)
│   ├── OCI Container Standards (Open Container Initiative)
│   └── OpenTelemetry (CNCF)
├── Benefits of Open Standards
├── Challenges and Trade-offs
├── How to Get Involved
└── Conclusion
```

## Key Decisions

- **Standards selected:** A mix of foundational (HTTP, SQL) and modern (OpenAPI, OCI, OpenTelemetry) standards. This shows that open standards aren't just historical -- they're actively being created today.
- **Audience level:** General developer audience. Assumes programming experience but not deep standards-body knowledge.
- **Tone:** Informative but opinionated -- advocates for open standards while honestly addressing trade-offs.
- **Format:** Pure Markdown, no external dependencies or images. Keeps it portable, consistent with the project's existing blog post format.

## Content Approach

Each standard section follows the same template:
1. One-sentence summary of what it is
2. Who maintains it and how governance works (1-2 sentences)
3. Why it matters / real-world impact (1-2 paragraphs)

The benefits/challenges sections use concrete examples rather than abstract claims.

## Implementation Notes

- Deliverable is a single file `open-source-standards.md` in the repo root.
- Following the same Markdown format and structure conventions as the existing sorting algorithms blog post.
- Target length: ~2000 words.
- No code examples needed for this topic -- the focus is conceptual rather than implementation-oriented.
- The "How to Get Involved" section should include actionable steps (joining mailing lists, attending working group meetings, contributing to reference implementations) rather than vague encouragement.
