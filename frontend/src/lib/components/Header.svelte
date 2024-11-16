<script lang="ts">
	import * as Avatar from '$lib/components/ui/avatar/index.js';
	import { HeaderSearch } from '$lib/components/ui/header-search/index.js';
</script>

<header class="sticky top-0 z-50 flex items-center justify-between bg-white px-4 py-1 shadow-sm">
	<div class="flex flex-row items-center gap-3">
		<div class="flex h-7 w-7 items-center justify-center rounded-lg bg-slate-300">
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" class="h-5 w-5">
				<!-- Main R shape -->
				<path
					d="M20 80 V20 H60 C70 20 80 30 80 40 C80 50 70 60 60 60 L80 80 H65 L45 60 H35 V80 H20 Z
				   M35 45 H55 C60 45 65 43 65 40 C65 37 60 35 55 35 H35 V45 Z"
					fill="#fff"
				/>
			</svg>
		</div>
		Risk tool
	</div>
	<HeaderSearch placeholder="Zoeken of uitvoeren" class="w-96" />
	<div class="flex items-center gap-2">
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

		<Avatar.Root class="h-9 w-9">
			<Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
			<Avatar.Fallback>CN</Avatar.Fallback>
		</Avatar.Root>
	</div>
</header>
