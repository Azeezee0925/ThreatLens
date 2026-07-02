import { Card } from "@/components/ui/card";

interface Props {
  result: any;
}

export default function SummaryCard({ result }: Props) {
  return (
    <Card className="bg-slate-900 border-slate-800 p-6 text-white">

      <h2 className="text-3xl font-bold">
        {result.ioc}
      </h2>

      <p className="text-slate-400 mt-2">
        {result.ioc_type.toUpperCase()}
      </p>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-6 mt-8">

        <div>
          <p className="text-slate-400 text-sm">Status</p>
          <h3 className="text-2xl font-bold text-green-400">
            {result.status}
          </h3>
        </div>

        <div>
          <p className="text-slate-400 text-sm">Threat Score</p>
          <h3 className="text-2xl font-bold">
            {result.threatlens_score}/100
          </h3>
        </div>

        <div>
          <p className="text-slate-400 text-sm">Confidence</p>
          <h3 className="text-2xl font-bold">
            {result.confidence}%
          </h3>
        </div>

        <div>
          <p className="text-slate-400 text-sm">Owner</p>
          <h3 className="text-lg font-semibold">
            {result.owner ?? "-"}
          </h3>
        </div>

      </div>

    </Card>
  );
}