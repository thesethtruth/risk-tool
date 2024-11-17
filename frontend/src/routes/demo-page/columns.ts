import AvatarCell from "$lib/components/ui/avatar-cell.svelte";
import { renderComponent } from "$lib/components/ui/data-table/render-helpers";
import type { ColumnDef } from "@tanstack/table-core";

export type RiskEntry = {
    id: string;
    name: string;
    description?: string;
    cause?: string;
    consequence?: string;
    responsible?: string;
    status?: string;
    score?: number;
    mitigation?: string;
};

export const columns: ColumnDef<RiskEntry>[] = [
    {
        accessorKey: "responsible",
        header: "",
        cell: ({ row }) => renderComponent(AvatarCell, {
            name: row.getValue("responsible") as string
        })
    },
    {
        accessorKey: "score",
        header: "Score",
    },
    {
        accessorKey: "name",
        header: "Naam",
    },
    {
        accessorKey: "status",
        header: "Status",
    },
    {
        accessorKey: "description",
        header: "Beschrijving",
    },
    {
        accessorKey: "cause",
        header: "Oorzaak",
    },
    {
        accessorKey: "consequence",
        header: "Gevolg",
    },
    {
        accessorKey: "mitigation",
        header: "Mitigatie",
    },
];
