<script lang="ts">
	import * as Command from '$lib/components/ui/command/index.js';
	import { cn } from '$lib/utils.js';
	import type { WithElementRef } from 'bits-ui';
	import type { HTMLInputAttributes } from 'svelte/elements';

	interface SearchProps extends HTMLInputAttributes {
		open?: boolean;
		classParent?: string;
	}

	let {
		ref = $bindable(null),
		value = $bindable(),
		open: open,
		class: className,
		classParent: classParent,
		...restProps
	}: WithElementRef<SearchProps> = $props();
</script>

<div class={cn('relative', classParent)}>
	<svg
		xmlns="http://www.w3.org/2000/svg"
		width="24"
		height="24"
		viewBox="0 0 24 24"
		fill="none"
		stroke="currentColor"
		stroke-width="2"
		stroke-linecap="round"
		stroke-linejoin="round"
		class="text-muted-foreground absolute left-2 top-1/2 h-4 w-4 -translate-y-1/2 transform"
		><circle cx="11" cy="11" r="6"></circle><path d="m21 21-4.3-4.3"></path></svg
	>

	<input
		bind:this={ref}
		class={cn(
			'border-input bg-background ring-offset-background placeholder:text-muted-foreground focus-visible:ring-ring flex h-8 w-full rounded-md border py-2 pl-8 pr-3 text-sm file:border-0 file:bg-transparent file:text-sm file:font-medium focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50',
			className
		)}
		bind:value
		{...restProps}
	/>
</div>
