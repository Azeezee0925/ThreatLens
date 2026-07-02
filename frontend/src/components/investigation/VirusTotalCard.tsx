import { Card } from "@/components/ui/card";

interface Props {
  result: any;
}

export default function VirusTotalCard({ result }: Props) {

  return (

    <Card className="bg-slate-900 border-slate-800 p-6 text-white">

      <h2 className="text-2xl font-bold mb-6">

        VirusTotal Analysis

      </h2>

      <div className="grid grid-cols-3 gap-6">

        <div className="rounded-lg bg-green-950 p-5">

          <p className="text-green-300 text-sm">

            Harmless

          </p>

          <h2 className="text-4xl font-bold mt-2">

            {result.harmless}

          </h2>

        </div>

        <div className="rounded-lg bg-red-950 p-5">

          <p className="text-red-300 text-sm">

            Malicious

          </p>

          <h2 className="text-4xl font-bold mt-2">

            {result.malicious}

          </h2>

        </div>

        <div className="rounded-lg bg-yellow-950 p-5">

          <p className="text-yellow-300 text-sm">

            Suspicious

          </p>

          <h2 className="text-4xl font-bold mt-2">

            {result.suspicious}

          </h2>

        </div>

      </div>

    </Card>

  );

}