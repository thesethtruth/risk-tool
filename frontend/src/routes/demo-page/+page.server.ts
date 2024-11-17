type RiskData = {
    id: string;
    name: string;
    description: string;
    cause: string;
    consequence: string;
    status: string;
    score: number;
    mitigation: string;
    responsible?: string;
};

const data: RiskData[] = [
    {
        id: "RISK-001",
        name: "VVE Goedkeuring",
        description: "Risico dat VVE niet akkoord gaat met voorgestelde wijzigingen",
        cause: "Meerderheid van VVE leden moet instemmen met wijziging splitsingsakte",
        consequence: "Plan moet worden bijgesteld of project wordt gestopt",
        status: "Actief",
        score: 13,
        mitigation: "VVE tijdig informeren en positief belang creëren voor VVE leden"
    },
    {
        id: "RISK-002",
        name: "Huurcontract Risico",
        description: "Huurders willen geen langlopend huurcontract",
        cause: "Gemeentelijke verhuur beperkingen en voorkeur voor korte contracten",
        consequence: "Leegstand en gederfde huurinkomsten",
        status: "Actief",
        score: 13,
        mitigation: "Risicoreservering bij gemeente"
    },
    {
        id: "RISK-003",
        name: "Raad Krediet Goedkeuring",
        description: "Raad stemt niet in met verstrekken krediet voor aankoop en verbouwing",
        cause: "Te weinig draagvlak in nieuwe raad/maatschappij",
        consequence: "Project wordt gestopt",
        status: "Actief",
        score: 11,
        mitigation: "Stakeholder betrokkenheid en gedetailleerde financiële planning"
    },
    {
        id: "RISK-004",
        name: "Aanbesteding Mislukking",
        description: "Risico op mislukte aanbesteding",
        cause: "Krapte op de markt en hoge prijzen",
        consequence: "Project vertraging of budget overschrijding",
        status: "Actief",
        score: 11,
        mitigation: "Monitoring van kosten en evenwichtige risicoverdeling"
    },
    {
        id: "RISK-005",
        name: "BTW Impact",
        description: "Meer meters verhuurd aan niet-BTW huurders",
        cause: "Gewijzigde inzichten/bedrijfsvoering niet-BTW huurders",
        consequence: "Verminderde BTW aftrek over investering en exploitatie",
        status: "Actief",
        score: 9,
        mitigation: "Financiële herberekening bij wijzigingen in huurdermix"
    },
    {
        id: "RISK-006",
        name: "Muziekschool Kosten",
        description: "Hogere huisvestingskosten muziekschool",
        cause: "Verhoogde kosten in MFC voor huur en beheer",
        consequence: "Extra gemeentelijke bijdragen noodzakelijk",
        status: "Actief",
        score: 9,
        mitigation: "Kostenoptimalisatie en aanpassing serviceniveau"
    },
    {
        id: "RISK-007",
        name: "VBK Ultimatum",
        description: "Druk door aankoopdeadline",
        cause: "VBK bv heeft ultimatum gesteld voor aankoopbesluit",
        consequence: "Overhaaste beslissing of hogere aankoopkosten",
        status: "Actief",
        score: 9,
        mitigation: "Versneld besluitvormingsproces"
    },
    {
        id: "RISK-008",
        name: "Bibliotheek Frictiekosten",
        description: "Raad niet akkoord met frictiekosten bibliotheek",
        cause: "Bibliotheek vraagt vergoeding van frictiekosten",
        consequence: "Mogelijk stoppen van project",
        status: "Actief",
        score: 8,
        mitigation: "Onderhandeling met bibliotheek stakeholders"
    },
    {
        id: "RISK-009",
        name: "Vergunning Bezwaren",
        description: "Risico op bezwaar bij vergunningaanvraag",
        cause: "Benodigde omgevingsvergunning en zorgen van belanghebbenden",
        consequence: "Vertraging planvorming of aanpassing ontwerp",
        status: "Actief",
        score: 8,
        mitigation: "Proactief stakeholder management"
    }
];

export async function load() {
    const names = [
        'John',
        'Jane',
        'Doe',
        'Smith',
        'Johnson',
        'Williams',
        'Brown',
        'Jones',
        'Miller',
        'Davis'
    ];

    data.forEach((entry) => {
        // Just assign the name, the AvatarCell component will handle the rendering
        entry.responsible = names[Math.floor(Math.random() * names.length)];
    });

    return {
        data,
    };
}
