# AI engineering — lessons

Working through LLM engineering from the ground up, using a real dataset instead of a toy one.

Each lesson is a script you **run**, not read. The point of a lesson is to watch something
behave — usually break — and then have a name for what you saw.

## The data

`data/hydtp_sample.json` — 200 public posts by
[@HYDTP](https://x.com/HYDTP), the Hyderabad Traffic Police account on X (290K followers),
already tagged across six dimensions (topic, hook type, category, location, timing, platform).

These are the account's **own published posts**, collected during a college analytics project.
Nothing private is in this repo.

Each script uses the full local dataset if it's on the machine, and falls back to this sample
otherwise — so everything here runs straight after a clone.

## Lessons

### `01_wobbly_ruler.py` — why a moody model destroys your ability to measure

An eval set is a measuring tape: its one job is to tell you whether a change made things better.
This simulates two prompts, where prompt B is genuinely better, and asks whether your eval set
can actually tell.

At temperature 0, the same eval run five times gives `[86, 86, 86, 86, 86]`.
At temperature 0.6, the same eval, same prompt, nothing changed between runs, gives
`[71, 69, 56, 63, 69]` — and it picks the *worse* prompt roughly 6 times out of 10.

That's what "your eval set stops working" means. Not that it errors — that it keeps producing
confident numbers that are noise, and you make real decisions on them.

```
python3 01_wobbly_ruler.py
```

Change the temperature at the bottom of the file and re-run to see where it breaks down.

### `02_python_you_need.py` — six exercises, no theory

The Python that every later lesson is built from: `json.load`, dicts, lists, `for`/`if`,
counting into a dict, filtering, and writing a function. Fill in the blanks; the file checks
itself and tells you what's wrong.

```
python3 02_python_you_need.py
```

Exercise 4 is the one that matters most — counting things into a dict *is* how you score
accuracy, and it shows up again in the eval lessons.

## Coming next

Calling an LLM from code · structured output and constrained decoding · classification on real
tweets · building an eval set by hand · measuring accuracy · error analysis · confidence and
calibration · embeddings and retrieval.
