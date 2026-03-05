# Paper Template

## Usage

1. Fork this repository.
2. Enable GitHub Workflow write access to your forked repository:
   1. Navigate to `https://github.com/<your_username>/<this_repo>/settings/actions`
   2. Scroll down to the "Workflow permissions" section.
   3. Select "Read and write permissions".
   4. Click "Save".
3. Clone your forked repository to your local machine.
4. Configure the NeurIPS style (already vendored as `neurips_2025.sty`):
   - `paper.tex` uses `\usepackage[preprint]{neurips_2025}`; drop `[preprint]` for anonymous submission, add `final` after acceptance, and pick a track option (`main`, `position`, `dandb`, `creativeai`, `sglblindworkshop`, `dblblindworkshop`) if needed.
   - Citation style is set to numbered, sorted, and compressed; adjust `\PassOptionsToPackage` or `\setcitestyle` in `paper.tex` / `common.tex` if your track requires different settings.
   - Fill in the author block according to double-blind or camera-ready requirements.
5. Write your paper in `.tex` section files.
6. Commit and push your changes to your forked repository.
   - The `.github/workflows/todo.yml` workflow will automatically create issues for you from `FIXME` and `TODO` comments.
   - The `.github/workflows/build.yml` workflow will compile your paper and generate a PDF release on each push.
