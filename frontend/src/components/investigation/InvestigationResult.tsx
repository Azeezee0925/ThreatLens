import SummaryCard from "./SummaryCard";
import VirusTotalCard from "./VirusTotalCard";
import ExecutiveSummaryCard from "./ExecutiveSummaryCard";
import AlienVaultCard from "./AlienVaultCard";
import MITRECard from "./MITRECard";
import OWASPCard from "./OWASPCard";
import RecommendationCard from "./RecommendationCard";
import AbuseIPDBCard from "./AbuseIPDBCard";

interface Props {
  result: any;
}

export default function InvestigationResult({ result }: Props) {

  return (

    <div className="space-y-6">

      <SummaryCard result={result} />

      <VirusTotalCard result={result} />

      <AbuseIPDBCard result={result} />

      <AlienVaultCard result={result} />

      <ExecutiveSummaryCard result={result} />

      <MITRECard result={result} />

      <OWASPCard result={result} />

      <RecommendationCard result={result} />

    </div>

  );

}