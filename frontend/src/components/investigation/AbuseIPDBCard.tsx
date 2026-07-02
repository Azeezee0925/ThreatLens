import { Card } from "@/components/ui/card";

interface Props {
  result: any;
}

export default function AbuseIPDBCard({ result }: Props) {

  // Only show for IPs
  if (result.ioc_type !== "ip") return null;

  return (
    <Card className="bg-slate-900 border-slate-800 p-6 text-white">

      <h2 className="text-2xl font-bold mb-6">
        🌐 AbuseIPDB Intelligence
      </h2>

      <div className="grid grid-cols-2 md:grid-cols-3 gap-5">

        <div className="bg-slate-800 rounded-xl p-5">
          <p className="text-slate-400">
            Abuse Score
          </p>

          <h1 className="text-3xl font-bold mt-2">
            {result.abuse_confidence_score}/100
          </h1>
        </div>

        <div className="bg-slate-800 rounded-xl p-5">
          <p className="text-slate-400">
            Total Reports
          </p>

          <h1 className="text-3xl font-bold mt-2">
            {result.total_reports}
          </h1>
        </div>

        <div className="bg-slate-800 rounded-xl p-5">
          <p className="text-slate-400">
            ASN
          </p>

          <h1 className="text-xl font-bold mt-2">
            {result.asn}
          </h1>
        </div>

        <div className="bg-slate-800 rounded-xl p-5">
          <p className="text-slate-400">
            Owner
          </p>

          <p className="mt-2">
            {result.owner}
          </p>
        </div>

        <div className="bg-slate-800 rounded-xl p-5">
          <p className="text-slate-400">
            ISP
          </p>

          <p className="mt-2">
            {result.isp}
          </p>
        </div>

        <div className="bg-slate-800 rounded-xl p-5">
          <p className="text-slate-400">
            Domain
          </p>

          <p className="mt-2">
            {result.domain}
          </p>
        </div>

        <div className="bg-slate-800 rounded-xl p-5">
          <p className="text-slate-400">
            Country Code
          </p>

          <h1 className="text-2xl font-bold mt-2">
            {result.country_code}
          </h1>
        </div>

      </div>

    </Card>
  );
}