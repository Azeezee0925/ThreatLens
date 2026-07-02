import { Card } from "@/components/ui/card";

interface Props {
  result: any;
}

export default function ExecutiveSummaryCard({ result }: Props) {
  return (
    <Card className="bg-slate-900 border-slate-800 p-6 text-white">

      <h2 className="text-2xl font-bold mb-6">
        AI Executive Summary
      </h2>

      <div className="space-y-6">

        <div>
          <h3 className="text-slate-400 mb-2">
            Executive Summary
          </h3>

          <p>
            {result.executive_summary}
          </p>
        </div>

        <div>
          <h3 className="text-slate-400 mb-2">
            Risk Assessment
          </h3>

          <p>
            {result.risk_assessment}
          </p>
        </div>

        <div>
          <h3 className="text-slate-400 mb-2">
            Key Findings
          </h3>

          <ul className="list-disc pl-6 space-y-2">
            {result.key_findings?.map((item: string, index: number) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>

      </div>

    </Card>
  );
}