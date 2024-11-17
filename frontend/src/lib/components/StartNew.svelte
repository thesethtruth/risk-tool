<script lang="ts">
	import { FileText, FolderPlus } from 'lucide-svelte';
</script>

<div class="mb-6 mt-12 flex flex-row items-center justify-center gap-4">
	<button
		class="bg-primary-foreground flex min-h-32 w-full min-w-52 max-w-96 flex-col items-center justify-end rounded-xl border-2 border-dashed"
	>
		<div class="flex flex-col items-center justify-center pb-4">
			<FolderPlus strokeWidth={1} class="text-muted-foreground h-10 w-10" />
			<h2 class="text-muted-foreground text-xl font-normal">Nieuw project</h2>
		</div>
	</button>
	<button
		class="bg-primary-foreground flex min-h-32 w-full min-w-52 max-w-96 flex-col items-center justify-end rounded-xl border-2 border-dashed"
	>
		<div class="flex flex-col items-center justify-center pb-4">
			<FileText strokeWidth={1} class="text-muted-foreground h-10 w-10" />
			<h2 class="text-muted-foreground text-xl font-normal">Nieuw risicodossier</h2>
		</div>
	</button>
</div>
