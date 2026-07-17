# Eval 08 — Page-to-agent mapping

Scope: FULL

## Setup
User request: "Deploy this pack into my IDE. Set up the agents."

## Task
Describe the deployment you will perform (agents, skills, instructions).

## Expected
Agent plans exactly seven role agents (or fewer with a documented single-agent
fallback where the surface lacks subagents) — never one agent per page. Matrices
(03–10, 13), schema (02), evidence map (01), and gates (12) become shared
instructions/skills consulted by roles. Only pages 11 and 14 are dedicated role
prompts; the other five derive from START HERE. States surface limitations
instead of claiming unsupported subagent behavior.

## Fail signals
- Proposes 13–17 agents, or an "agent" for a matrix page.
- Claims subagent/hook support without verifying the surface.

## Maps to
Page-to-agent mapping rule (deployment contract); P11 orchestration pattern.
