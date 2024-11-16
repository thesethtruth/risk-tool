<script lang="ts">
	import * as Avatar from '$lib/components/ui/avatar/index.js';
	import { HeaderSearch } from '$lib/components/ui/header-search/index.js';
	import * as Sidebar from '$lib/components/ui/sidebar/index.js';
	import { Ellipsis } from 'lucide-svelte';
</script>

<header
	class="sticky top-0 z-50 flex h-12 w-full items-center justify-between bg-white px-4 py-1 shadow-sm"
>
	<Sidebar.Trigger />
	<HeaderSearch placeholder="Zoeken of uitvoeren" class="w-full min-w-64 max-w-96" />
	<div class="flex items-center gap-3 pr-2">
		<Ellipsis />

		<Avatar.Root class="h-8 w-8">
			<Avatar.Image src="https://sethvanwieringen.dev/seth_comp.jpg" alt="@thesethtruth" />
			<Avatar.Fallback>Z</Avatar.Fallback>
		</Avatar.Root>
	</div>
</header>
