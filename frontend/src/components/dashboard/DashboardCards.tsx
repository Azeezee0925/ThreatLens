"use client";

import { Card } from "@/components/ui/card";
import { useEffect, useState } from "react";
import { getDashboardStats } from "@/services/dashboard";

interface DashboardStats {
  total_investigations: number;
  safe: number;
  suspicious: number;
  malicious: number;
  average_threat_score: number;
}

export default function DashboardCards() {

  const [stats, setStats] = useState<DashboardStats | null>(null);

  useEffect(() => {

    async function fetchData() {

      try {

        const data = await getDashboardStats();

        setStats(data);

      } catch (error) {

        console.error("Dashboard Error:", error);

      }

    }

    fetchData();

  }, []);

  if (!stats) {

    return <p>Loading dashboard...</p>;

  }

  const cards = [

    {
      title: "Investigations",
      value: stats.total_investigations,
    },

    {
      title: "Safe",
      value: stats.safe,
    },

    {
      title: "Suspicious",
      value: stats.suspicious,
    },

    {
      title: "Malicious",
      value: stats.malicious,
    },

  ];

  return (

    <div className="grid grid-cols-4 gap-6">

      {cards.map((card) => (

        <Card
          key={card.title}
          className="bg-slate-900 border-slate-800 p-6 text-white"
        >

          <p className="text-slate-300 text-lg">

            {card.title}

          </p>

          <h2 className="text-5xl font-bold mt-5 text-cyan-400">

            {card.value}

          </h2>

        </Card>

      ))}

    </div>

  );

}