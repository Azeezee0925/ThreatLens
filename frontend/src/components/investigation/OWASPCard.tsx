import { Card } from "@/components/ui/card";

interface Props {
  result: any;
}

export default function OWASPCard({ result }: Props) {
  return (
    <Card className="bg-slate-900 border-slate-800 p-6 text-white">

      <h2 className="text-2xl font-bold mb-6">
        🛡️ OWASP Mapping
      </h2>

      {!result.owasp_category ? (

        <p className="text-slate-400">
          No OWASP category identified.
        </p>

      ) : (

        <div className="space-y-6">

          <div>

            <h3 className="text-slate-400 mb-2">
              Category
            </h3>

            <p>
              {result.owasp_category}
            </p>

          </div>

          <div>

            <h3 className="text-slate-400 mb-2">
              Description
            </h3>

            <p>
              {result.owasp_description}
            </p>

          </div>

        </div>

      )}

    </Card>
  );
}