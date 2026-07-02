import SummaryCard from "./SummaryCard";
import VirusTotalCard from "./VirusTotalCard";

interface Props {
  result: any;
}

export default function InvestigationResult({ result }: Props) {

  return (

    <div className="space-y-6">

      <SummaryCard result={result} />

      <VirusTotalCard result={result} />

    </div>

  );

}