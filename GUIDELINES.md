# Writing More Successful Machine Learning Research Papers

Best practices to impress reviewers and fellow researchers, based on insights from Prof. Marc Aubreville.

## 1. Don't Assume the Reader Knows About the Importance of Your Topic

You know what you're doing and why you're doing it. But your average reader will not. Always have in mind that you will have at least four kinds of readers:

- **Your supervisor** - Don't write for your supervisor. A good supervisor knows already what you are doing and especially why you are doing it.
- **People in the same research field** - They mostly know all the related work and terms, but the closer they are to your exact topic, the fewer exist.
- **People in closely related research areas** - They won't exactly know your specific problems but have good general understanding. **This is your target audience.**
- **People from remotely related research areas** - This is the biggest group and likely includes some of your reviewers. They don't know all related work or why your research is important.

**Bottom line:** Spend enough time on motivation. Formulate clear thoughts and back up your claims with literature. All of this goes into the introduction section.

## 2. Write About Novel Insights, Not Technical Novelties

Most papers state "novelty" at the end of introduction because journals/conferences require it. However, authors often misunderstand this as needing ground-breaking new methods.

**Reality:** Insights are the most important aspect of any paper. If the reader feels informed about something they didn't know beforehand, that's novelty!

**Bottom line:** Spend time on analysis and interpretation of your results. If your method shows better results than state-of-the-art, first doubt your results! Analyze, interpret  then publish.

## 3. Don't Assume the Reader Knows Your Previous Work

Research is incremental, but assume none of your readers has read your previous papers. Don't force them to read it.

Most reviewers are senior scientists or professors with busy schedules. Make your paper **fully self-contained**:

- Don't use your own abbreviations/names from previous work without explanation
- Don't expect readers to know your previous model architectures
- Don't make heavy use of referrals to previous work

## 4. Follow the Scientific Method

**Bad approach (HARKing - Hypothesis After Results are Known):**
1. Develop a method
2. Test that method
3. Analyze results
4. Interpret why the method worked

**Good approach:**
1. **Observation** - What did you observe in data that makes you think you could improve on state-of-the-art?
2. **Hypothesis** - How do you need to design your method?
3. **Test Design** - How will you specifically test if your hypothesis is true or false? Ensure your test is not biased!
4. **Experiment** - Run inference on independent test set
5. **Analysis** - Analyze results and relate to your hypothesis

**Structure your paper around this flow** - your method should always be the test for your hypothesis.

## 5. Be Your Own Devil's Advocate

Be humble and aware of your research limitations. Identify weaknesses before reviewers do:

**Questions to ask yourself:**
- Could findings be due to lucky choice of dataset/hyperparameters/random states?
- Why did you choose X,Y,Z in your experimental setup?
- Will this work for other datasets beyond what was demonstrated?

**Goal:** Describe limits of what you did so others don't make avoidable mistakes.

## 6. Avoid "Unnecessary Mathiness"

Formulas are great for precision but often take readers much longer to understand than verbal descriptions or pseudocode.

**Why people overuse math:**
- Makes paper seem more sophisticated
- Can help pass peer review
- Shows technical depth

**Reality:** Hard-to-understand papers have smaller long-term impact.

**Bottom line:** Use formulas when they help readers understand more precisely what you did. Don't add math to show off.

## 7. Concept First, Writing Second

**Don't write while results are unknown.** Writing a paper is like writing a novel - know the main storyline before writing the first paragraph.

**You'll likely waste time if you start writing before:**
- Having final results
- Running analysis on results
- Understanding what story you're telling

**Exception:** Start writing the introduction early. It helps identify relevant related work and clarifies your own understanding.

## 8. Write the Abstract Last

The abstract is the most important part - it's what most people will read. Write it last because only after writing the discussion will you know the key essences and takeaways.

**Abstract structure:** Wrap up every part of the paper (introduction/methods/results/discussion) in 1-3 sentences each.

**Pre-writing exercise:** Try to explain your concept on a single sheet of paper with a thick sharpie. If you can summarize your paper this way, you're ready to write the abstract.

## Best Practices Checklist

### Content Quality
- [ ] Clear motivation that explains why your research matters
- [ ] Novel insights supported by thorough analysis, not just technical novelty
- [ ] Self-contained paper that doesn't require reading previous work
- [ ] Scientific method structure (hypothesis -> method -> test -> analysis)
- [ ] Identified and discussed limitations
- [ ] Appropriate use of math/formulas (only when necessary)
- [ ] Complete results and analysis before writing

### Writing and Structure
- [ ] Abstract written last, summarizing entire paper
- [ ] Title clearly expresses main contribution
- [ ] Problem well-motivated and separated from contributions
- [ ] Clear conceptual outline or pseudocode provided
- [ ] All assumptions formally stated
- [ ] Proofs included for nontrivial claims
- [ ] Clean separation between design, description, results, and interpretation

### Reproducibility and Transparency
- [ ] All hyperparameters listed with ranges explored
- [ ] Source code and computing infrastructure specified
- [ ] Evaluation metrics formally defined
- [ ] Algorithms used for each result clearly stated
- [ ] Experimental analysis goes beyond single metrics
- [ ] Proof-read for clarity and correctness

## Final Reminder

Remember: You spent many hours on research, failing, redoing, and finally getting decent results. Don't rush the writing phase - these guidelines will help ensure your hard work gets the recognition it deserves.
