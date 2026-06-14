# Architecture Decision Records (ADRs)

This folder contains short, beginner‑friendly notes explaining the key decisions I made while building this project.  
These ADRs help me document *why* I chose certain AWS services or folder structures.

---

## ADR 001 — Using Amazon S3 for Hosting
I chose S3 because it is the simplest and most beginner‑friendly way to host a static website.  
It requires no servers, is very low cost, and easy to set up.

## ADR 002 — Keeping Website Code in a Separate Repository
The actual website files live in another repo.  
This keeps things organized and avoids duplication.

## ADR 003 — Including Placeholder Folders (src, scripts, tests)
Even though these folders are empty, they show good project structure and leave room for future learning.

---

These ADRs are intentionally simple because I am still learning.  

