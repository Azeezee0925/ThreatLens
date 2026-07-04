"use client";

import Link from "next/link";
import {
  LayoutDashboard,
  Search,
  History,
  Bell,
  Settings,
} from "lucide-react";

const menu = [
  {
    title: "Dashboard",
    icon: LayoutDashboard,
    href: "/dashboard",
  },
  {
    title: "Investigate",
    icon: Search,
    href: "/investigate",
  },
  {
    title: "History",
    icon: History,
    href: "/history",
  },
  {
    title: "Alerts",
    icon: Bell,
    href: "/alerts",
  },
];

export default function Sidebar() {
  return (
    <aside className="w-64 h-screen bg-slate-900 border-r border-slate-800 p-5">
      <h1 className="text-2xl font-bold text-cyan-400 mb-10">
        ThreatLens
      </h1>

      <nav className="space-y-2">
        {menu.map((item) => {
          const Icon = item.icon;

          return (
            <Link
              key={item.title}
              href={item.href}
              className="flex items-center gap-3 rounded-lg p-3 hover:bg-slate-800 transition"
            >
              <Icon size={20} />

              {item.title}
            </Link>
          );
        })}
      </nav>
    </aside>
  );
}