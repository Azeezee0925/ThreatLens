"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { investigateIOC } from "@/services/investigation";
import InvestigationResult from "@/components/investigation/InvestigationResult";

export default function Searchbox() {
  const [ioc, setIoc] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);

  async function handleInvestigate() {
    if (!ioc.trim()) {
      alert("Please enter an IOC");
      return;
    }

    try {
      setLoading(true);

      const data = await investigateIOC(ioc);

      setResult(data);

    } catch (error) {
      console.error(error);
      alert("Investigation failed.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="space-y-6">

      <div className="flex gap-4">

        <Input
          placeholder="Enter IP, Domain, URL or Hash"
          value={ioc}
          onChange={(e) => setIoc(e.target.value)}
        />

        <Button
          onClick={handleInvestigate}
          disabled={loading}
        >
          {loading ? "Investigating..." : "Investigate"}
        </Button>

      </div>

      {result && (

<InvestigationResult
    result={result}
/>

)}

    </div>
  );
}