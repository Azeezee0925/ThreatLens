import { Card } from "@/components/ui/card";

interface Props {
  result: any;
}

export default function RecommendationCard({ result }: Props) {
  return (
    <Card className="bg-slate-900 border-slate-800 p-6 text-white">

      <h2 className="text-2xl font-bold mb-6">
        💡 AI Recommendation
      </h2>

      <div className="bg-slate-800 rounded-xl p-6">

        <p className="leading-7">
          {result.ai_recommendation}
        </p>

      </div>

    </Card>
  );
}