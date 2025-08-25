import yaml, random, argparse, json
from pathlib import Path

def load_yaml(path: str):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def pick_mbti(rng, mbti_data):
    t = rng.choice(list(mbti_data["types"].keys()))
    return {"type": t, **mbti_data["types"][t]}

def pick_enneagram(rng, ennea_data):
    k = rng.choice(list(ennea_data["types"].keys()))
    entry = ennea_data["types"][k]
    return {"type": k, **entry}

def pick_archetype(rng, arch_data):
    return rng.choice(arch_data["archetypes"])

def estimate_big_five(mbti_type: str, ennea_type: str):
    # tiny toy estimate — good enough for flavor
    E = 0.7 if "E" in mbti_type else 0.3
    if ennea_type in {"4","5","9"}: E -= 0.05
    if ennea_type in {"7"}: E += 0.10
    N = 0.7 if "N" in mbti_type else 0.4
    J = 0.6 if "J" in mbti_type else 0.4
    return {
        "Openness": round(N, 2),
        "Conscientiousness": round(0.5 + (J-0.5)*0.6, 2),
        "Extraversion": round(E, 2),
        "Agreeableness": round(0.55 if "F" in mbti_type else 0.45, 2),
        "Neuroticism": round(0.55 if ennea_type in {"4","6"} else 0.45, 2),
    }

def generate_persona(rng, mbti_data, ennea_data, arch_data):
    mbti = pick_mbti(rng, mbti_data)
    ennea = pick_enneagram(rng, ennea_data)
    arch = pick_archetype(rng, arch_data)
    return {
        "mbti": {
            "type": mbti["type"],
            "stack": mbti["stack"],
            "temperament": mbti["temperament"],
        },
        "enneagram": {
            "type": ennea["type"],
            "name": ennea["name"],
            "core_desire": ennea["core_desire"],
            "core_fear": ennea["core_fear"],
        },
        "archetype": arch,
        "big_five_estimate": estimate_big_five(mbti["type"], ennea["type"]),
        "hooks": {
            "conflict_style": rng.choice(["assertive", "conciliatory", "strategic", "avoidant"]),
            "growth_edge": rng.choice(["trusting others", "setting boundaries", "embracing chaos", "speaking up"]),
        },
    }

def to_markdown(personas):
    lines = []
    for i, p in enumerate(personas, 1):
        lines.append(f"## Persona {i}")
        lines.append(f"- **MBTI:** {p['mbti']['type']}  ·  Stack: {', '.join(p['mbti']['stack'])}  ·  Temperament: {p['mbti']['temperament']}")
        e = p["enneagram"]
        lines.append(f"- **Enneagram:** {e['type']} ({e['name']}) — Desire: *{e['core_desire']}* · Fear: *{e['core_fear']}*")
        a = p["archetype"]
        lines.append(f"- **Archetype:** {a['name']} — _{a['prompt']}_")
        b5 = p["big_five_estimate"]
        lines.append(f"- **Big Five (est):** O:{b5['Openness']} C:{b5['Conscientiousness']} E:{b5['Extraversion']} A:{b5['Agreeableness']} N:{b5['Neuroticism']}")
        h = p["hooks"]
        lines.append(f"- **Hooks:** conflict={h['conflict_style']}, growth={h['growth_edge']}")
        lines.append("")  # blank line
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Generate worldbuilding personas")
    parser.add_argument("--seed", type=int, default=None, help="Reproducible output if set")
    parser.add_argument("--count", type=int, default=1, help="How many personas to generate")
    parser.add_argument("--out", type=str, default=None, help="Optional output path (.md or .json)")
    args = parser.parse_args()

    rng = random.Random(args.seed)
    mbti_data = load_yaml("mbti.yaml")
    ennea_data = load_yaml("enneagram.yaml")
    arch_data = load_yaml("archetypes.yaml")

    personas = [generate_persona(rng, mbti_data, ennea_data, arch_data) for _ in range(args.count)]

    # Print to console (quick win)
    for i, p in enumerate(personas, 1):
        print(f"\n=== Persona {i} ===")
        print("MBTI:", p["mbti"]["type"], "| Stack:", p["mbti"]["stack"], "| Temperament:", p["mbti"]["temperament"])
        print("Enneagram:", p["enneagram"]["type"], p["enneagram"]["name"])
        print("Archetype:", p["archetype"]["name"])
        print("Hooks:", p["hooks"])

    # Opt export
    if args.out:
        out_path = Path(args.out)
        if out_path.suffix.lower() == ".json":
            out_path.write_text(json.dumps(personas, indent=2))
        elif out_path.suffix.lower() == ".md":
            out_path.write_text(to_markdown(personas))
        else:
            raise SystemExit("Use .md or .json for --out")
        print(f"\nSaved → {out_path.resolve()}")

if __name__ == "__main__":
    main()