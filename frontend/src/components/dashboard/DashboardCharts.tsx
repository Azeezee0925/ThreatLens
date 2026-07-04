"use client";

import { useEffect, useState } from "react";
import { getCharts } from "@/services/charts";

import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
  BarChart,
  XAxis,
  YAxis,
  CartesianGrid,
  Legend,
  Bar,
  LineChart,
  Line,
} from "recharts";

const COLORS = [
  "#22c55e",
  "#facc15",
  "#ef4444",
];

export default function DashboardCharts() {

  const [data, setData] = useState<any>(null);

  useEffect(() => {

    async function loadCharts() {

      const response = await getCharts();

      setData(response);

    }

    loadCharts();

  }, []);

  if (!data)
    return null;

  const threatData = [

    {
      name: "Safe",
      value: data.threat_distribution.safe,
    },

    {
      name: "Suspicious",
      value: data.threat_distribution.suspicious,
    },

    {
      name: "Malicious",
      value: data.threat_distribution.malicious,
    },

  ];

  return (

    <div className="grid md:grid-cols-2 gap-6 mt-10">

      {/* Threat Distribution */}

      <div className="bg-slate-900 rounded-xl p-6">

        <h2 className="text-xl font-semibold mb-5">
          Threat Distribution
        </h2>

        <ResponsiveContainer
          width="100%"
          height={300}
        >

          <PieChart>

            <Pie
              data={threatData}
              dataKey="value"
              outerRadius={100}
              label
            >

              {threatData.map((entry, index) => (

                <Cell
                  key={index}
                  fill={COLORS[index]}
                />

              ))}

            </Pie>

            <Tooltip />

          </PieChart>

        </ResponsiveContainer>

      </div>

      {/* IOC Distribution */}

      <div className="bg-slate-900 rounded-xl p-6">

        <h2 className="text-xl font-semibold mb-5">
          IOC Types
        </h2>

        <ResponsiveContainer
          width="100%"
          height={300}
        >

          <BarChart
            data={data.ioc_distribution}
          >

            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="type" />

            <YAxis />

            <Tooltip />

            <Legend />

            <Bar
              dataKey="count"
              fill="#3b82f6"
            />

          </BarChart>

        </ResponsiveContainer>

      </div>

      {/* Investigation Trend */}

   <div className="bg-slate-900 rounded-xl p-6 mt-6">

  <h2 className="text-xl font-semibold mb-5">
    Investigation Trend (Last 7 Days)
  </h2>

  <ResponsiveContainer
    width="100%"
    height={320}
  >

    <LineChart
      data={data.weekly_trend}
    >

      <CartesianGrid strokeDasharray="3 3" />

      <XAxis dataKey="day" />

      <YAxis />

      <Tooltip />

      <Legend />

      <Line
        type="monotone"
        dataKey="count"
        stroke="#3b82f6"
        strokeWidth={3}
      />

    </LineChart>

  </ResponsiveContainer>

</div>

    </div>

  );

}