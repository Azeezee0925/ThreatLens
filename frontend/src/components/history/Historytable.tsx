"use client";

import { useEffect, useState } from "react";
import { getHistory } from "@/services/history";

interface InvestigationHistory {
  id: number;
  ioc: string;
  ioc_type: string;
  status: string;
  threat_score: number;
  virustotal_score: number;
  alienvault_score: number;
  investigated_at: string;
}

export default function HistoryTable() {
  const [history, setHistory] = useState<InvestigationHistory[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadHistory() {
      try {
        const data = await getHistory();
        setHistory(data);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    }

    loadHistory();
  }, []);

  if (loading) {
    return <p className="text-slate-400">Loading history...</p>;
  }

  return (
    <div className="overflow-x-auto rounded-xl border border-slate-800 bg-slate-900">
      <table className="w-full text-sm">
        <thead className="bg-slate-800 text-slate-200">
          <tr>
            <th className="p-4 text-left">IOC</th>
            <th className="p-4">Type</th>
            <th className="p-4">Status</th>
            <th className="p-4">Threat</th>
            <th className="p-4">VirusTotal</th>
            <th className="p-4">AlienVault</th>
            <th className="p-4">Date</th>
          </tr>
        </thead>

        <tbody>
          {history.map((item) => (
            <tr
              key={item.id}
              className="border-t border-slate-800 hover:bg-slate-800/50"
            >
              <td className="p-4 font-medium text-white">{item.ioc}</td>

              <td className="text-center capitalize text-slate-300">
                {item.ioc_type}
              </td>

              <td
                className={`text-center font-semibold ${
                  item.status === "Safe"
                    ? "text-green-400"
                    : item.status === "Suspicious"
                    ? "text-yellow-400"
                    : "text-red-400"
                }`}
              >
                {item.status}
              </td>

              <td className="text-center text-white">
                {item.threat_score}
              </td>

              <td className="text-center text-white">
                {item.virustotal_score}
              </td>

              <td className="text-center text-white">
                {item.alienvault_score}
              </td>

              <td className="text-center text-slate-300">
                {new Date(item.investigated_at).toLocaleString()}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}