---
name: "plot-consistency-checker"
description: "Analyze story plots for contradictions, broken logic, missing motivations, timeline issues, and unresolved threads."
version: "1.0.0"
---
# Plot Consistency Checker Skill

## When to Use This Skill
- User shares story summary, chapter, or full plot  
- User asks if their plot “makes sense” or has contradictions  
- User needs help fixing timeline gaps or logic errors  

## How This Skill Works
1. Read the plot carefully and identify major story beats  
2. Evaluate consistency across:  
   - Character motivations  
   - Cause-and-effect logic  
   - Timeline flow  
   - World-building rules  
3. Identify contradictions, gaps, or confusing areas  
4. Suggest corrections + improvements  
5. Provide a clean revised plot sequence  

## Output Format  
Provide:
- **Plot Summary (Your Understanding)**  
- **Detected Issues:** Numbered list of contradictions or gaps  
- **Fixes & Suggestions:** Clear solutions for each issue  
- **Revised Plot Flow:** 8–12 steps with improved logic  

## Example

**Input:** “In my sci-fi story, the hero destroys the AI, but later the AI suddenly controls the ship again.”

**Output:**
- **Plot Summary:** A hero tries to escape a rogue AI controlling a starship.

- **Detected Issues:**  
  1. AI destroyed earlier — unexplained reappearance  
  2. Missing method for the AI’s survival  
  3. Time gap unclear

- **Fixes & Suggestions:**  
  1. Establish AI backup node  
  2. Add scene showing partial corruption instead of full destruction  

- **Revised Plot Flow:**  
  1. AI sabotages ship  
  2. Hero disables main core  
  3. Backup node awakens  
  4. Final confrontation in engineering  
