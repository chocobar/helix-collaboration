# Design: Blog Post About Sorting Algorithms

## Overview

A standalone Markdown blog post explaining common sorting algorithms. No code repository changes needed — the deliverable is a single `.md` file.

## Structure

```
blog-post-sorting-algorithms.md
├── Title + Introduction (why sorting matters)
├── Bubble Sort
├── Selection Sort
├── Insertion Sort
├── Merge Sort
├── Quick Sort
├── Heap Sort (bonus)
├── Comparison Table
└── Conclusion (when to use what)
```

## Key Decisions

- **Language for code examples:** Python — widely readable, concise syntax, good for pseudocode-like examples.
- **Algorithms covered:** The 5 classic comparison-based sorts plus Heap Sort. These cover O(n^2) and O(n log n) categories well. Radix/Counting sort omitted to keep scope manageable and focused on comparison-based sorting.
- **Audience level:** Beginner to intermediate. Assumes basic programming knowledge but not CS theory.
- **Format:** Pure Markdown with fenced code blocks. No external dependencies, images, or interactive elements — keeps it portable and easy to publish anywhere.

## Content Approach

Each algorithm section follows the same template:
1. One-sentence summary
2. How it works (plain English, 2-3 paragraphs)
3. Python implementation (short, readable)
4. Complexity analysis (table: best/average/worst time + space)

The comparison table at the end consolidates all complexity info plus stability and in-place properties.

## Implementation Notes

- Deliverable is a single file `sorting-algorithms.md` in the repo root — no other files needed.
- Used a readable (list-comprehension based) Quick Sort implementation rather than in-place Lomuto/Hoare partition, since clarity matters more than performance in a blog post.
- Post is ~2400 words, within the 1500-3000 target range.
- Each algorithm section follows the exact same template for consistency: summary, how-it-works, code, complexity table.
- Included a practical "when to use what" conclusion section and a mention of real-world hybrid algorithms (Timsort, dual-pivot Quick Sort) to bridge theory and practice.
