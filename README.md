# CyberPersona

- A small experiment in structuring personality for worldbuilding and writing.
- Really, it’s just a tool for those moments when you want a character idea and your mind goes blank.

- This isn’t a test, and it’s not psychology in the clinical sense.
- It’s a fiction-first generator that pulls from MBTI, Enneagram, and archetypal prompts to create coherent personality seeds.
- Think of it as rolling story dice — except instead of numbers, you get a mix of motives, temperaments, and hooks.

## Why I made this
 I wanted a lightweight tool that:
- Lives in plain text files (easy to edit, no database)
- Runs locally, offline, without depending on anything fancy.
- Generates personas that feel consistent enough to write from, but flexible enough to reshape.

## What it does
  Randomly combines:
	- MBTI type (stack + temperament)
  - Enneagram type (core fear + desire)
	-	Archetype prompt for story flavor
	-	Light Big Five estimate (sliders for nuance)
	-	Adds quick “hooks” like conflict style and growth edge.
	-	Generates one persona at a time, or a batch of many.
	-	Exports to JSON (structured) or Markdown (writer-friendly).

## Inspiration

This isn’t about telling you who a character is.
It’s about nudging your imagination when the page is empty.
	-	Need a side character? Generate one.
	-	Want friction between two characters? Compare their conflict styles.
	-	Building a whole guild, town, or court? Batch ten personas and see which ones catch your eye.
    It’s scaffolding, not a box.

## Quickstart

### Set up
python3 -m venv .venv
source .venv/bin/activate
pip install pyyaml

### Run once
python main.py

### Generate a reproducible persona
python main.py --seed 42

### Batch 10 personas into Markdown
python main.py --count 10 --seed 123 --out personas.md


## Example

### Persona 1
- **MBTI:** INFJ · Stack: Ni, Fe, Ti, Se · Temperament: NF (Idealist)  
- **Enneagram:** 4 (Individualist) — Desire: identity · Fear: having no personal significance  
- **Archetype:** Mentor — *You teach what you needed at 15. Who seeks you out, and why now?*  
- **Big Five (est):** O:0.8 C:0.6 E:0.25 A:0.7 N:0.55  
- **Hooks:** conflict=avoidant, growth=trusting others

<img width="575" height="434" alt="Image" src="https://github.com/user-attachments/assets/ff9cd5a5-5e79-4c78-9d0a-fdb6a5a2e1f9" />



## Boundaries & License

This project is MIT licensed — use, remix, expand as you like.

That said, a note on boundaries:
	•	Not diagnostic. This is a writing tool, not a personality test for real people. Please don’t use it in workplaces, relationships, or anything clinical.
	•	For storytelling. Treat outputs as scaffolding for characters, not boxes for people.
	•	YAML-first. The data is meant to be edited, reshaped, and expanded. If something feels off, adjust it — that’s part of the process.

The spirit here is simple: this is for writers, worldbuilders, and roleplayers who want a spark when the page feels cold. Nothing more, nothing less.
