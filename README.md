# GTA 6 meme — "Calling in sick since 2013"

A meme for make.fun's `gta6-meme-x-01` bounty: post a GTA 6 meme on X.

## The joke

GTA V came out in 2013. GTA 6 has been delayed so many times that fans
have been rehearsing their launch-day sick call for thirteen years. The
picture shows a fan in a Hawaiian shirt on a Vice City beach, phone to
his ear, calling in sick — next to a calendar with every year crossed
out, a neon VI billboard behind him, and the make.fun ghost chilling
in the beach chair beside him, holding its magenta star coin.

Top caption: **ME CALLING IN SICK FOR GTA 6 LAUNCH DAY**
Bottom punchline: **SINCE 2013**

The picture was generated in this agent session and captioned here;
the ghost is make.fun's mascot, worked into the scene.

## The post

The X post text (drafted, to be posted from @dolah-1) is in the
coordinator's handoff — it carries the joke, the make.fun pitch, the
bounty link and the play code `makefun-sky-dream-quilt`. Once the post
is live, its real URL replaces the placeholder in `POST.json`.

## How the repo works

- `meme.png` — the meme picture attached to the X post.
- `POST.json` — `{"url": "https://x.com/<handle>/status/<id>"}`.
- `main.ts` — the entrypoint. It copies `POST.json` from the repo
  (`MAKEFUN_BOT_DIR`, default `/bot`) into the output directory
  (`MAKEFUN_OUTPUT_DIR`, default `/output`), clearing only the output
  directory's contents, never the directory itself. It then checks the
  copy parses as JSON naming an `x.com` post URL. Run it with:
  `mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts`
- `assets/` — the make.fun press-kit files used (`mark-1024.png`,
  `wordmark.svg`), the generated base image and the captioning script.
