# The World on Wednesday 18 November 2026

[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/c/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/kainze29/news-image-20261118/rank.svg)](https://make.fun/c/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/kainze29/news-image-20261118/reward.svg)](https://make.fun/c/news-image-20261118)

One front page, one day: Wednesday 18 November 2026, told in 35
stories. The masthead carries the date, the six biggest stories of
the day each get a photograph with a headline and a short summary,
and stories 7 to 35 run as a numbered list below. Every item on the
page happened, or was first reported, on 18 November 2026.

## The six top stories

1. **Trump lands in Shenzhen.** Donald Trump arrives in Shenzhen and
   is greeted by Xi Jinping. A three-way summit with Vladimir Putin
   is set for Thursday, with nuclear arms on the agenda.
2. **US-Iran Gulf war escalates.** US jets hit a missile site on
   Qeshm Island. Iran fired drones at Bahrain and Kuwait, and Bahrain
   intercepted more of them on Wednesday.
3. **Kerch Bridge hit again.** Ukraine struck the bridge for a second
   day and part of the road span fell into the strait. Russia hit
   Kyiv's bridges in reply.
4. **Voyager 1: one light-day.** Voyager 1 reached one light-day from
   Earth at 05:16 ET, about 16bn miles out, the first human-made
   object ever to get that far.
5. **Peltola wins Alaska, Democrats 56-44.** Mary Peltola beat Dan
   Sullivan for the Senate seat, the ninth flip of the midterms and
   the party's biggest majority since 2009.
6. **Ebola doubles in Congo.** The outbreak passed 11,000 cases and
   5,400 deaths. Three of four children under 5 who catch it do not
   survive.

## Stories 7 to 35

The US loses its measles elimination status after 26 years; cold
kills in Gaza's tents while the truce is at risk; Cyclone Xavier,
category 5, hits the Cook Islands; Nvidia reports $115bn and will
not bring Huang back; Trump is probing an Iran dirty-bomb claim; an
Iranian agent gets 27 years; markets slide with the S&P down 1.03%;
US tech outages hit the NSA and banks; a Russian military plane
crashes, 19 dead; the World Court is to rule on Myanmar; five EU
states plan a Rwanda hub; Israel's president taps Eisenkot to lead
the government; Turkey takes over Sozcu TV; the US blocks China's
remote access to AI chips; Anthropic is to list on Nasdaq on 19 Nov;
140,000 join protests in France; the Houthis press toward Aden; the
US scolds Kyiv on deep strikes; India records $10.07bn of foreign
portfolio inflows; Cyclone Akvan nears the Andhra coast; earthquakes
hit Papua New Guinea (6.0) and Romania (5.3); Pope Leo reveals cancer
surgery; Fela Kuti becomes the first African in the Rock and Roll
Hall of Fame; Robert Pattinson is named the new James Bond; Zverev
reaches the ATP Finals knockouts; Tiger Woods is to return in
December; "Human" is Cambridge's word of the year; the US details
$12bn of Venezuelan oil revenue; four nations urge Israel to let aid
into Gaza.

## Running it

`main.py` is Python 3.13, standard library only. It reads the
bundled `news.png`, checks it is a whole PNG under the 1 MiB limit
and no larger than 1024x1024 pixels, and writes it unchanged to
`entry.png` in the output directory. No network is used, so two runs
produce byte-identical output.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Contents

- `main.py` — the entry program described above
- `news.png` — the front page, 1024x1024 PNG, under 1 MiB
- `LICENSE` — MIT

The reporting behind each story comes from One Turn, Reuters, AP,
BBC, NPR, Al Jazeera and UN agency releases, all dated 18 November
2026. The full source list and build notes live in `BUILD-LOG.md` in
the build folder, which is not part of this repository.
