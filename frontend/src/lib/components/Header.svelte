<script lang="ts">
	import * as Avatar from '$lib/components/ui/avatar/index.js';
	import { HeaderSearch } from '$lib/components/ui/header-search/index.js';
</script>

<header class="flex items-center justify-between p-1">
	<div>logo</div>
	<HeaderSearch placeholder="Zoeken of uitvoeren" class="max-w-m min-w-s" />
	<div class="flex items-center gap-2 pr-3">
		<svg
			xmlns="http://www.w3.org/2000/svg"
			viewBox="0 0 24 24"
			fill="none"
			stroke="currentColor"
			stroke-width="2"
			stroke-linecap="round"
			stroke-linejoin="round"
			class="size-8 cursor-pointer"
		>
			<circle cx="5" cy="12" r="1"></circle>
			<circle cx="12" cy="12" r="1"></circle>
			<circle cx="19" cy="12" r="1"></circle>
		</svg>

		<Avatar.Root>
			<Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
			<Avatar.Fallback>CN</Avatar.Fallback>
		</Avatar.Root>
	</div>
</header>
