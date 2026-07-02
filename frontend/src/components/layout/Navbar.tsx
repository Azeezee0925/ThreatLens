"use client";

import { Bell, ShieldCheck, UserCircle } from "lucide-react";

export default function Navbar() {
  return (
    <header className="h-16 bg-slate-900 border-b border-slate-800 flex items-center justify-between px-8">

      <div>
        <h1 className="text-2xl font-bold">
          ThreatLens Dashboard
        </h1>

        <p className="text-sm text-slate-400">
          Enterprise Threat Intelligence Platform
        </p>
      </div>

      <div className="flex items-center gap-6">

        <Bell className="cursor-pointer hover:text-cyan-400 transition" />

        <div className="flex items-center gap-2 bg-slate-800 px-4 py-2 rounded-xl">
          <ShieldCheck className="text-green-400" size={20} />
          <span>System Online</span>
        </div>

        <UserCircle size={34} className="cursor-pointer hover:text-cyan-400 transition" />

      </div>

    </header>
  );
}