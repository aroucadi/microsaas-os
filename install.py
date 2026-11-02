#!/usr/bin/env python3
"""
Micro-SaaS Founder OS - Installer for Google Antigravity
======================================================
Installs the 7 Micro-SaaS skills into your global Antigravity config
or into a specific project workspace.

Usage:
    py install.py                  # Installs globally to ~/.gemini/config/skills/
    py install.py --global         # Explicit global install
    py install.py --workspace .    # Installs to current workspace (.agents/skills/)
    py install.py --list           # Check status of installed skills
    py install.py --uninstall      # Remove skills from target
    py install.py --dry-run        # Preview actions without modifying disk
"""

import argparse
import os
import shutil
import sys
from pathlib import Path

SKILL_NAMES = [
    "microsaas-hub",
    "microsaas-discovery",
    "microsaas-research",
    "microsaas-validation",
    "microsaas-product",
    "microsaas-distribution",
    "microsaas-metrics",
]

def get_global_skills_dir() -> Path:
    home = Path.home()
    return home / ".gemini" / "config" / "skills"

def get_workspace_skills_dir(workspace_path: str) -> Path:
    ws = Path(workspace_path).resolve()
    # Antigravity discovers workspace skills in .gemini/skills or .agents/skills
    return ws / ".gemini" / "skills"

def install_skills(target_dir: Path, source_dir: Path, dry_run: bool = False):
    print(f"\n🚀 Installing Micro-SaaS OS skills to: {target_dir}")
    if not dry_run:
        target_dir.mkdir(parents=True, exist_ok=True)

    installed_count = 0
    for name in SKILL_NAMES:
        src = source_dir / name
        dst = target_dir / name
        if not src.exists():
            print(f"  ❌ Source skill not found: {src}")
            continue

        if dry_run:
            print(f"  [DRY-RUN] Would copy: {src.name} -> {dst}")
            installed_count += 1
            continue

        try:
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            print(f"  ✅ Installed {name} -> {dst}")
            installed_count += 1
        except Exception as e:
            print(f"  ❌ Failed to copy {name}: {e}")

    print(f"\n🎉 Successfully installed {installed_count}/{len(SKILL_NAMES)} skills.")
    print("Restart or start a new conversation in Antigravity to activate your new skills!\n")

def list_installed_skills(target_dir: Path):
    print(f"\n🔍 Checking installed skills in: {target_dir}")
    if not target_dir.exists():
        print("  Directory does not exist. No skills installed.")
        return

    found = 0
    for name in SKILL_NAMES:
        dst = target_dir / name
        skill_file = dst / "SKILL.md"
        if skill_file.exists():
            print(f"  ✅ [INSTALLED] {name}")
            found += 1
        else:
            print(f"  ⚪ [NOT FOUND] {name}")
    print(f"\nTotal: {found}/{len(SKILL_NAMES)} Micro-SaaS skills active.")

def uninstall_skills(target_dir: Path, dry_run: bool = False):
    print(f"\n🗑️  Uninstalling Micro-SaaS OS skills from: {target_dir}")
    if not target_dir.exists():
        print("  Directory does not exist. Nothing to uninstall.")
        return

    removed = 0
    for name in SKILL_NAMES:
        dst = target_dir / name
        if dst.exists():
            if dry_run:
                print(f"  [DRY-RUN] Would remove: {dst}")
                removed += 1
            else:
                shutil.rmtree(dst)
                print(f"  🗑️  Removed {name}")
                removed += 1
    print(f"\nRemoved {removed} skills.\n")

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(
        description="Micro-SaaS Founder OS Installer for Google Antigravity"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--global",
        dest="is_global",
        action="store_true",
        default=True,
        help="Install globally to ~/.gemini/config/skills/ (default)",
    )
    group.add_argument(
        "--workspace",
        type=str,
        help="Install into a specific project workspace path (e.g. --workspace .)",
    )

    action_group = parser.add_mutually_exclusive_group()
    action_group.add_argument(
        "--list",
        action="store_true",
        help="List status of installed skills",
    )
    action_group.add_argument(
        "--uninstall",
        action="store_true",
        help="Uninstall skills from target destination",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview actions without making changes on disk",
    )

    args = parser.parse_args()

    repo_root = Path(__file__).parent.resolve()
    source_skills_dir = repo_root / "skills"

    if args.workspace:
        target_dir = get_workspace_skills_dir(args.workspace)
    else:
        target_dir = get_global_skills_dir()

    if args.list:
        list_installed_skills(target_dir)
    elif args.uninstall:
        uninstall_skills(target_dir, dry_run=args.dry_run)
    else:
        install_skills(target_dir, source_skills_dir, dry_run=args.dry_run)

if __name__ == "__main__":
    main()
