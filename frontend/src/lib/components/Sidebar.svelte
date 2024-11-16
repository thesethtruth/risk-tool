<script lang="ts">
	import { page } from '$app/stores';

	interface NavItem {
		title: string;
		href: string;
		icon?: string;
	}

	const navigation: NavItem[] = [
		{ title: 'Dashboard', href: '/' },
		{ title: 'Projects', href: '/projects' },
		{ title: 'Tasks', href: '/tasks' },
		{ title: 'Reports', href: '/reports' },
		{ title: 'Settings', href: '/settings' }
	];

	let isCollapsed = false;

	function toggleSidebar() {
		isCollapsed = !isCollapsed;
	}

	$: currentPath = $page.url.pathname;
</script>

<aside
	class="bg-background h-full border-r transition-all duration-300 {isCollapsed
		? 'w-[60px]'
		: 'w-full'}"
>
	<div class="flex h-full flex-col gap-4 p-4">
		<button
			class="absolute -right-3 top-4 z-10 rounded-full bg-white p-1.5 shadow-lg hover:bg-gray-100"
			on:click={toggleSidebar}
		>
			{#if isCollapsed}
				<svg
					xmlns="http://www.w3.org/2000/svg"
					width="16"
					height="16"
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					stroke-width="2"
					stroke-linecap="round"
					stroke-linejoin="round"
				>
					<path d="m9 18 6-6-6-6" />
				</svg>
			{:else}
				<svg
					xmlns="http://www.w3.org/2000/svg"
					width="16"
					height="16"
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					stroke-width="2"
					stroke-linecap="round"
					stroke-linejoin="round"
				>
					<path d="m15 18-6-6 6-6" />
				</svg>
			{/if}
		</button>

		<nav class="space-y-2">
			{#each navigation as item}
				<a
					href={item.href}
					class="flex items-center gap-3 rounded-lg px-3 py-2 text-sm transition-colors
            {currentPath === item.href
						? 'bg-muted text-primary hover:bg-muted/80'
						: 'text-muted-foreground hover:bg-muted hover:text-primary'}"
				>
					{#if item.icon}
						<span class="h-4 w-4">{item.icon}</span>
					{/if}
					{#if !isCollapsed}
						<span>{item.title}</span>
					{/if}
				</a>
			{/each}
		</nav>
	</div>
</aside>
