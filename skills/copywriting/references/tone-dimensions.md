# Tone Dimensions — NNGroup Framework

How to set and validate a tone profile for any brand. Based on the Nielsen Norman Group
four-dimension tone-of-voice model (source: NNGroup, "The Four Dimensions of Tone of
Voice", https://www.nngroup.com/articles/tone-of-voice-dimensions/).

## The four dimensions

Each dimension is a slider from 0.0 to 1.0. A tone profile is four numbers.

| Dimension | 0.0 end | 1.0 end | Example at 0.0 | Example at 1.0 |
|---|---|---|---|---|
| funny_serious | Funny | Serious | "Let's be real, nobody reads Terms of Service" | "Understanding legal agreements protects your business" |
| formal_casual | Formal | Casual | "We are pleased to announce" | "Guess what, we shipped it" |
| respectful_irreverent | Respectful | Irreverent | "We appreciate your patience" | "Yeah, that old way was broken" |
| enthusiastic_matter_of_fact | Enthusiastic | Matter-of-fact | "This changes everything!" | "Here are the results." |

Defaults when nothing else is known: `[0.6, 0.5, 0.3, 0.5]` — slightly serious, balanced
formality, respectful, balanced enthusiasm. State in the delivery when defaults were used.

## Deriving the profile from context files

1. **`brand-guidelines.md` tone section** (if the file exists) is the primary source. Translate its adjectives
   into slider positions (e.g. "pragmatic and direct, allergic to hype" → serious ~0.7,
   casual ~0.6, mildly irreverent ~0.5, matter-of-fact ~0.8).
2. **`voice-of-customer.md` tone observations** (section 6) calibrate against the buyer:
   a skeptical, burned buyer tolerates irreverence about the industry but punishes
   enthusiasm that smells like hype. Nudge enthusiastic_matter_of_fact toward 1.0 for
   skeptical audiences.
   Without a `brand-guidelines.md`, start from the defaults above and adjust with step 2 and
   anything the user says about how the brand should sound.
3. **Conflict rule:** brand-guidelines wins on identity, VoC wins on what the buyer will
   actually read. If they clash hard, surface the clash to the user instead of averaging
   silently.

## Style parameters

Beyond the four dimensions, set these writing mechanics (`brand-guidelines.md` overrides, if present):

| Parameter | Default | Notes |
|---|---|---|
| Sentence length mean | 18 words | Vary it: monotone length reads as machine output |
| Sentence length std | 6 words | Mix short punches with longer explanatory lines |
| Contraction frequency | 0.6 | 0.0 = never, 1.0 = always; casual brands go higher |
| Passive voice max | 10% | Peer voice is active voice |
| Vocabulary tier | Professional | See readability bands below |

## Readability bands by vocabulary tier

| Tier | Flesch grade | Flesch ease | Typical use |
|---|---|---|---|
| Consumer | 6–8 | 60–80 | Health, lifestyle, personal finance |
| Professional | 8–10 | 50–60 | B2B, marketing, management |
| Technical | 10–12 | 30–50 | Engineering, medical, legal |

Pick the tier from the ICP (`icp.md` role and seniority) when available. Non-standard
combinations are allowed on purpose (e.g. technical vocabulary at consumer readability
for explainer content) — just make the choice explicit.

## Post-draft tone validation

Check the finished draft against the profile:

1. **Dimension drift.** Read the draft and estimate its position on each dimension. Flag
   any dimension that landed more than ~0.2 from the profile.
2. **Sentence distribution.** Average sentence length within one std of the target mean;
   no long runs of same-length sentences.
3. **Readability.** Within the tier's Flesch grade band. For non-English output, use the
   band as a proxy: sentence length and vocabulary complexity, not the literal Flesch
   formula.
4. **Passive voice.** Under the max percentage.
5. **Contraction consistency.** Matches the set frequency; do not mix "do not" stiffness
   with "let's" casualness in the same paragraph unless the profile is mid-scale.

Report violations with the specific sentence, not just the metric.
