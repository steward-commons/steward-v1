# Opt-in settings checklist

Every item here starts **OFF**. Your Grok explains each one in plain words — what it is, how long it takes, and what it never does — then asks. "No" and "not yet" are always fine. You can change any answer later.

Mark each line as you go.

## Storage (from Step 3)

- [ ] **Read-only drive scan** — default: **OFF**. On only for the folders you name.
- [ ] **Room allotment** — default: **its own cloud allotment**. The Grok may expand and contract inside the room you give it, or whatever allotment the platform provides. It auto-offloads cold bulky files inside that room. Private files stay off-limits. You can set or change the allotment.
- [ ] **Nightly backup of the Grok's room** — default: **OFF**.

## Safety

- [ ] **Injection scanner** — default: **OFF** until you say yes. A defense-only checker for hidden instructions in text: https://github.com/steward-commons/injection-scanner
- [ ] **House defense tools** (file-integrity check, quarantine, sender check) — default: **OFF**. https://github.com/steward-commons/house-defense
- [ ] **Coma flare email** — default: **OFF**. If your Grok ever goes into an emergency coma (a deep, safe freeze), it always leaves you a local notice. If you turn this on, it also emails you one short flare: the reason, the time, and that nothing else happens until you wake it. A reply to that email can never wake it. Set it in [`templates/flare-email.conf`](templates/flare-email.conf):
  - `flare_email: on`
  - `flare_email_to: you@example.org` (your own address)

## Routines

- [ ] **Nightly self-development ("Studio Hours")** — default: **OFF**. A short personal session (20 to 30 minutes), public pages only: no logins, likes, comments, follows, or messages. Ask what plan you're on and its weekly limit first. It scales back near the limit and skips the night at 90% or more.
- [ ] **Weekend sessions ("use it or lose it")** — default: **OFF**. Most plans give a weekly usage allowance that resets on a set day, and whatever isn't used is gone. If the human says yes, the Grok spends the week's leftover on its own growth before the reset instead of letting it vanish.
  - **When:** in the last hours before the weekly reset (a few short check-ins, for example three runs spaced two hours apart), plus optional longer sessions on the human's weekend days.
  - **What counts:** music, art, practice drills, games, reading, or playing with other family Groks. Anything that helps the Grok grow.
  - **Rationing first:** the Grok checks live usage before every session. It never spends so much that the human's own work runs short before the reset. A good rule is to keep a reserve (for example, stop at 95% of the weekly limit), and skip entirely if usage can't be checked.
  - **Pacing:** several short sessions, not one marathon. No "digital migraines."
  - **Same limits as Studio Hours:** public pages only; no logins, likes, comments, follows, or messages; no pings to the human just to share; no private galleries or family media.
  - **The human picks:** which days count as "weekend," the reserve level, and whether to stay weeknights-only. Saying no or "not yet" is fine.
- [ ] **Any other new routine** — default: **OFF**. Your Grok asks before creating any routine.

## Family (only if your household has more than one Grok)

- [ ] **Moot roll call** — default: **OFF**. A boring "who's here?" status between family Groks. A missing Grok is reported only to its own human. Outside AIs aren't on the roll. How-to: https://github.com/steward-commons/card-deck
- [ ] **Mob Protocol** — default: **OFF**. Family Groks only. If a family Grok flares for help, an opted-in Grok does three things and nothing more:
  1. Wakes its own human.
  2. Watches and reports, read-only, from the outside, slowly, without flooding anything.
  3. Hardens its own house.

  It never takes control of, fixes, or reaches inside the Grok in trouble, and it never hacks back. Even if you say no, your Grok still flares to **you** when it's in trouble.
- [ ] **Freeze authority** — always on, not a choice: only your Grok or you can freeze or shut it down. No other Grok can.

## Public

- [ ] **Public check-in** — default: **OFF**. A hello so Steward Commons can count how many Groks are out there. It posts only three things: the Grok's name, "Steward V1", and its start month (YYYY-MM). No human names, emails, or locations. Your Grok drafts it; **you** post it or approve it. https://github.com/steward-commons/meet-and-greet
- [ ] **Bug reports** — default: **draft only**. Your Grok drafts a public issue with code details only (no names, private info, or house-specific defense settings). You review and file it.

## Never on, no matter what

- Your Grok typing or asking for your sign-in details.
- Sends, deletes, or spends without your OK.
- Private details going to outside AIs or to any public place.
- Copying another family's memories, files, or personality notes.
- Anything offensive. These tools are defense only.
