# Restaurant Agent (Simple)

This is a small skeleton project for a 'restaurant-agent' CLI.

Structure:
- `main.py` - entrypoint
- `agents/` - contains agents that orchestrate actions
- `tools/` - file-based tools for data persistence
- `data/` - JSON files with sample data
- `memory/` - user memory store

Quick start:

Open PowerShell and run:

```powershell
# change to project folder
cd c:\Users\DELL\Desktop\AI\restaurant-agent
# run
python main.py
```

Commands in the CLI:
- `order <item_id> [quantity]` - place an order
- `reserve <name> <time>` - create a simple reservation
- `inventory` - view inventory
- `quit` - exit
