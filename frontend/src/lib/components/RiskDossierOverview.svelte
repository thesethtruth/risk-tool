<script lang="ts">
	import * as Avatar from '$lib/components/ui/avatar/index.js';
	import { Badge } from '$lib/components/ui/badge/index.js';
	import { ScrollArea } from '$lib/components/ui/scroll-area/index.js';
	import * as Table from '$lib/components/ui/table/index.js';
	import { cn } from '$lib/utils.js';

	interface RiskDossier {
		projectCode: string;
		projectDescription: string;
		status: string;
		deadline: string;
		lastEdit: string;
		avatar: string;
	}
	const riskDossiers: RiskDossier[] = [
		{
			projectCode: '1370565',
			projectDescription: 'Dijkverbreding daarginteren',
			status: 'Concept',
			deadline: '24-12-2024',
			lastEdit: '16-11-2024 om 17:05',
			avatar: 'https://api.dicebear.com/9.x/personas/svg?seed=Felix&backgroundColor=b6e3f4'
		},
		{
			projectCode: '1482390',
			projectDescription: 'Waterkering renovatie fase 2',
			status: 'In Progress',
			deadline: '15-03-2025',
			lastEdit: '15-11-2024 om 09:30',
			avatar: 'https://api.dicebear.com/9.x/personas/svg?seed=Sophie&backgroundColor=b6e3f4'
		},
		{
			projectCode: '1256789',
			projectDescription: 'Sluiscomplex onderhoud',
			status: 'Review',
			deadline: '01-02-2025',
			lastEdit: '14-11-2024 om 14:15',
			avatar: 'https://api.dicebear.com/9.x/personas/svg?seed=Marcus&backgroundColor=b6e3f4'
		},
		{
			projectCode: '1398754',
			projectDescription: 'Polderbemaling upgrade',
			status: 'Concept',
			deadline: '30-01-2025',
			lastEdit: '16-11-2024 om 11:45',
			avatar: 'https://api.dicebear.com/9.x/personas/svg?seed=Luna&backgroundColor=b6e3f4'
		},
		{
			projectCode: '1445632',
			projectDescription: 'Kustbescherming analyse',
			status: 'Final',
			deadline: '10-04-2025',
			lastEdit: '13-11-2024 om 16:20',
			avatar: 'https://api.dicebear.com/9.x/personas/svg?seed=Noah&backgroundColor=b6e3f4'
		},
		{
			projectCode: '1567890',
			projectDescription: 'Gemaal automatisering',
			status: 'In Progress',
			deadline: '28-02-2025',
			lastEdit: '15-11-2024 om 13:40',
			avatar: 'https://api.dicebear.com/9.x/personas/svg?seed=Emma&backgroundColor=b6e3f4'
		},
		{
			projectCode: '1234567',
			projectDescription: 'Waterberging uitbreiding',
			status: 'Review',
			deadline: '20-03-2025',
			lastEdit: '14-11-2024 om 10:25',
			avatar: 'https://api.dicebear.com/9.x/personas/svg?seed=Oliver&backgroundColor=b6e3f4'
		},
		{
			projectCode: '1678901',
			projectDescription: 'Dijkmonitoring systeem',
			status: 'Final',
			deadline: '05-01-2025',
			lastEdit: '16-11-2024 om 15:50',
			avatar: 'https://api.dicebear.com/9.x/personas/svg?seed=Aria&backgroundColor=b6e3f4'
		},
		{
			projectCode: '1789012',
			projectDescription: 'Rioolwaterzuivering optimalisatie',
			status: 'Concept',
			deadline: '12-05-2025',
			lastEdit: '15-11-2024 om 08:15',
			avatar: 'https://api.dicebear.com/9.x/personas/svg?seed=Lucas&backgroundColor=b6e3f4'
		},
		{
			projectCode: '1890123',
			projectDescription: 'Stormvloedkering inspectie',
			status: 'In Progress',
			deadline: '18-04-2025',
			lastEdit: '14-11-2024 om 16:35',
			avatar: 'https://api.dicebear.com/9.x/personas/svg?seed=Isabella&backgroundColor=b6e3f4'
		},
		{
			projectCode: '1901234',
			projectDescription: 'Natuurvriendelijke oevers',
			status: 'Review',
			deadline: '25-03-2025',
			lastEdit: '16-11-2024 om 09:20',
			avatar: 'https://api.dicebear.com/9.x/personas/svg?seed=Ethan&backgroundColor=b6e3f4'
		},
		{
			projectCode: '2012345',
			projectDescription: 'Klimaatadaptatie studie',
			status: 'Final',
			deadline: '08-02-2025',
			lastEdit: '15-11-2024 om 14:45',
			avatar: 'https://api.dicebear.com/9.x/personas/svg?seed=Mila&backgroundColor=b6e3f4'
		},
		{
			projectCode: '2123456',
			projectDescription: 'Zoetwatervoorziening plan',
			status: 'Concept',
			deadline: '15-06-2025',
			lastEdit: '14-11-2024 om 11:30',
			avatar: 'https://api.dicebear.com/9.x/personas/svg?seed=Liam&backgroundColor=b6e3f4'
		},
		{
			projectCode: '2234567',
			projectDescription: 'Waterkwaliteit monitoring',
			status: 'In Progress',
			deadline: '22-05-2025',
			lastEdit: '16-11-2024 om 10:55',
			avatar: 'https://api.dicebear.com/9.x/personas/svg?seed=Zoe&backgroundColor=b6e3f4'
		},
		{
			projectCode: '2345678',
			projectDescription: 'Hoogwaterbescherming analyse',
			status: 'Review',
			deadline: '30-04-2025',
			lastEdit: '15-11-2024 om 15:10',
			avatar: 'https://api.dicebear.com/9.x/personas/svg?seed=Atlas&backgroundColor=b6e3f4'
		}
	];

	interface RiskDossierTableProps {
		scrollClass?: string;
		children?: any;
		title?: string;
		entries?: RiskDossier[];
		mockEntriesLength?: number;
	}

	let {
		scrollClass,
		title,
		entries,
		mockEntriesLength,
		children,
		...restProps
	}: RiskDossierTableProps = $props();
