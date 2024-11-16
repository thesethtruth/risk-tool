<script lang="ts">
	import * as Avatar from '$lib/components/ui/avatar/index.js';
	import { Separator } from '$lib/components/ui/separator/index.js';
	import * as Table from '$lib/components/ui/table/index.js';

	import { Badge } from '$lib/components/ui/badge/index.js';
	import { FileText, FolderPlus } from 'lucide-svelte';
</script>

<div
	class="hidden translate-x-[10px] gap-[-20px] pb-4 hover:brightness-100 hover:contrast-100 hover:saturate-100 hover:filter-none"
>
	asdfasdfasdfas
</div>

<div class="container mx-auto p-4">
	<h1 class="mb-4 text-2xl font-bold">Welkom, Seth</h1>
	<p>Blader door de zijbalk, open een recent project voortzetten of een nieuw project maken!</p>

	<div class="grid h-3/4 grid-cols-1 grid-rows-[1fr_auto_1fr] gap-4 pt-12">
		<div class="flex flex-row items-center justify-center gap-4 py-12">
			<button
				class="bg-primary-foreground flex min-h-32 w-full min-w-52 max-w-96 flex-col items-center justify-end rounded-xl border-2 border-dashed"
			>
				<div class="flex flex-col items-center justify-center pb-4">
					<FolderPlus class="text-muted-foreground h-10 w-10" />
					<h2 class="text-muted-foreground text-xl font-semibold">Nieuw project</h2>
				</div>
			</button>
			<button
				class="bg-primary-foreground flex min-h-32 w-full min-w-52 max-w-96 flex-col items-center justify-end rounded-xl border-2 border-dashed"
			>
				<div class="flex flex-col items-center justify-center pb-4">
					<FileText class="text-muted-foreground h-10 w-10" />
					<h2 class="text-muted-foreground text-xl font-semibold">Nieuw risicodossier</h2>
				</div>
			</button>
		</div>
		<Separator />
		<div>
			<h2 class="text-muted-foreground mb-2 text-lg font-semibold tracking-tight">
				Recente risico dossiers
			</h2>
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
					<Table.Row>
						<Table.Cell class="font-medium">1370565</Table.Cell>
						<Table.Cell>Dijkverbreding daarginteren</Table.Cell>
						<Table.Cell>Concept</Table.Cell>
						<Table.Cell>
							<Badge>24-12-2024</Badge></Table.Cell
						>
						<Table.Cell class="italic">16-11-2024 om 17:05</Table.Cell>
						<Table.Cell>
							<Avatar.Root class="h-8 w-8">
								<Avatar.Image
									src="https://api.dicebear.com/9.x/personas/svg?seed=John?&backgroundColor=b6e3f4"
									alt="avatar"
								/>
								<Avatar.Fallback>Z</Avatar.Fallback>
							</Avatar.Root>
						</Table.Cell>
					</Table.Row>
					<Table.Row>
						<Table.Cell class="font-medium">1370565</Table.Cell>
						<Table.Cell>Dijkverbreding daarginteren</Table.Cell>
						<Table.Cell>Concept</Table.Cell>
						<Table.Cell><Badge>24-12-2024</Badge></Table.Cell>
						<Table.Cell class="italic">24-12-2024 om 17:05</Table.Cell>
						<Table.Cell>
							<Avatar.Root class="h-8 w-8">
								<Avatar.Image
									src="https://api.dicebear.com/9.x/personas/svg?seed=James&backgroundColor=b6e3f4"
									alt="avatar"
								/>
								<Avatar.Fallback>Z</Avatar.Fallback>
							</Avatar.Root>
						</Table.Cell>
					</Table.Row>
				</Table.Body>
			</Table.Root>
		</div>
	</div>
</div>
