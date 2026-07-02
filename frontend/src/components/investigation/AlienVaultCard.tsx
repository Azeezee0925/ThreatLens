import { Card } from "@/components/ui/card";

interface Props {
  result: any;
}

export default function AlienVaultCard({ result }: Props) {
  return (
    <Card className="bg-slate-900 border-slate-800 p-6 text-white">

      <h2 className="text-2xl font-bold mb-6">
        AlienVault OTX Intelligence
      </h2>

      <div className="grid grid-cols-2 gap-6">

        <div className="bg-slate-800 rounded-xl p-5">
          <p className="text-slate-400">
            Threat Score
          </p>

          <h1 className="text-4xl font-bold mt-3">
            {result.alienvault_score}
          </h1>
        </div>

        <div className="bg-slate-800 rounded-xl p-5">
          <p className="text-slate-400">
            Threat Pulses
          </p>

          <h1 className="text-4xl font-bold mt-3">
            {result.pulse_count}
          </h1>
        </div>

      </div>

    </Card>
  );
}