# Paper Template

## Usage

1. Fork this repository.
2. Enable GitHub Workflow write access to your forked repository:
   1. Navigate to `https://github.com/<your_username>/<this_repo>/settings/actions`
   2. Scroll down to the "Workflow permissions" section.
   3. Select "Read and write permissions".
   4. Click "Save".
3. Clone your forked repository to your local machine.
4. Apply conference/journal style file:
   1. Remove `arxiv.sty`.
   2. Add the style files provided by your target venue.
   3. Modify `paper.tex` to align with the expected premble and bibliography style.
   4. Update `paper.tex` included files as needed based on your venue's requirements.
5. Write your paper in `.tex` section files.
6. Commit and push your changes to your forked repository.
   - The `.github/workflows/todo.yml` workflow will automatically create issues for you from `FIXME` and `TODO` comments.
   - The `.github/workflows/build.yml` workflow will compile your paper and generate a PDF release on each push.
