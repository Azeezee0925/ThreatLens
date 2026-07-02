"use client";

import HistoryTable from "@/components/history/Historytable";

export default function HistoryPage() {

  return (

    <div className="space-y-8">

      <div>

        <h1 className="text-4xl font-bold text-white">

          Investigation History

        </h1>

        <p className="text-slate-400 mt-2">

          View all previous IOC investigations

        </p>

      </div>

      <HistoryTable />

    </div>

  );

}