</script>

<div class="pt-4">
	{#if title}
		<h2 class="text-muted-foreground mb-2 text-xl font-semibold tracking-tight">
			{title}
		</h2>
	{/if}
	<ScrollArea class={cn('h-60 rounded-md border', scrollClass)}>
		<Table.Root>
			<Table.Header>
				<Table.Row>
					<Table.Head class="w-[100px]">Projectcode</Table.Head>
					<Table.Head>Projectbeschrijving</Table.Head>
					<Table.Head>Status</Table.Head>
					<Table.Head>Deadline</Table.Head>
					<Table.Head>Laatste aanpassing</Table.Head>
					<Table.Head class="w-[100px]" id="avatar"></Table.Head>
				</Table.Row>
			</Table.Header>
			<Table.Body>
				{#each mockEntriesLength ? riskDossiers.slice(0, mockEntriesLength) : riskDossiers as { projectCode, projectDescription, status, deadline, lastEdit, avatar }, index}
					<Table.Row id={String(index)}>
						<Table.Cell>{projectCode}</Table.Cell>
						<Table.Cell>{projectDescription}</Table.Cell>
						<Table.Cell>
							<Badge variant="outline" class="h-6">{status}</Badge>
						</Table.Cell>
						<Table.Cell>{deadline}</Table.Cell>
						<Table.Cell>{lastEdit}</Table.Cell>
						<Table.Cell>
							<Avatar.Root>
								<Avatar.Image src={avatar} alt="avatar" />
								<Avatar.Fallback>Z</Avatar.Fallback>
							</Avatar.Root>
						</Table.Cell>
					</Table.Row>
				{/each}
			</Table.Body>
		</Table.Root>
	</ScrollArea>
</div>
