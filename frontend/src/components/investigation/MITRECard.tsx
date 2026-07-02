import { Card } from "@/components/ui/card";

interface Props {
  result: any;
}

export default function MITRECard({ result }: Props) {
  return (
    <Card className="bg-slate-900 border-slate-800 p-6 text-white">

      <h2 className="text-2xl font-bold mb-6">
        🎯 MITRE ATT&CK Mapping
      </h2>

      {!result.mitre_tactics ? (

        <p className="text-slate-400">
          No MITRE ATT&CK techniques identified.
        </p>

      ) : (

        <div className="space-y-6">

          <div>

            <h3 className="text-slate-400 mb-2">
              Tactics
            </h3>

            <p>
              {result.mitre_tactics}
            </p>

          </div>

          <div>

            <h3 className="text-slate-400 mb-2">
              Techniques
            </h3>

            <div className="space-y-2">

              {result.mitre_techniques?.map((technique: any) => (

                <div
                  key={technique.id}
                  className="bg-slate-800 rounded-lg p-4"
                >
                  <p className="font-bold">
                    {technique.id}
                  </p>

                  <p className="text-slate-300">
                    {technique.name}
                  </p>

                </div>

              ))}

            </div>

          </div>

        </div>

      )}

    </Card>
  );
}