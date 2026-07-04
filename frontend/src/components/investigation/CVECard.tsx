import { Card } from "@/components/ui/card";

interface Props {
  result: any;
}

export default function CVECard({ result }: Props) {
  return (
    <Card className="bg-slate-900 border-slate-800 p-6 text-white">

      <h2 className="text-2xl font-bold mb-6">
        🛡️ CVE Correlation
      </h2>

      {result.cve_found ? (

        <div className="space-y-6">

          <div className="grid grid-cols-2 gap-5">

            <div className="bg-slate-800 rounded-xl p-5">
              <p className="text-slate-400">
                CVEs Found
              </p>

              <h1 className="text-3xl font-bold mt-2 text-red-400">
                {result.cve_count}
              </h1>
            </div>

            <div className="bg-slate-800 rounded-xl p-5">
              <p className="text-slate-400">
                Status
              </p>

              <h1 className="text-3xl font-bold mt-2 text-red-400">
                YES
              </h1>
            </div>

          </div>

          <div>

            <h3 className="text-slate-400 mb-3">
              Related CVEs
            </h3>

            <div className="space-y-3">

              {result.related_cves?.map((cve: string) => (

                <div
                  key={cve}
                  className="bg-slate-800 rounded-lg p-4"
                >
                  {cve}
                </div>

              ))}

            </div>

          </div>

        </div>

      ) : (

        <div className="bg-slate-800 rounded-xl p-6">

          <h3 className="text-green-400 text-xl font-bold">
            ✅ No Known CVEs
          </h3>

          <p className="text-slate-300 mt-3">
            No known Common Vulnerabilities and Exposures (CVEs)
            were associated with this IOC.
          </p>

        </div>

      )}

    </Card>
  );
}