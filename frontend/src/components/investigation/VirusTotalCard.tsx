import { Card } from "@/components/ui/card";

interface Props {
  result: any;
}

export default function VirusTotalCard({ result }: Props) {
  return (
    <Card className="bg-slate-900 border-slate-800 p-6 text-white">

      <h2 className="text-2xl font-bold mb-6">
        🦠 VirusTotal Intelligence
      </h2>

      <div className="grid grid-cols-2 md:grid-cols-3 gap-5">

        <div className="bg-slate-800 rounded-xl p-5">
          <p className="text-slate-400">Threat Score</p>
          <h1 className="text-3xl font-bold mt-2">
            {result.virustotal_score}/100
          </h1>
        </div>

        <div className="bg-slate-800 rounded-xl p-5">
          <p className="text-slate-400">Harmless</p>
          <h1 className="text-3xl font-bold text-green-400 mt-2">
            {result.harmless}
          </h1>
        </div>

        <div className="bg-slate-800 rounded-xl p-5">
          <p className="text-slate-400">Malicious</p>
          <h1 className="text-3xl font-bold text-red-400 mt-2">
            {result.malicious}
          </h1>
        </div>

        <div className="bg-slate-800 rounded-xl p-5">
          <p className="text-slate-400">Suspicious</p>
          <h1 className="text-3xl font-bold text-yellow-400 mt-2">
            {result.suspicious}
          </h1>
        </div>

        <div className="bg-slate-800 rounded-xl p-5">
          <p className="text-slate-400">Reputation</p>
          <h1 className="text-3xl font-bold mt-2">
            {result.reputation}
          </h1>
        </div>

        <div className="bg-slate-800 rounded-xl p-5">
          <p className="text-slate-400">Last Analysis</p>

          <p className="mt-3 text-sm leading-6">
            {result.last_analysis_date}
          </p>
        </div>

      </div>

    </Card>
  );
}