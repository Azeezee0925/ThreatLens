import SummaryCard from "./SummaryCard";
import VirusTotalCard from "./VirusTotalCard";
import ExecutiveSummaryCard from "./ExecutiveSummaryCard";
import AlienVaultCard from "./AlienVaultCard";
import MITRECard from "./MITRECard";
import OWASPCard from "./OWASPCard";
import RecommendationCard from "./RecommendationCard";
import AbuseIPDBCard from "./AbuseIPDBCard";
import CVECard from "./CVECard";
import { downloadReport } from "@/services/report";


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

      <CVECard result={result} />

      <RecommendationCard result={result} />

      <div className="mt-8 flex justify-end">

    <button

        onClick={() => downloadReport(result.ioc)}

        className="bg-blue-600 hover:bg-blue-700 px-5 py-3 rounded-lg font-semibold"

    >

        📄 Generate PDF Report

    </button>

</div>

    </div>

  );

}