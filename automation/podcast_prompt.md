# Deep-dive podcast prompt

These are the steering instructions passed to NotebookLM's audio hosts (via
`notebooklm generate audio --prompt-file automation/podcast_prompt.md`) to
produce the daily deep-dive podcast. The single source in the notebook is that
day's chosen deep-dive article, so "the article provided" is unambiguous.

---

Create a deep-dive podcast about today's featured article — the single source
provided in this notebook. Read through that article and ground every claim in
it; do not invent facts, numbers, or quotes.

Walk through the article in this order:

1. **Business context** — the problem it addresses and why it matters to the
   company and the wider industry. Set the stage for a curious, non-expert
   listener.
2. **Technical details** — explain how it actually works in accessible terms:
   name the specific models, techniques, and architectures, and the key
   numbers and results. Define the jargon as you go.
3. **Impact** — what it changes in practice, both the results actually realized
   and the potential or transferable lessons for other teams.

Then shift from explanation to analysis:

4. **Novelty** — how genuinely new is this? Separate a true advance from
   established practice applied well, and say which parts are which.
5. **Similar and related work** — the most relevant comparable articles,
   papers, or systems, and how this one differs from them.
6. **Helpful opinions and caveats** — expert-style commentary: strengths,
   limitations, open questions, and who should care. Clearly flag this as
   opinion, distinct from the article's own claims.

Tone: engaging and conversational, but precise and faithful to the source.
Keep commentary and opinion clearly separated from the article's factual claims.
