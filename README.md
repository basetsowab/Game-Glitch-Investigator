# Game Glitch Investigator: Applied AI Debugging System

## Overview

Game Glitch Investigator is an applied AI system that helps developers diagnose and debug common game issues. Users input a description of a glitch, and the system analyzes it to identify the type of bug, suggest possible causes, and recommend fixes.

This project demonstrates how AI systems can be designed to perform structured reasoning tasks using retrieval, rule-based logic, and evaluation techniques.

---

## Original Project (Modules 1–3)

This project is based on my earlier Game Glitch Investigator project. The original version focused on organizing and analyzing glitch reports using basic Python logic.

For this final version, the project was extended into a complete applied AI system by adding:

* Retrieval-based reasoning using a knowledge base
* Confidence scoring to measure reliability
* Guardrails to handle uncertainty
* Automated evaluation and testing

---

## System Architecture

The system follows a modular pipeline:

Input → Validation → Classification → Retrieval → Reasoning → Output

### Components:

* Input Validator: Ensures the glitch report is usable
* Glitch Classifier: Matches keywords to glitch types
* Knowledge Base: Retrieves known causes and fixes
* AI Reasoner: Generates structured debugging output
* Evaluator/Test Harness: Measures system reliability
* Guardrails: Adds warnings based on confidence levels

System diagram is located in the `/assets` folder.

---

## Features

* Glitch classification (collision, animation, audio, UI, crash)
* Retrieval-based debugging suggestions
* Confidence scoring system
* Guardrails for low-confidence outputs
* Built-in evaluation and testing script
* Modular AI system design

---

## Setup Instructions

```bash
git clone https://github.com/YOUR_USERNAME/Game-Glitch-Investigator.git
cd Game-Glitch-Investigator

pip install -r requirements.txt
python app.py
```

To run tests:

```bash
python test.py
```

---

## Sample Interactions

### Example 1

Input:

```
My player keeps falling through the floor near a platform edge
```

Output:

```
Glitch Type: collision
Confidence: 0.85

Likely Causes:
- Missing collider
- Thin collision boundary

Suggested Fixes:
- Check collider placement
- Increase collider thickness

Guardrail: High confidence, but still verify in your game engine.
```

---

### Example 2

Input:

```
Character stuck in T-pose and animation not working
```

Output:

```
Glitch Type: animation
Confidence: 0.75

Likely Causes:
- Broken animation state
- Missing transition

Suggested Fixes:
- Check animator transitions
- Verify animation clips
```

---

### Example 3

Input:

```
Game broken
```

Output:

```
Glitch Type: unknown
Confidence: 0.30

Guardrail: Low confidence. Human review recommended.
```

---

## Testing and Reliability

The system includes a test harness that runs multiple predefined glitch scenarios.

Results:

* 5 out of 6 tests passed
* Accuracy: approximately 83%
* Performs best with detailed inputs
* Performance decreases with vague or short descriptions

Confidence scoring is used to indicate how reliable each output is.

---

## Design Decisions

* Used a keyword-based retrieval approach for transparency and simplicity
* Organized logic into separate modules for maintainability and clarity
* Added confidence scoring to prevent over-reliance on AI outputs
* Prioritized explainability over complex machine learning models

---

## Limitations

* Relies on keyword matching rather than deep natural language understanding
* Limited knowledge base does not cover all game engines or edge cases
* Cannot directly debug or execute game code

---

## Ethics and Responsibility

* The system is designed to assist, not replace, human debugging
* Outputs are suggestions and should always be verified
* Guardrails are used to indicate uncertainty
* The system avoids generating misleading or fabricated debugging steps

---

## Reflection

This project demonstrates how to build AI systems that are not only functional but also reliable and responsible. It highlights the importance of testing, modular design, and clear communication of uncertainty in AI outputs.

---

## Demo

Add your Loom walkthrough link here.

---

## Repository Structure

```
Game-Glitch-Investigator/
│
├── app.py
├── glitch_analyzer.py
├── evaluator.py
├── logic_utils.py
├── test.py
├── requirements.txt
│
├── data/
│   └── glitch_knowledge_base.json
│
├── assets/
│   └── system_diagram.png
```

---

## What This Project Demonstrates

* Ability to build end-to-end AI systems
* Understanding of retrieval-based reasoning
* Experience with testing and evaluation
* Focus on responsible AI design and reliability
