import DashboardCards from "@/components/dashboard/DashboardCards";

export default function DashboardPage() {
  return (
    <div className="space-y-8">

      <div>
        <h1 className="text-4xl font-bold">
          Dashboard
        </h1>

        <p className="text-slate-400">
          Real-time Threat Intelligence Overview
        </p>
      </div>

      <DashboardCards />

    </div>
  );
}