"use client";

import Searchbox from "@/components/investigation/Searchbox";

export default function InvestigatePage() {
  return (
    <div className="space-y-8">

      <div>
        <h1 className="text-4xl font-bold">
          Investigate IOC
        </h1>

        <p className="text-slate-400 mt-2">
          Analyze IP Addresses, Domains, URLs and File Hashes
        </p>
      </div>

      <Searchbox />

    </div>
  );
}