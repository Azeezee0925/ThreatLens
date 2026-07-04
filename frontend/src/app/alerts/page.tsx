"use client";

import { useEffect, useState } from "react";

import { getAlerts } from "@/services/alerts";

export default function AlertsPage() {

    const [alerts, setAlerts] = useState<any[]>([]);

    useEffect(() => {

        async function loadAlerts() {

            const data = await getAlerts();

            setAlerts(data);

        }

        loadAlerts();

    }, []);

    return (

        <div className="space-y-6">

            <div>

                <h1 className="text-4xl font-bold">
                    Alerts
                </h1>

                <p className="text-slate-400">
                    Real-Time Threat Alerts
                </p>

            </div>

            <div className="space-y-4">

                {alerts.map((alert) => (

                    <div

                        key={alert.id}

                        className="bg-slate-900 rounded-xl p-5 border border-slate-700"

                    >

                        <div className="flex justify-between items-center">

                            <div>

                                <h2 className="font-semibold text-lg">

                                    {alert.ioc}

                                </h2>

                                <p className="text-slate-400">

                                    {alert.ioc_type.toUpperCase()}

                                </p>

                            </div>

                            <div className="text-right">

                                <p className="text-red-400 font-bold">

                                    {alert.status}

                                </p>

                                <p>

                                    Threat Score: {alert.threat_score}
                                </p>

                            </div>

                        </div>

                        <p className="text-sm text-slate-500 mt-3">

                            {new Date(alert.created_at).toLocaleString()}

                        </p>

                    </div>

                ))}

            </div>

        </div>

    );

}