![WIP](https://img.shields.io/badge/status-Work_in_Progress-yellow?style=for-the-badge&logoColor=white)

<br>

<h1 align="center"> ＣｙｂｅｒＰｅｒｓｏｎａ </h1>

<p align="center">
  <img src="https://github.com/user-attachments/assets/fd6fdfc1-1799-4f3f-9284-4aab1fa9aaac" width="220"/>
  &nbsp;&nbsp;&nbsp;&nbsp;
	<img src="https://github.com/user-attachments/assets/591dd256-de2a-4d3e-aba9-f918e5a41dea" width="220" height="140" />
  &nbsp;&nbsp;&nbsp;&nbsp;
    <img src="https://github.com/user-attachments/assets/a9fc2177-93fe-4941-985b-e70f19fb4320" height="140"/>
</p>

## What It Is
- An experiment in structuring personality for worldbuilding and writing
- Currently being upgraded to a more advanced "personality-engine" 
- For now, it’s just a tool for those moments when you want a character idea and your mind goes blank.

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
	-	MBTI type (stack + temperament)
  	- 	Enneagram type (core fear + desire)
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

<p align="center">
<img width="750" height="750" alt="Image" src="https://github.com/user-attachments/assets/b6ee4b77-f5ac-42c8-b591-e1874c98f011" />
</p>


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

<br>

### Screenshot

<img width="575" height="434" alt="Image" src="https://github.com/user-attachments/assets/af1d0969-0a09-410b-9681-b3dff8e5c9e9" />

## Boundaries & License

This project is MIT licensed — use, remix, expand as you like.

That said, a note on boundaries:
	•	Not diagnostic. This is a writing tool, not a personality test for real people. Please don’t use it in workplaces, relationships, or anything clinical.
	•	For storytelling. Treat outputs as scaffolding for characters, not boxes for people.
	•	YAML-first. The data is meant to be edited, reshaped, and expanded. If something feels off, adjust it — that’s part of the process.

The spirit here is simple: this is for writers, worldbuilders, and roleplayers who want a spark when the page feels cold. Nothing more, nothing less.






