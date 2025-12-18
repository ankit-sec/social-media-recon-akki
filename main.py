#!/usr/bin/env python3
"""
AKKI SocialRecon
Professional Linux CLI OSINT Tool
Created by Ankit Kumar
"""

import asyncio
import argparse
from datetime import datetime
from typing import Dict, Any

import aiohttp
import colorama
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.panel import Panel
from rich.text import Text

colorama.init(autoreset=True)


class LinuxCLIReconTool:
    def __init__(self):
        self.console = Console()
        self.platforms = self._load_platforms()

    # ---------------- BANNER ---------------- #
    def show_banner(self):
        banner = Text("""
 █████╗ ██╗  ██╗██╗  ██╗██╗
██╔══██╗██║ ██╔╝██║ ██╔╝██║
███████║█████╔╝ █████╔╝ ██║
██╔══██║██╔═██╗ ██╔═██╗ ██║
██║  ██║██║  ██╗██║  ██╗██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝
""", style="bold green")

        panel = Panel(
            banner,
            title="[bold cyan]AKKI SocialRecon[/bold cyan]",
            subtitle="[green]Linux CLI OSINT Tool | Created by Ankit Kumar[/green]",
            border_style="green",
        )
        self.console.print(panel)

    # --------------- PLATFORMS --------------- #
    def _load_platforms(self) -> Dict[str, Dict[str, Any]]:
        return {
            "github": {
                "url": "https://github.com/{}",
                "indicators": ["repositories", "joined github"],
                "emoji": "💻",
            },
            "gitlab": {
                "url": "https://gitlab.com/{}",
                "indicators": ["gitlab"],
                "emoji": "🦊",
            },
            "twitter": {
                "url": "https://twitter.com/{}",
                "indicators": ["followers", "following"],
                "emoji": "🐦",
            },
            "instagram": {
                "url": "https://www.instagram.com/{}/",
                "indicators": ["followers", "posts"],
                "emoji": "📸",
            },
            "facebook": {
                "url": "https://www.facebook.com/{}",
                "indicators": ["facebook"],
                "emoji": "📘",
            },
            "linkedin": {
                "url": "https://www.linkedin.com/in/{}",
                "indicators": ["linkedin"],
                "emoji": "💼",
            },
            "reddit": {
                "url": "https://www.reddit.com/user/{}",
                "indicators": ["karma"],
                "emoji": "👽",
            },
            "youtube": {
                "url": "https://www.youtube.com/@{}",
                "indicators": ["subscribers"],
                "emoji": "📺",
            },
            "telegram": {
                "url": "https://t.me/{}",
                "indicators": ["tgme"],
                "emoji": "✈️",
            },
            "snapchat": {
                "url": "https://www.snapchat.com/add/{}",
                "indicators": ["snapchat"],
                "emoji": "👻",
            },
            "tiktok": {
                "url": "https://www.tiktok.com/@{}",
                "indicators": ["tiktok"],
                "emoji": "🎵",
            },
            "pinterest": {
                "url": "https://www.pinterest.com/{}/",
                "indicators": ["pinterest"],
                "emoji": "📌",
            },
            "medium": {
                "url": "https://medium.com/@{}",
                "indicators": ["medium"],
                "emoji": "📝",
            },
            "wordpress": {
                "url": "https://{}.wordpress.com",
                "indicators": ["wordpress"],
                "emoji": "🌐",
            },
            "soundcloud": {
                "url": "https://soundcloud.com/{}",
                "indicators": ["soundcloud"],
                "emoji": "🎧",
            },
            "twitch": {
                "url": "https://www.twitch.tv/{}",
                "indicators": ["twitch"],
                "emoji": "🎮",
            },
        }

    # ---------------- CHECK ---------------- #
    async def check_username(self, session, platform, username):
        cfg = self.platforms[platform]
        url = cfg["url"].format(username)

        try:
            async with session.get(url, timeout=10) as resp:
                text = await resp.text()
                found = any(i in text.lower() for i in cfg["indicators"])
                return {
                    "platform": platform,
                    "url": url,
                    "exists": found,
                    "status": resp.status,
                    "emoji": cfg["emoji"],
                }
        except Exception:
            return {
                "platform": platform,
                "url": url,
                "exists": False,
                "status": "ERR",
                "emoji": "❌",
            }

    # ---------------- SCAN ---------------- #
    async def hunt(self, username: str):
        self.console.print(
            f"\n🎯 Target Username: [bold cyan]{username}[/bold cyan]"
        )
        self.console.print(f"📡 Platforms Loaded: {len(self.platforms)}\n")

        results = []

        async with aiohttp.ClientSession() as session:
            with Progress(
                SpinnerColumn(),
                TextColumn("[cyan]Scanning[/cyan]"),
                BarColumn(),
                TextColumn("{task.completed}/{task.total}"),
                console=self.console,
            ) as progress:
                task = progress.add_task("scan", total=len(self.platforms))

                tasks = [
                    self.check_username(session, p, username)
                    for p in self.platforms
                ]

                for coro in asyncio.as_completed(tasks):
                    res = await coro
                    results.append(res)
                    progress.advance(task)

        return results

    # ---------------- RESULT ---------------- #
    def show_results(self, username, results):
        found = [r for r in results if r["exists"]]

        table = Table(title="🧠 OSINT RESULTS", header_style="bold green")
        table.add_column("Platform")
        table.add_column("Status")
        table.add_column("URL")
        table.add_column("HTTP")

        if found:
            for r in found:
                table.add_row(
                    f"{r['emoji']} {r['platform']}",
                    "[green]FOUND[/green]",
                    r["url"],
                    str(r["status"]),
                )
        else:
            table.add_row("-", "[red]NOT FOUND[/red]", "-", "-")

        self.console.print()
        self.console.print(table)
        self.console.print(
            f"\n🕒 Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )


# ---------------- MAIN ---------------- #
async def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("username", nargs="?", help="Username / keyword to scan")
    args = parser.parse_args()

    tool = LinuxCLIReconTool()
    tool.show_banner()

    if not args.username:
        tool.console.print(
            "\n[bold yellow]Enter Username / Name / Keyword to scan:[/bold yellow]"
        )
        username = input("➤ ").strip()
        if not username:
            tool.console.print("[red]No input provided. Exiting.[/red]")
            return
    else:
        username = args.username

    results = await tool.hunt(username)
    tool.show_results(username, results)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user")
