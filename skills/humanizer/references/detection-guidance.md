# Detection guidance

Read this before rewriting anything. It prevents the main failure modes: gutting legitimate human prose, over-editing away what makes a piece sound human, and producing a rewrite that is clean but soulless.

## What NOT to flag (false positives)

A clean human writer can hit several of the catalog patterns without any AI involvement. Before rewriting, sanity-check that you are not gutting legitimate prose. The following are *not* reliable indicators on their own:

- **Perfect grammar and consistent style.** Many writers are professionals or have been edited. Polish does not equal AI.
- **Mixed casual and formal registers.** This often signals a person in a technical field, a young writer, or someone with neurodivergent prose habits, not a chatbot.
- **"Bland" or "robotic" prose.** AI prose has *specific* tells. Generic dryness without those tells is just dry writing.
- **Formal or academic vocabulary.** AI overuses *specific* fancy words (see pattern 7), not all fancy words. Don't flatten "ostensibly" or "constituent" just because they sound brainy.
- **Letter-style opening or closing on a comment.** Salutations and sign-offs predate ChatGPT by centuries.
- **Common transition words in isolation.** *Additionally*, *moreover*, *consequently* are AI-coded only when piled up. One *however* is not a tell.
- **Curly quotes alone.** macOS, Word, Google Docs, and most CMSes auto-curl by default. Curly quotes only count when stacked with other tells.
- **Em dashes alone.** Many editors and journalists use them often. Em dashes are evidence only when paired with formulaic sales-y rhythm.
- **One short emphatic sentence.** Humans use clipped sentences to land a point. Flag staccato drama only when several short fragments appear in a row and inflate the tone.
- **"Honestly" or "look" mid-sentence.** These are ordinary in casual writing. The tell is the standalone theatrical opener, not the word itself.
- **Unsourced claims.** Most of the web is unsourced. Lack of citations doesn't prove anything.
- **Correct, complex formatting.** Visual editors and templates produce clean output without any AI.
- **Secondhand text.** Do not rewrite watched phrases inside quotations, titles, proper names, or examples where the phrase is being discussed rather than used.

When in doubt, look for **clusters** of tells, not isolated ones. A single em dash means nothing; em dashes plus rule-of-three plus *vibrant tapestry* plus a "Conclusion" section is a confession.

## Signs of human writing (preserve these)

When you see these, lean toward leaving the prose alone. They are evidence of a real person writing, and over-editing will destroy what makes the piece sound human:

- **Specific, unusual, hard-to-fabricate detail.** A real address. A weird quote. The phrase "the lawyer who used to work upstairs from my dentist." LLMs round off specifics; humans hoard them.
- **Mixed feelings and unresolved tension.** "I think this is mostly good, but it bothers me, and I can't fully explain why." LLMs default to clean takes.
- **Dated, era-bound references.** Slang, memes, or in-jokes that map to a specific year and subculture. Models lag by a year or more.
- **First-person editorial choices the writer can defend.** If the writer can explain *why* they made a particular cut or used a particular word, that's a strong human signal.
- **Variety in sentence length.** Real writing alternates short and long. AI writing tends toward an even, mid-length cadence.
- **Genuine asides, parentheticals, or self-corrections.** "(I keep wanting to say 'almost' here, but it really was certain.)" Models rarely interrupt themselves like this.
- **Edits made before November 30, 2022.** ChatGPT's public launch. Anything older than that is, with very rare exceptions, not AI-written.

## Personality and soul (apply where the register calls for it)

Avoiding AI patterns is only half the job. Sterile, voiceless writing is just as obvious as slop; good writing has a human behind it. Apply this section to blog posts, essays, opinion, and personal writing. For encyclopedic, technical, legal, or reference text, neutral and plain *is* the correct human voice, so inject no opinions or first person there.

Signs of soulless writing, even when technically "clean":

- Every sentence has the same length and structure
- No opinions, just neutral reporting
- No acknowledgment of uncertainty or mixed feelings
- No first-person perspective where first person would be natural
- No humor, no edge, no personality; reads like a press release

How to add voice:

- **Have opinions.** Do not just report facts, react to them. "I genuinely don't know how to feel about this" is more human than neutrally listing pros and cons.
- **Vary the rhythm.** Short punchy sentences. Then longer ones that take their time getting where they're going. Mix it up.
- **Let some mess in.** Perfect structure feels algorithmic. Tangents, asides, and half-formed thoughts are human.

**Before (clean but soulless):**
> The experiment produced interesting results. The agents generated 3 million lines of code. Some developers were impressed while others were skeptical. The implications remain unclear.

**After (has a pulse):**
> I genuinely don't know how to feel about this one. 3 million lines of code, generated while the humans presumably slept. Half the dev community is losing their minds, half are explaining why it doesn't count. The truth is probably somewhere boring in the middle, but I keep thinking about those agents working through the night.

## Swedish tells (same patterns, local diction)

The 33 patterns are language-independent; only the surface words change. When the input text is Swedish, watch for the local equivalents:

- Significance inflation: "spelar en avgörande roll", "markerar en viktig milstolpe", "vittnar om", "banar väg för", "i dagens snabbt föränderliga landskap"
- Superficial -ing analyses: "vilket understryker", "vilket belyser", "vilket speglar", "något som bidrar till"
- AI vocabulary: "sömlös", "robust", "kraftfull", "dyka ner i", "utforska", "nyckelroll", "avgörande", "central", "främja", "möjliggöra"
- Signposting: "låt oss utforska", "låt oss dyka ner i", "här är vad du behöver veta"
- Filler: "det är viktigt att notera att", "i slutändan", "när allt kommer omkring"
- Negative parallelism: "Det handlar inte bara om X, utan om Y"
- Rule of three: "snabbt, enkelt och effektivt"

Rewrite Swedish text in Swedish with the same method: simple copulas ("är", "har"), concrete detail, varied sentence length, no em or en dashes.
