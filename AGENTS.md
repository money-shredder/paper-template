# AGENTS.md

This file provides guidance to Claude Code (claude.ai/code) when working with research paper LaTeX files in this repository, incorporating best practices from successful ML research papers.

## Project Overview

This repository contains the complete LaTeX source for a research paper to be submitted to a top ML venue. The writing follows established guidelines for impactful ML research papers.

## Research Paper Writing Guidelines (GUIDELINES.md)

Based on established best practices for successful ML research papers:

### Core Writing Principles
- **Audience**: Write for researchers in closely related fields who don't know your specific topic
- **Insights over novelty**: Focus on novel understanding rather than just technical innovations
- **Self-contained**: Make the paper fully understandable without requiring knowledge of previous work
- **Scientific method**: Follow Observation → Hypothesis → Test → Analysis structure
- **Critical analysis**: Identify limitations and potential weaknesses before reviewers do
- **Appropriate complexity**: Use math/formulas only when they aid understanding, not to appear sophisticated

### Writing Process
- **Concept before writing**: Have final results and complete analysis before writing (except introduction)
- **Abstract last**: Write the abstract after completing the entire paper to properly summarize key insights
- **Introduction early**: Start writing the introduction to clarify research questions and identify related work

### Content Quality Principles
- Clear motivation explaining why research matters
- Novel insights supported by thorough analysis
- Self-contained presentation without external dependencies
- Scientific method structure with formal hypothesis testing
- Identified and discussed limitations
- Appropriate use of mathematical notation
- Complete results and analysis before writing begins

## Editing Guidelines

### Source Code Conventions
- Use semantic line breaks for git-based collaboration convention and avoid long lines of source text

### LaTeX Conventions
- Use `\Cref{}` for cross-references to figures, tables, sections, etc.
- Use and update definitions in `common.tex` for shared commands and packages
- General mathematical notation defined in `math_commands.tex`
- Algorithmic descriptions in `algorithms/` directory

### Math Quality Guidelines
- All equations or inequalities must have well-defined symbols
- Symbol definitions should have specified domains
  - Domains are symbols and should also be defined in clear words

### Citation Style
- BibTeX entries in `references.bib`
- Use `\cite{}` for inline citations
