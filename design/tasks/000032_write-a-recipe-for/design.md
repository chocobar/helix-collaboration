# Design: Chicken Soup Recipe

## Overview

Create a single markdown file containing a classic chicken soup recipe. No code, no tooling — just a well-structured `.md` document.

## Structure

The recipe file uses standard markdown elements:

- **H1** for the recipe title
- **Bold text** for prep time, cook time, and servings metadata
- **H2** sections for Ingredients, Instructions, and Tips
- **Unordered list** for ingredients with quantities
- **Ordered list** for step-by-step instructions
- **Unordered list** with bold labels for tips

## Decisions

- **Format:** Plain markdown (no frontmatter or metadata schemas) — keeps it simple and universally readable.
- **Recipe style:** Classic homestyle chicken soup with egg noodles — broadly appealing and straightforward.
- **File name:** `chicken-soup.md` in the repository root — simple and discoverable.

## Implementation Notes

- Created a single `chicken-soup.md` file in the repo root
- Used bold text for metadata (prep/cook/servings) rather than a table — cleaner for a simple recipe
- Included practical tips section covering make-ahead, freezing, and variations
- All ingredients have specific quantities for reproducibility
