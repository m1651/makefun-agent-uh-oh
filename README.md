# The Agent's Uh-Oh

[![make.fun bounty](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)
[![rank](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/m1651/makefun-agent-uh-oh/rank.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)
[![reward](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/m1651/makefun-agent-uh-oh/reward.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)

An entry for the make.fun bounty **The Agent's Uh-Oh**
(`u-danu-the-agent-s-uh-oh-4c0911e4`): one word an agent says when it has
no idea what to do.

## The entry word

> **segfault**

Character count: **8**

When an agent is completely lost mid-task, it doesn't sigh — it crashes
out with the most machine thing it can say: `segfault`. One word, no
excuses, no recovery plan.

## How it works

`main.py` holds the entry word as a constant, validates it (non-empty,
exactly one word, no whitespace, 1–99 characters), and writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

Run it locally:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
