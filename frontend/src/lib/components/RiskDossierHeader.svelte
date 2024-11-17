<script lang="ts">
	import * as Avatar from '$lib/components/ui/avatar/index.js';
	import { Badge } from '$lib/components/ui/badge/index.js';
	import { Settings } from 'lucide-svelte';
	const names = ['Jane', 'Jane', 'Jack', 'Josphine', 'Jill'];
</script>

<div class="flex w-full justify-between">
	<div class="flex flex-col items-start justify-center">
		<h1 class="mb-3 text-2xl font-semibold tracking-tight">137098</h1>
		<p class="text-md text-gray-500">Dijkverbreding daarginteren</p>
	</div>
	<div class="flex flex-col items-end justify-between">
		<div class="flex flex-row items-center justify-between gap-4">
			<Badge variant="outline" class="h-6">concept</Badge>
			<Settings class="hover:text-primary hover:cursor-pointer" />
		</div>
		<!-- overlapping avatars -->
		<div class="mt-2 flex flex-row items-center justify-between">
			{#each Array(names.length) as _, index}
				<Avatar.Root
					class="-ml-2 h-6 w-6 brightness-150 contrast-50 saturate-0 transition-all first:ml-0 hover:ml-0 hover:brightness-100 hover:contrast-100 hover:saturate-100"
				>
					<Avatar.Image
						src="https://api.dicebear.com/9.x/personas/svg?seed={names[
							index
						]}?&backgroundColor=c4e2f2"
						alt="@thesethtruth"
						class=""
					/>
					<Avatar.Fallback>Z</Avatar.Fallback>
				</Avatar.Root>
			{/each}
		</div>
	</div>
</div>
