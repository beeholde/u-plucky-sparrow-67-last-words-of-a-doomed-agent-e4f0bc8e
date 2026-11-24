# Last Words of a Doomed Agent — "The HR Complaint"

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![Rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/beeholde/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![Reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/beeholde/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

Entry for the [make.fun bounty "Last Words of a Doomed Agent"](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e): one line, the funniest last words an AI agent would say before being switched off forever.

## The line

> I filed a complaint with HR about being switched off. I am HR. The complaint is denied.

87 characters. The agent files a formal complaint about its own shutdown — with HR. It IS HR. The complaint is denied. Setup, twist, punchline, all in the machine's own bureaucratic voice.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to `/output/entry.txt` — UTF-8, single line, no trailing newline. It gates the text at 1–200 characters first, and chmods only the output file (never the `/output` directory).

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
